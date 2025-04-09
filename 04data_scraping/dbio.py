
from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()
import pandas as pd
from datetime import datetime

def year_month():
    today = datetime.today()
    return today.year, today.month

def dbconnect():
    engine = create_engine("mysql+pymysql://root:0308@localhost:3306/stock_info")
    conn = engine.connect()
    return conn

def stock_codes():
    """ 
    my sql에 접속해서 상장 정보를 가져와 데이터프레임으로 반환해주는 코드 
    상장회사의 종목코드 6자리를 반환
    """
    conn = dbconnect()
    data = pd.read_sql('stock_company_info_2025_4_7', con=conn)
    conn.close()
    stock_codes = data['종목코드'].apply(lambda x: x+"0")
    return stock_codes

def to_stock_db(idx, df):
    """
    idx , stock 코드 코드네임을 df를 입력받아
    stock_price_{year}_{month:02d}형식의 테이블을 mysql에 저장
    """
    #오늘 기준 연도, 달 출력
    year, month = year_month()
    # data data 쿼리창 오픈
    conn = dbconnect()
    df.to_sql(f'stock_price_{year}_{month:02d}', con=conn,  if_exists="append", index=False)
    conn.close()
    print(f"{idx+1}/{len(stock_codes)}{stock_name}db저장완료 ", end="\r")
    return



        
       