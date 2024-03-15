import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# setting a service
serv = Service("C:/Users/seanp/Desktop/Self Improvement/Selenium Course - Python/chromedriver-win64/chromedriver.exe")

driver = webdriver.Chrome(service=serv)
driver.implicitly_wait(10) # WAIT MAX 5 SECONDS TO ELEMENT TO APPEAR

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.XPATH, "//input[@type='search']").send_keys("Cu")
time.sleep(3) # Needed more waiting
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
print(count)

for result in results:
    result.find_element(By.XPATH, "div/button").click()




flag = False
while True:
    pass
    inp = input()
    if inp == "1":
       flag = True
       if flag:
           break