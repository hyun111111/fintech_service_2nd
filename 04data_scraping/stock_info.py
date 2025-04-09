import os
import requests
import time
import pandas as pd
from bs4 import BeautifulSoup as bs
from datetime import datetime
from sqlalchemy import create_engine, text
import pymysql
pymysql.install_as_MySQLdb()

page = 1
company_infos = []
while True:
    url = "https://kind.krx.co.kr/corpgeneral/corpList.do"
    payload= dict(method="searchCorpList", pageIndex=page, 
                  currentPageSize=100,orderMode=3, 
              orderStat='D',searchType=13, fiscalYearEnd="all",location="all")
    r = requests.get(url, payload)
    response = r.content
    soup = bs(response, "lxml")
    time.sleep(5)
    total_pages = int(soup.select_one(".info.type-00 >em").text.replace(",","")) // 100 +1
    
    for idx, tr in enumerate(soup.select("tbody > tr")) :
        print(f'{page}/{total_pages}중, {idx}/{len(soup.select("tbody > tr"))}작업중', end="\r")
        # 주식 종목
        stock_type = tr.select_one("td:nth-child(1) > img")['alt']
        # 회사명
        company_name = tr.select_one("td:nth-child(1) > a")["title"]
        # 종목코드
        code = tr.select_one("td:nth-child(1) > a")["onclick"].split("'")[1]
        # 업종
        business_type = tr.select_one("td:nth-child(2)").text 
        # 주요제품 
        product = tr.select_one("td:nth-child(3)").text 
        # 상장일
        resi_date = tr.select_one("td:nth-child(4)").text 
        # 결산월 
        settlment = tr.select_one("td:nth-child(5)").text 
        # 대표자명
        ceo = tr.select_one("td:nth-child(6)").text
        # 홈페이지
        hompage = tr.select_one("td:nth-child(7) a")['href'] if tr.select_one("td:nth-child(7) a") != None else ""
        # 지역
        location = tr.select_one("td:nth-child(8)").text
        
        company_infos.append((stock_type, company_name, code, business_type, product, 
                          resi_date, settlment, ceo, hompage, location))
    if page < total_pages : 
            page += 1
    else :
        break 

 # 컬럼명
columns =soup.select_one("table")['summary'].split(", ")
columns.insert(0, "주식종목")
columns.insert(2, "종목코드")
df = pd.DataFrame(company_infos, columns=columns )



today = datetime.now()
today = f"{today.year}_{today.month:02d}_{today.day:02d}"

#폴더 자동 생성
if not os.path.exists("./scraping_result"):
      os.mkdir("scraping_result")

df.to_csv(f"./{today}법인상장정보.csv", encoding="utf-8-sig", index=False )
print(f"./scraping_result/{today}_상장법인정보 엑셀 저장완료")



# localhost = 127.0.0.1와 3306은 같다
engine = create_engine("mysql+pymysql://root:0308@localhost:3306/stock_info")
# engine.connect create_engine에 있는 정보로 db접속
conn = engine.connect()

# 테이터 프레임을 db에 저장하기 to_sql("테이블명")
df.to_sql(f"stock_company_info_{today}", con=conn, if_exists="replace", index= False)
conn.close()
print(f"{today}_상장법인정보 데이터베이스 저장완료")