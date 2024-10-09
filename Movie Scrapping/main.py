from bs4 import BeautifulSoup
import requests
#
# # with open("website.html") as file:
# #
# #     content = file.read()
# #
# #
# # soup = BeautifulSoup(content, "html.parser")
# #
# # for tag in soup.find_all(name="a"):
# #     # print(tag.get("href"))
# #     pass
# #
# # heading = soup.find(name='h1', id="name")
# # # print(heading)
# #
# # find = soup.find_all(name="h3")
# # #print(find)
# #
# # print(soup.select(selector="p a")[0].get("href"))
#
#
# response = requests.get("https://news.ycombinator.com/")
#
# soup = BeautifulSoup(response.text, "html.parser")
# alll = soup.find_all(name="span", class_="score")
# title_li = []
# find = soup.select(selector="span.titleline a")
# print(find)
# for list in find:
#     title_li.append(list.string)
#
#
# number_li =[]
#
# id = []
# for lists in alll:
#     number_li.append((int(lists.getText().split()[0])))
#     id.append(lists.get("id"))
#
# print(number_li)
# print(title_li)
# max = max(number_li)
# ind = number_li.index(max)
# print(f"Currently Trending post is: {title_li[ind]}, with {max} votes.")
#
#
#

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.text,"html.parser")
text = soup.select("h3.listicleItem_listicle-item__title__BfenH")
number = 99
for movies in range(100):
    movie = text[number].string
    with open("movies.txt", mode="a") as file:
        file.write(f" {movie}\n")
        number-=1

