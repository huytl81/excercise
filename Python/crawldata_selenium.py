# pip install selenium webdriver-manager


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_argument("--headless") # khong mo trinh duyet

# tuong tac voi trinh duyet
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
url = "https://quotes.toscrape.com"

driver.get(url) # get url
# goi ham sleep de load het toan bo trang
time.sleep(3)

def scrape_quotes():
    quotes = driver.find_elements(By.CLASS_NAME, "text")
    for quote in quotes:
        print(quote.text)

# authors = driver.find_elements(By.CLASS_NAME, "author")
# for author in authors:
#     print(author.text)

scrape_quotes() # da lay data page dau tien

# tiep tuc crawl 3 page nua ngoai page dau tien
for _ in range(3):
    next_button = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/nav/ul/li/a")
    next_button.click()
    time.sleep(3) # nghi 3s de page duoc load hoan toan
    scrape_quotes()

driver.quit()



