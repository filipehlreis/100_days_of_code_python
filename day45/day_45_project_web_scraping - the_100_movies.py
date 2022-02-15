import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline."\
    "com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
response.raise_for_status()

data = response.text

soup = BeautifulSoup(data, "html.parser")
all_h3_tags = soup.find_all("h3", class_="title")

titles = [
    all_h3_tags[-1-i].getText()
    for i in range(len(all_h3_tags))
]
# another way of reversing the list is "list[::-1]"

for title in titles:
    print(title)
    with open("day45\\list\\movies.txt", mode="a") as file:
        file.write(f"{title}\n")
