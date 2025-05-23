
from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()
import pandas as pd


def dbconnect():
    engine = create_engine("mysql+pymysql://root:0308@localhost:3306/naver_book")
    conn = engine.connect()
    return conn

def to_book_db(keyword, df):
    """
    keyword와 df를 입력받아 네이버 도세어세 검색하고 5페이지 결과를
    {검색어명}_book_info형식의 테이블을 mysql에 저장
    """
    # data data 쿼리창 오픈
    conn = dbconnect()
    df.to_sql(f'{keyword}_book_info', con=conn, if_exists="append", index=False)
    conn.close()
    


        
       