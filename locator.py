from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# setting a service
serv = Service("C:/Users/seanp/Desktop/Self Improvement/Selenium Course - Python/chromedriver.exe")

# Chrome web browser 
driver = webdriver.Chrome(service = serv) # opening web browser
driver.maximize_window() # Maximize window 
driver.get("http:/www.rahulshettyacademy.com/angularpractice")

# There are alot of potential locators as - ID, Xpath, CSSselector, ClassName, Name, LinkText\
# These will help me to find the text box i want to fill


# Finding element by CSSselector - tagname[attribute='value'] 
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Sean Selenium")

# driver.find_element(By.NAME, "email")   # find the wanted element by name
driver.find_element(By.NAME, "email").send_keys("HelloWorld@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456789")
driver.find_element(By.ID, "exampleCheck1").click()

#driver.find_element(By.ID, "exampleFormControlSelect1").find_element("Female").is_selected()

driver.find_element(By.ID, "inlineRadio1").click()

driver.find_element(By.NAME, "bday").send_keys("18091994")

# Finding elements using Xpath - //tagname[@attribute='value']

driver.find_element(By.XPATH, "//input[@type='submit']").click()
driver.find_element(By.CSS_SELECTOR, "input[class='ng-untouched ng-pristine ng-valid']").clear()


message = driver.find_element(By.CLASS_NAME, "alert-success").text

# Select from a DROPDOWN 
drop_down = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
drop_down.select_by_index(1)


assert 'Success' in message

print(message)

#DO NOT CLOSE
while True:
    pass

# driver.close()
