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

username.send_keys("hisherhim2022@gmail.com")
password.send_keys("Hajoo18cs75")
password.send_keys(Keys.ENTER)


apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button")
apply_button.click()


phone = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
phone.send_keys("1122334455")

next_button = driver.find_element(By.CLASS_NAME, "artdeco-button")
next_button.click()




driver.quit()





















































#
# email_or_phone = driver.find_element(By.ID, "username")
# print(email_or_phone.text)
# # email_or_phone.send_keys("hisherhim2022@gmail.com")
# # email_or_phone.send_keys(Keys.ENTER)
#
#
# password = driver.find_element(By.ID, "password")
# print(password.text)
# password.send_keys("Hajoo18cs75")
# password.send_keys(Keys.ENTER)




# time.sleep(3)
# login = driver.find_element(By.CSS_SELECTOR, ".btn__primary--large")
# print(login.text)
# login.click()

#
# search_job = driver.find_element(By.ID, "jobs-search-box-keyword-id-ember350")
# search_job.send_keys("Python developer")
# search_job.send_keys(Keys)
#

#
# easy_apply = driver.find_element(By.CSS_SELECTOR, ".artdeco-button__text")
# easy_apply.click()
#

# mobile_num = driver.find_element(By.CLASS_NAME, ".ember-view")
# mobile_num.send_keys("1122334455")
# mobile_num.send_keys(Keys.ENTER)
#
#
# next_button = driver.find_element(By.CLASS_NAME, ".artdeco-button__text")
# next_button.click()

