from bs4 import BeautifulSoup
import requests
response = requests.get("https://news.ycombinator.com/")

response_content = response.text

soup = BeautifulSoup(response_content, "html.parser")
# print(soup.title.text)

articles = soup.find_all(name='a', class_="titlelink")
# print("Article Tag: ", article_tag)
# print(articles)

all_texts = []
all_links = []

for article_tag in articles:
    article_text = article_tag.getText()
    all_texts.append(article_text)
    article_links = article_tag.get('href')
    all_links.append(article_links)

# print(all_texts)
# print(all_links)

article_upvotes = soup.find_all(name='span', class_='score')
all_points = []
for votes in article_upvotes:
    all_points.append(int(votes.text.split()[0]))
# print(all_points)


largest_number = max(all_points)
# print(largest_number)

largest_index = all_points.index(largest_number)
print("Maximum Voted News: ", all_points[largest_index])
print("The Content: ", all_texts[largest_index])
print("The Link: ", all_links[largest_index])






















# total_votes = [all_points.append(int((votes.text).split()[0])) for votes in article_upvotes]
# print(total_votes)

# for article_tag in articles:
#     article_text = article_tag.getText()
# print("Article Text: ", article_text)
#
# article_link = article_tag.get('href')
# print("Article Link: ", article_link)
#
# article_upvotes = soup.find_all(name='span', class_='score')
# points_count = points_tag.getText()
# print(points_count)


































# with open('website.html', encoding="utf8") as file:
#     content = file.read()
#
# soup = BeautifulSoup(content, "html.parser")
# # print(soup.title)
#
# # print(soup.prettify())
# # all_anchor_tags = soup.findAll("a")
# # print(all_anchor_tags)
# #
# # only_text = [tags.getText() for tags in all_anchor_tags]
# # only_links = [tags.get('href') for tags in all_anchor_tags]
# # print(only_text)
# # print(only_links)
# ###################### Heading with id #######################
# # heading = soup.find(name='h1', id='name')
# # print(heading)
#
# # heading = soup.find(name='h3', class_='heading')
# # print(heading.getText())
#
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
# print(company_url.get('href'))
#
#
















