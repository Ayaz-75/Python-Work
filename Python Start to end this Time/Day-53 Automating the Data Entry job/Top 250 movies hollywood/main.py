import requests
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



url = "https://www.imdb.com/chart/top/"

response = requests.get(url)
data = response.text

soup = BeautifulSoup(data, "html.parser")

table = soup.find('table')

all_links = table.find_all("a")

all_table_data = []

for item in all_links:
    text = item.text.replace('\n',"").strip()
    if text != "":
        all_table_data.append(text)


with open("movies.txt", mode="w") as file:
    try:
        [file.write(f"{name}\n") for name in all_table_data]

    except:
        file.readlines()



















