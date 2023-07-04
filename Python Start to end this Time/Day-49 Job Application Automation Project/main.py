from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


chrome_driver_path = "D:\Development\chromedriver.exe"


job_link = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
s = Service(chrome_driver_path)


driver = webdriver.Chrome(service=s)
driver.get(job_link)


sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()


time.sleep(5)


username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")

username.send_keys("your email")
password.send_keys("your password")
password.send_keys(Keys.ENTER)


apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button")
apply_button.click()


phone = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
phone.send_keys("1122334455")

next_button = driver.find_element(By.CLASS_NAME, "artdeco-button")
next_button.click()




driver.quit()

