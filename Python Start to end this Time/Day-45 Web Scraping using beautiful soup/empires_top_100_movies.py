import requests
from bs4 import BeautifulSoup


movies_site = "https://timesofindia.indiatimes.com/entertainment/hindi/bollywood/top-20-best-bollywood-movies-of-2022"

response = requests.get(movies_site)
response_content = response.text

soup = BeautifulSoup(response_content, "html.parser")

all_movies = soup.find_all(name="h2")

movies_list = []

for item in all_movies:
    text = item.getText()
    # movies_list.append(text.replace('\n', ''))
    movies_list.append(text)


# print(movies_list)
with open("best_bollywood_movies_2022.txt", "w") as file:
    for item in movies_list:
        file.write(item)


