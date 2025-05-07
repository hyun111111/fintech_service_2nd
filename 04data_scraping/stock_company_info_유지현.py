
from sqlalchemy import create_engine, text
import pymysql
pymysql.install_as_MySQLdb()
import requests
import time
import pandas as pd
from bs4 import BeautifulSoup as bs
from io import StringIO

def ensure_database_exists():
    """
    korean_stock 데이터베이스가 없다면 생성한다.
    """
    # mysql 시스템 DB에 접속
    engine = create_engine("mysql+pymysql://root:1234@127.0.0.1:3306")
    with engine.connect() as conn:
        conn.execute(text("CREATE DATABASE IF NOT EXISTS korean_stock DEFAULT CHARACTER SET utf8mb4"))


def dbconnect():
    # 먼저 데이터베이스가 존재하는지 확인 후 연결
    ensure_database_exists()
    engine = create_engine("mysql+pymysql://root:1234@127.0.0.1:3306/korean_stock")
    conn = engine.connect()
    return conn


def to_stock_db(idx, df):
    """
    idx , stock 코드 코드네임을 df를 입력받아
    company_info이름의  테이블을 mysql에 저장
    """
    # data data 쿼리창 오픈
    conn = dbconnect()
    df.to_sql(f'company_info', con=conn,  if_exists="replace", index=False)
    conn.close()
    print(f"{idx+1} 번째 company_info 테이블 저장 완료", end="\r")
    return

page = 1
result = []
while True:
    url = "https://kind.krx.co.kr/corpgeneral/corpList.do"
    payload = dict(method="searchCorpList", pageIndex=page, currentPageSize=100, orderMode=3, orderStat='D', searchType=13, fiscalYearEnd="all", location="all#")
    r = requests.get(url, params=payload) 
    response = r.content
    soup =  bs(response,"lxml")
    time.sleep(5)
    total_pages = int(soup.select_one(".info.type-00 >em").text.replace(",","")) // 100 +1
    
    for idx, corp_list in enumerate(soup.select("tbody > tr")):
        print(f'{page}/{total_pages}중, {idx}/{len(soup.select("tbody > tr"))}작업중', end="\r")
        s_type = corp_list.select_one("td:nth-child(1) img")['alt']
        company = corp_list.select_one("td:nth-child(1)")["title"]
        code = corp_list.select_one("td:nth-child(1) a")["onclick"].split("'")[1]
        business_type = corp_list.select_one("td:nth-child(2)")["title"]
        product = corp_list.select_one("td:nth-child(3)")["title"]
        date = corp_list.select_one("td:nth-child(4)").text
        settlment = corp_list.select_one("td:nth-child(5)").text
        ceo = corp_list.select_one("td:nth-child(6)").text
        homepage = corp_list.select_one("td:nth-child(7) a")['href'] if corp_list.select_one("td:nth-child(7) a") != None else ""
        location = corp_list.select_one("td:nth-child(8)").text
        result.append([s_type, company, code, business_type, product, date, settlment, ceo ,homepage, location])
    if page < total_pages : 
            page += 1
    else :
        break 
columns =soup.select_one("table")['summary'].split(", ")
columns.insert(0, "주식종목")
columns.insert(2, "종목코드")
df = pd.DataFrame(result, columns=columns )
to_stock_db(idx, df)