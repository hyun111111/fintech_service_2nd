import { NextResponse } from 'next/server';
import axios from 'axios';
import * as cheerio from 'cheerio';
import OpenAI from 'openai';

// OpenAI API 키 설정
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

// 뉴스 내용 추출 함수
async function extractNewsContent(url: string) {
  try {
    const response = await axios.get(url);
    const $ = cheerio.load(response.data);
    
    // 메타 태그에서 제목 추출
    const title = $('meta[property="og:title"]').attr('content') || 
                 $('title').text() || 
                 $('h1').first().text();

    // 본문 내용 추출 (일반적인 뉴스 사이트 구조에 맞춤)
    const content = $('article').text() || 
                   $('.article-content').text() || 
                   $('.news-content').text() || 
                   $('main').text();

    return { title, content: content.trim() };
  } catch (error) {
    console.error('Error extracting news content:', error);
    throw new Error('Failed to extract news content');
  }
}

// OpenAI를 사용한 요약 함수
async function summarizeWithAI(title: string, content: string) {
  try {
    const prompt = `
      다음 주식 관련 뉴스를 요약해주세요:
      
      제목: ${title}
      
      내용: ${content}
      
      다음 형식으로 응답해주세요:
      1. 간단한 요약 (2-3문장)
      2. 주요 포인트 (3-4개)
      3. 감성 분석 (positive/negative/neutral)
    `;

    const completion = await openai.chat.completions.create({
      model: "gpt-3.5-turbo",
      messages: [
        {
          role: "system",
          content: "You are a financial news analyst. Summarize the given news article in Korean."
        },
        {
          role: "user",
          content: prompt
        }
      ],
      temperature: 0.7,
    });

    const response = completion.choices[0].message.content;
    
    // 응답 파싱
    const lines = response?.split('\n').filter(line => line.trim());
    const summary = lines?.[0] || '';
    const keyPoints = lines?.slice(1, -1).map(point => point.replace(/^\d+\.\s*/, '')) || [];
    const sentiment = lines?.[lines.length - 1].toLowerCase().includes('positive') ? 'positive' :
                     lines?.[lines.length - 1].toLowerCase().includes('negative') ? 'negative' : 'neutral';

    return {
      title,
      summary,
      keyPoints,
      sentiment
    };
  } catch (error) {
    console.error('Error summarizing with AI:', error);
    throw new Error('Failed to summarize with AI');
  }
}

export async function POST(request: Request) {
  try {
    const { url } = await request.json();

    // 뉴스 내용 추출
    const { title, content } = await extractNewsContent(url);

    // AI를 사용한 요약
    const summary = await summarizeWithAI(title, content);

    return NextResponse.json(summary);
  } catch (error) {
    console.error('Error in summarize API:', error);
    return NextResponse.json(
      { error: 'Failed to summarize news' },
      { status: 500 }
    );
  }
} 