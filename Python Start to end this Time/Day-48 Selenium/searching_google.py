from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_driver_path = "C:\Development\chromedriver.exe"


google_link = "https://www.google.com/"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
driver.get(google_link)

search = driver.find_element(By.NAME, "q")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
search.click()

