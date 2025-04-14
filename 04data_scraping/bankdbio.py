from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()
import pandas as pd
import time


def dbconnect():
    engine = create_engine("mysql+pymysql://root:0308@localhost:3306/3306/bank_reviews")
    conn = engine.connect()
    return conn

def to_bank_db(bank, df):
    """
    google play 은행앱 리뷰를 DB에 저장하는 함수
    """
    # data data 쿼리창 오픈
    conn = dbconnect()
    time.sleep(1)
    df.to_sql(f'{page}_reviews', con=conn, if_exists="append", index=False)
    conn.close()
    


        
       
