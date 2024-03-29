
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# setting a service
serv = Service("C:/Users/seanp/Desktop/Self Improvement/Selenium Course - Python/chromedriver-win64/chromedriver.exe")

driver = webdriver.Chrome(service=serv)
driver.implicitly_wait(10) # WAIT MAX 5 SECONDS TO ELEMENT TO APPEAR

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
products = driver.find_elements(By.XPATH, "//div[@class='products']/div/h4")
list_products = []
for product in products:
    list_products.append(product.text)

driver.find_element(By.XPATH, "//input[@type='search']").send_keys("Cu")
time.sleep(3) # Needed more waiting
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
print(count)

for result in results:
    print(result.text)
    result.find_element(By.XPATH, "div/button").click()
driver.find_element(By.XPATH, "//a[@class='cart-icon']").click()
#time.time(2)
driver.find_element(By.XPATH, "//div[@class='action-block']/button[1]").click()

items = driver.find_elements(By.XPATH, "//tr/td[5]/p") # All the prices of the items in the cart
total = 0

for item in items:
    print(item.text)
    total += int(item.text) # Sum the price of each item

print(total)
web_total = int(driver.find_element(By.XPATH, "//span[@class='totAmt']").text)
assert total == web_total, f"web total is not equal to sum, got: {web_total}"

# Assignment
web_total_after_dis = int(driver.find_element(By.XPATH, "//span[@class='discountAmt']").text)
assert web_total >= web_total_after_dis, f"After discount client is paying more, got: {web_total_after_dis}"
print(list_products)
# done assignment
flag = False
while True:
    pass
    inp = input()
    if inp == "1":
       flag = True
       if flag:
           break