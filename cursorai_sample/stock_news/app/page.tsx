'use client';

import React, { useState, useEffect } from 'react';
import { Card, Title, AreaChart, BarChart, DonutChart, Text } from '@tremor/react';
import { MagnifyingGlassIcon } from '@heroicons/react/24/outline';

interface StockData {
  symbol: string;
  price: number;
  change: string;
  changePercent: string;
  volume: number;
  historicalData: {
    date: string;
    price: number;
    volume: number;
  }[];
}

interface NewsSummary {
  title: string;
  summary: string;
  keyPoints: string[];
  sentiment: string;
}

export default function Home() {
  const [stockData, setStockData] = useState<StockData | null>(null);
  const [newsSummaries, setNewsSummaries] = useState<NewsSummary[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchStockData();
    fetchNewsSummaries();
  }, []);

  const fetchStockData = async () => {
    try {
      const response = await fetch('/api/stock?symbol=AAPL');
      if (!response.ok) throw new Error('Failed to fetch stock data');
      const data = await response.json();
      setStockData(data);
    } catch (err) {
      setError('주식 데이터를 불러오는데 실패했습니다.');
    }
  };

  const fetchNewsSummaries = async () => {
    try {
      // 실제 구현에서는 최근 뉴스 데이터를 가져와야 합니다
      // 여기서는 더미 데이터를 사용합니다
      const dummyNews = [
        {
          title: "애플, 신제품 출시로 주가 상승",
          summary: "애플이 새로운 제품 라인업을 발표하며 주가가 상승세를 보이고 있습니다.",
          keyPoints: ["신제품 출시", "실적 예상치 상회", "시장 반응 긍정적"],
          sentiment: "positive"
        },
        {
          title: "글로벌 칩 부족 현상 지속",
          summary: "반도체 공급 부족으로 인한 영향이 지속되고 있습니다.",
          keyPoints: ["공급망 문제", "생산 지연", "가격 상승"],
          sentiment: "negative"
        },
        {
          title: "테슬라, 새로운 공장 건설 계획",
          summary: "테슬라가 새로운 전기차 공장 건설을 발표했습니다.",
          keyPoints: ["생산능력 확대", "일자리 창출", "지역 경제 활성화"],
          sentiment: "positive"
        }
      ];
      setNewsSummaries(dummyNews);
    } catch (err) {
      setError('뉴스 데이터를 불러오는데 실패했습니다.');
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-blue-500"></div>
      </div>
    );
  }

  return (
    <main className="min-h-screen p-8 bg-gray-50">
      <div className="max-w-7xl mx-auto">
        <h1 className="text-4xl font-bold text-center mb-8 text-gray-900">
          주식 시장 대시보드
        </h1>

        {error && (
          <div className="p-4 mb-4 text-red-700 bg-red-100 rounded-lg">
            {error}
          </div>
        )}

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
          {/* 주가 차트 */}
          <Card>
            <Title>주가 추이</Title>
            {stockData && (
              <AreaChart
                className="h-72 mt-4"
                data={stockData.historicalData}
                index="date"
                categories={["price"]}
                colors={["blue"]}
                valueFormatter={(number) => `$${number.toFixed(2)}`}
              />
            )}
          </Card>

          {/* 거래량 차트 */}
          <Card>
            <Title>거래량</Title>
            {stockData && (
              <BarChart
                className="h-72 mt-4"
                data={stockData.historicalData}
                index="date"
                categories={["volume"]}
                colors={["green"]}
                valueFormatter={(number) => number.toLocaleString()}
              />
            )}
          </Card>
        </div>

        {/* 주요 뉴스 섹션 */}
        <Card className="mb-8">
          <Title>주요 뉴스</Title>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mt-4">
            {newsSummaries.map((news, index) => (
              <Card key={index} className="p-4">
                <Text className="font-bold mb-2">{news.title}</Text>
                <Text className="text-sm mb-2">{news.summary}</Text>
                <div className="space-y-1">
                  {news.keyPoints.map((point, i) => (
                    <Text key={i} className="text-sm text-gray-600">
                      • {point}
                    </Text>
                  ))}
                </div>
                <div className={`mt-2 inline-block px-2 py-1 rounded-full text-xs font-medium ${
                  news.sentiment === 'positive' 
                    ? 'bg-green-100 text-green-800'
                    : news.sentiment === 'negative'
                    ? 'bg-red-100 text-red-800'
                    : 'bg-gray-100 text-gray-800'
                }`}>
                  {news.sentiment === 'positive' ? '긍정적' : 
                   news.sentiment === 'negative' ? '부정적' : '중립적'}
                </div>
              </Card>
            ))}
          </div>
        </Card>

        {/* 뉴스 URL 입력 폼 */}
        <Card>
          <Title>새로운 뉴스 분석</Title>
          <form className="mt-4">
            <div className="flex gap-4">
              <input
                type="url"
                placeholder="뉴스 URL을 입력하세요"
                className="flex-1 p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              />
              <button
                type="submit"
                className="px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 flex items-center gap-2"
              >
                <MagnifyingGlassIcon className="w-5 h-5" />
                분석하기
              </button>
            </div>
          </form>
        </Card>
      </div>
    </main>
  );
} 