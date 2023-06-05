from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service



link = "https://www.legacy.com/funeral-homes/alabama/sylacauga/madden-s-funeral-home/fh-8334"
chrome_driver_path = "D:\Development\chromedriver.exe"


s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
driver.get(link)



















