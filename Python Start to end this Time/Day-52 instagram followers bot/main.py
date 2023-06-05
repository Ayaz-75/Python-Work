import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



chrome_driver_path = Service("D:\Development\chromedriver.exe")
SIMILAR_ACCOUNT = "Chefsteps"


USER_NAME = "hisherhim2022@gmail.com"
PASSWORD = "Hajoo786"



class InstaFollower:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=driver_path)


    def login(self):
        self.driver.get("https://www.instagram.com/")
        wait = WebDriverWait(self.driver, 20)
        username = wait.until(EC.element_to_be_clickable((By.NAME, 'username')))
        time.sleep(5)
        password = wait.until(EC.element_to_be_clickable((By.NAME, "password")))

        time.sleep(5)
        username.send_keys(USER_NAME)
        time.sleep(5)
        password.send_keys(PASSWORD)

        time.sleep(5)
        password.send_keys(Keys.ENTER)




    def find_followers(self):
        time.sleep(5)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Not Now']"))).click()
        time.sleep(5)
        search_bar = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Search']")))
        search_bar.send_keys(SIMILAR_ACCOUNT)
        time.sleep(5)
        search_bar.send_keys(Keys.ENTER)

        time.sleep(5)
        followers_count = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_tv"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/ul/li[2]/a/div/span')
        followers_count.click()


    def follow(self):
        pass



bot = InstaFollower(driver_path=chrome_driver_path)
bot.login()

bot.find_followers()





















# //*[@id="loginForm"]/div/div[1]/div/label/input