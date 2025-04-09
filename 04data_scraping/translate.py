
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def translate (keyword):
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument("start-maximized")
    options.add_argument("Chrome/135.0.0.0")
    options.add_argument("lang=ko_KR")

    driver1 = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
        )
    url = "https://translate.google.com/?sl=ko&tl=en&op=translate"
    driver1.get(url)
    wait = WebDriverWait(driver1, 10)
    text_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.er8xn")))
    text_box.send_keys(keyword)
    text_box.send_keys(Keys.ENTER)
    keyword = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.ryNqvb")))
    keyword = keyword.text
    return keyword