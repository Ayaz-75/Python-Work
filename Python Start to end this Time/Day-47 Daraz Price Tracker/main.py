import requests
from bs4 import BeautifulSoup


product_url = "https://stats.espncricinfo.com/ci/content/records/208504.html"


response = requests.get(product_url)
response_content = response.text
soup = BeautifulSoup(response_content, "html.parser")

details = soup.find_all(name="table")
print(details)

























# print(soup.prettify())
# record_table = soup.select(selector="table tbody tr")
#
# names_list = []
# scores_list = []
#
#
# for item in record_table:
#     names = item.find_all(name="a", class_="data-link")
#     names_list.append(names)
#
#
#     scores = item.find_all(name="b")
#     scores_list.append(scores)
#
#
# print(names_list)
# print(scores_list)

