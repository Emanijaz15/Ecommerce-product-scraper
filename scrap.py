from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

chrome_options = Options()
# chrome_options.add_argument("--headless")  # Headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36")
service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)


driver.get("https://www.daraz.pk")
time.sleep(3)  

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("headphones")
search_box.send_keys(Keys.RETURN)
time.sleep(5)

product_name=[]
data = driver.find_elements(By.CSS_SELECTOR,'div.RfADt a')
for ta in data:
    product_name.append(ta.text)

product_price=[]
data = driver.find_elements(By.CSS_SELECTOR,'span.ooOxS')
for ta in data:
    product_price.append(ta.text)

df=pd.DataFrame({
    "Book Title": product_name,
    "Price": product_price
})

df.to_csv("headphones.csv", encoding='utf-8')
print("Data saved to books.csv")
driver.quit()
