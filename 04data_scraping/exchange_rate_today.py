def new_cols(df):
    new_cols =[]
    for cols in df.columns:
        if cols[0] == cols[1] == cols[0]:
            new_cols.append(cols[0].replace(" ","_"))
        else:
            new_cols.append(" ".join(cols).strip().replace(" ","_"))
    return new_cols

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import time 
import pandas as pd
from io import StringIO
from exdb_io import to_ex_db

options = Options()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
options.add_argument("Chrome/135.0.0.0")
options.add_argument("lang=ko_KR")
# 셀레니움 브라우저가 닫혔을 때를 방지
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dav-shm-usage")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
    )
driver.get("https://www.kebhana.com/cms/rate/index.do?contentUrl=/cms/rate/wpfxd651_01i.do#//HanaBank")


today = datetime.today()
# 날짜를 'YYYY-MM-DD' 형식으로 변환
today_str = today.strftime("%Y-%m-%d")


if today.weekday() < 5:
    wait = WebDriverWait(driver, 20)
    date_element = wait.until(EC.presence_of_element_located((By.ID,"tmpInqStrDt")))
    date_element.clear()
    date_element.send_keys(today_str)
                                    
    btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btnDefault.bg")))
    btn.click()

    time.sleep(2)                                                        
    df = pd.read_html(StringIO(driver.find_element(By.CSS_SELECTOR, ".tblBasic.leftNone").get_attribute("outerHTML")))[0]
    df['date'] =  today_str
    new_columns = new_cols(df)
    df.columns = new_columns
    df = df[['date','통화','현찰_사실_때_환율','현찰_사실_때_Spread','현찰_파실_때_환율',
                '현찰_파실_때_Spread','송금_보낼_때_보낼_때','송금_받을_때_받을_때',
                '외화_수표_파실때','매매_기준율','환가_료율','미화_환산율']]
    to_ex_db(df)                                                         
    print(today_str)                                                        
else :
    pass

