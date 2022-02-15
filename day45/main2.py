
from bs4 import BeautifulSoup
# import lxml

print()
file_directory = "day45\\website.html"

with open(file_directory) as file:
    data = file.read()

soup = BeautifulSoup(data, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# print(soup.prettify())

# print(soup.a)
# print(soup.li)

all_anchor_tags = soup.find_all(name="a")
all_p_tags = soup.find_all(name="p")

# print(all_anchor_tags)
# print()
# print(all_p_tags)

for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))
    pass


heading = soup.find(name="h1", id="name")
# print(heading)

section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
# print(section_heading.getText())
# print(section_heading.name)
# print(section_heading.get("class"))

company_url = soup.select_one(selector="p a")
print(company_url)

name_page = soup.select_one(selector="#name")
print(name_page)

headings = soup.select(".heading")
print(headings)
