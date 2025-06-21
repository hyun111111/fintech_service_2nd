import { NextResponse } from 'next/server';
import axios from 'axios';

// 주식 데이터 가져오기
async function getStockData(symbol: string) {
  try {
    // 실제 구현에서는 Alpha Vantage나 다른 주식 API를 사용해야 합니다
    // 여기서는 더미 데이터를 반환합니다
    const dummyData = {
      symbol,
      price: Math.random() * 1000 + 100,
      change: (Math.random() * 10 - 5).toFixed(2),
      changePercent: (Math.random() * 5 - 2.5).toFixed(2),
      volume: Math.floor(Math.random() * 1000000),
      historicalData: Array.from({ length: 30 }, (_, i) => ({
        date: new Date(Date.now() - (29 - i) * 24 * 60 * 60 * 1000).toISOString().split('T')[0],
        price: Math.random() * 1000 + 100,
        volume: Math.floor(Math.random() * 1000000)
      }))
    };

    return dummyData;
  } catch (error) {
    console.error('Error fetching stock data:', error);
    throw new Error('Failed to fetch stock data');
  }
}

export async function GET(request: Request) {
  try {
    const { searchParams } = new URL(request.url);
    const symbol = searchParams.get('symbol') || 'AAPL';

    const stockData = await getStockData(symbol);
    return NextResponse.json(stockData);
  } catch (error) {
    return NextResponse.json(
      { error: 'Failed to fetch stock data' },
      { status: 500 }
    );
  }
} 