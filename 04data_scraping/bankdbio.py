from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()
import pandas as pd
import time


def dbconnect():
    engine = create_engine("mysql+pymysql://root:0308@localhost:3306/bank_reviews")
    
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
    

def review_extraction(all_reviews):
    all_result = []
    for review in reviews :
        date = review.find_element(By.CSS_SELECTOR,'span.bp9Aid').text.replace("년","").replace("월","").replace("일","").replace(" ","-")
        rate = review.find_element(By.CSS_SELECTOR, "div.Jx4nYe > div").get_attribute("aria-label").split()[3][0]
        user = review.find_element(By.CSS_SELECTOR,'div.h3YV2d').text
        try:
            answer = review.find_element(By.CSS_SELECTOR,'div.odk6He div.ras4vb').text
        except:
            answer = None
        result= (date, rate, user, answer,)
        all_result.append(result)

    result_df = pd.DataFrame(all_result, columns=['리뷰일', '평점', '사용자리뷰', '업체답변'])
    result_df
    to_bank_db(page,result_df)
    print(f"{page}저장 완료")
        
       



def bank_app_reviews(bank, month=1):
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument("start-maximized")
    options.add_argument("Chrome/135.0.0.0")
    options.add_argument("lang=ko_KR")


    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
        )
    driver.get("https://play.google.com/store/apps/details?id="+page+"&hl=ko")


    wait = WebDriverWait(driver, 20)
    button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[aria-label='평점 및 리뷰 자세히 알아보기']")
    ))
    button.click()
    drop_down = wait.until(EC.element_to_be_clickable(
        (By.ID, "sortBy_1")
    ))
    drop_down.click()
    latest_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'span[aria-label="최신"]')
    ))
    time.sleep(3)
    latest_button.click()

    end_date = datetime.today() - timedelta(days=month*30)
    current_date = ""
    all_reviews = ""

    while True :
        try :
            # 리뷰가 담긴 창을 찾아서 JavaScript로 1000px씩 아래로 스크롤
            driver.execute_script("document.querySelector('.fysCi.Vk3ZVd').scrollBy(0, 1000)")
            # 페이지 로딩 기다리기
            time.sleep(2)
            
            reviews = driver.find_elements(By.CSS_SELECTOR, '.RHo1pe')
            current_date = reviews[-1].find_element(By.CSS_SELECTOR,'span.bp9Aid').text.replace("년","").replace("월","").replace("일","").replace(" ","-")
            current_date = datetime.strptime(current_date,"%Y-%m-%d")
            print(f"{page} 현재리뷰날짜{current_date},리뷰수:{len(reviews)}", end="\r")
        except: 
            reviews = driver.find_elements(By.CSS_SELECTOR, ".RHo1pe")
            print(f"{page} 현재리뷰날짜{current_date},리뷰수:{len(reviews)}", end="\r")
            
        if current_date < end_date :
            break
            
    return all_reviews