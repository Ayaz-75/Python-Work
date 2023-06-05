import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

URL = "https://www.empireonline.com/movies/features/best-movies-2/"
chrome_driver_path = "D:\Development\chromedriver.exe"

s = Service(chrome_driver_path)
webdriver = webdriver.Chrome(service=s)

with webdriver as driver:
    # Set timeout time
    wait = WebDriverWait(driver, 10)

    # Retrieve url in headless browser
    driver.get(URL)

    html = driver.page_source

    driver.close()


soup = BeautifulSoup(html, 'html.parser')

titles = soup.find_all(name='h3', class_='jsx-2692754980')
titles = [i.text for i in titles if i.text is not None]
print(titles)



















# response = requests.get(URL)
# website_html = response.text
#
# soup = BeautifulSoup(website_html, "html.parser")
#
# all_movies = soup.find_all(name="h3")
# print(all_movies)


# movie_titles = [movie.getText() for movie in all_movies]
# movies = movie_titles[::-1]
#
# with open("movies.txt", mode="w") as file:
#     for movie in movies:
#         file.write(f"{movie}\n")




