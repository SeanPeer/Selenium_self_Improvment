from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium_utils import safe_click
import time

# setting a service
serv = Service("C:/Users/seanp/Desktop/Self Improvement/Selenium Course - Python/chromedriver.exe")

# Chrome web browser 
driver = webdriver.Chrome(service = serv) # opening web browser
driver.minimize_window() # Maximize window 
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

# Mark the up left section

radios = driver.find_elements(By.XPATH, "//input[@type='radio']")

for radio in radios:
    if radio.get_attribute("value") == "radio3":
        radio.click()


# Mark the center left - suggestion class 


# Mark the up right - Checkbox can be marked with few options 


checkboxs = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

for checkbox in checkboxs:
    if checkbox.get_attribute("value") == "option3":
        checkbox.click()


driver.find_element(By.XPATH, "//select[@id='dropdown-class-example']").click()
options = driver.find_elements(By.XPATH, "//select[@id='dropdown-class-example']/option")

for option in options:
    if option.get_attribute("value") == "option2":
        option.click()





# handle java pop up
MyName = "Sean Peer"
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(MyName)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alertext = driver.switch_to.alert.text
print(alertext)
alert.accept()


# driver.find_element(By.XPATH, "//div[1]/div[@class='cen-left-align']/fieldset/input").send_keys("isr")
time.sleep(2)
# safe_click(driver,By.XPATH,)
# driver.find_element(By.XPATH , "//ul/li/div[@id='ui-id-166']").click()