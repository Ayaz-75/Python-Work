from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_driver_path = "C:\Development\chromedriver.exe"

wiki_link = "https://en.wikipedia.org/wiki/Main_Page"
ser = Service(chrome_driver_path)
driver = webdriver.Chrome(service=ser)

# driver.get(wiki_link)
# num = driver.find_element(By.CSS_SELECTOR, "#articlecount a")

# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)



app_bary_link = "http://secure-retreat-92358.herokuapp.com/"
driver.get(app_bary_link)

f_name = driver.find_element(By.NAME, "fName")
f_name.send_keys("Ayaz")
f_name.send_keys(Keys.ENTER)

l_name = driver.find_element(By.NAME, "lName")
l_name.send_keys("Lakho")
l_name.send_keys(Keys.ENTER)

email = driver.find_element(By.NAME, "email")
email.send_keys("Lakho75@gmail.com")
email.send_keys(Keys.ENTER)


sign_up = driver.find_element(By.CSS_SELECTOR, "form button")
sign_up.click()







