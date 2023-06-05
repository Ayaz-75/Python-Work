import requests
from bs4 import BeautifulSoup


web_url = "https://priceoye.pk/mobiles/pricelist/best-mobiles-under-40000?gclid=CjwKCAjw_ISWBhBkEiwAdqxb9sO9b0ta2Y1spq05JjcQSwCM6pj-L1U29W2cuyntqIhFG9Z7yntWVRoCgPYQAvD_BwE"

response = requests.get(web_url)
response_content = response.text

soup = BeautifulSoup(response_content, "html.parser")
prices = soup.find_all(name="span", class_="mkt-price")

all_sets = []
all_mobiles = soup.select(selector="h4 a")
for model in all_mobiles:
    names = model.getText()
    all_sets.append(names.strip())

print(all_sets)
all_prices = [price.getText() for price in prices]
print(all_prices)

new_line = "\n"

with open("price_and_mobile.txt", mode="w") as file:
    for set_price in range(len(all_prices)):
        file.write(f"{set_price+1}) {all_sets[set_price]}, {all_prices[set_price]}{new_line}")

























