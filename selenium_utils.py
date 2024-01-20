# selenium_utils.py
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

def safe_click(driver, by, value):
    try:
        element = driver.find_element(by,value)
        element.click()
        return True
    except WebDriverException as e:
        print("Error occurred during click : {e}")
        return False