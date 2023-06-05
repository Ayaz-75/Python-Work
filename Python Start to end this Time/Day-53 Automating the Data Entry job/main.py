import random
import pandas as pd
import requests
from bs4 import BeautifulSoup
from xlsxwriter import Workbook
import lxml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service

names_ = []
mileages_ = []
ratings_ = []
prices_ = []


for i in range(1, 11):
    # url = "https://www.cars.com/shopping/results/?page="+str(i)+"&page_size=20&list_price_max=&makes[]=mercedes_benz&maximum_distance=all&models[]=&stock_type=cpo&zip="
    url = "https://www.cars.com/shopping/results/?page="+str(i)+"&page_size=20&list_price_max=&makes[]=&maximum_distance=all&models[]=&stock_type=cpo&zip="
    response = requests.get(url)
    # print(response.status_code)

    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    all_vehicles = soup.find_all(name='div', class_="vehicle-card")

    all_vehicles_names = soup.find_all(name='a', class_='vehicle-card-link')

    all_mileages = soup.find_all(name="div", class_="mileage")

    all_ratings = soup.find_all(name="span", class_="sds-rating__count")

    all_prices = soup.find_all(name='span', class_='primary-price')


    for (name,mileage,rating,price) in zip(all_vehicles_names, all_mileages, all_ratings, all_prices):
        names = name.text.replace("\n","")
        names_.append(names)
        mileages = mileage.text.replace("\n","")
        mileages_.append(mileages)
        ratings = rating.text.replace("\n","")
        ratings_.append(ratings)
        prices = price.text.replace("\n","")
        prices_.append(prices)



mileages_[0] = random.choice(mileages_[1:])
cars = pd.DataFrame({'Car Names': names_,
                     'Mileages': mileages_,
                     'Ratings': ratings_,
                     'Prices': prices_
                     })


print(cars)

cars.to_excel("D:\Python Start to end this Time\Day-53 Automating the Data Entry job"
              "\Mercedes-Benz-dataset.xlsx", engine='xlsxwriter', index=False)


cars.to_csv("D:\Python Start to end this Time\Day-53 Automating the Data Entry job"
            "\Mercedes-Benz-dataset.csv", index=False)




# print(names_)
# print(mileages_)
# print(ratings_)
# print(prices_)



















#
# all_prices = soup.find_all(name='div', class_='price-section-vehicle-card')
#
# prices = []
# for price in all_prices:
#     text = price.text
#     prices.append(text)
#
# print(prices)










































# print(all_vehicles)
# print(all_prices)










