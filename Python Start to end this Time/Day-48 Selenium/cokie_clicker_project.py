from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys


chrome_driver_path = "D:\Development\chromedriver.exe"
cookie_link = "http://orteil.dashnet.org/experiments/cookie/"


s = Service(chrome_driver_path)

driver = webdriver.Chrome(service=s)

driver.get(cookie_link)


money = driver.find_element(By.ID, "money")

for i in range(10):
    cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")
    cookie.click()

f_money = float(money.text)

print(f_money)



# # gma = driver.find_element(By.CSS_SELECTOR, "#buyGrandma")
# # money_float = float(money.text)
# money = driver.find_element(By.ID, "money")
# money_float = float(money.text)

# while money_float < 1000:
# # money = driver.find_element(By.ID, "money")
#
#     money_float = float(money.text)
#     cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")
#     cookie.click()
#
#     if money_float > 500:
#         fac = driver.find_element(By.CSS_SELECTOR, "#buyFactory")
#         fac.click()
#
#     elif money_float > 111:
#         gma = driver.find_element(By.CSS_SELECTOR, "#buyGrandma")
#         gma.click()

    #
    # cookie.click()


# print(money_float)
