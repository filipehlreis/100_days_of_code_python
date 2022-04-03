import pandas
from pprint import pprint
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path =\
    "C:\\github\\100_days_of_code_python\\chromedriver\\chromedriver.exe"

ser = Service(chrome_driver_path)
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)


URL_LINK = "https://www.allrecipes.com"
driver.get(URL_LINK)

sleep(2)

# css selector directory to search ids
all_recipes_css = "div.component.card.card__category"

# search for all cards of recipes
all_recipes_elements_list = driver.find_elements(
    By.CSS_SELECTOR, all_recipes_css
)

# get all the IDs founded in the search
all_recipes_ids_list = [
    recipe.get_attribute("data-content-graph-id")
    for recipe in all_recipes_elements_list[1:]
]

all_recipes_list = []

# get all recipe's main page info inside this for loop
for recipe_id in all_recipes_ids_list:
    div_recipe_root_css = f"div[data-content-graph-id='{recipe_id}']"

    div_recipe = f"{div_recipe_root_css}>div:nth-child(2)>div"

    # get info about LINK and TITLE of the recipes.
    link_div_class2 = f"{div_recipe}>a"

    link_title_recipe = driver.find_element(
        By.CSS_SELECTOR, link_div_class2
    )

    title_recipe = link_title_recipe.get_attribute('title')
    link_recipe = link_title_recipe.get_attribute('href')

    # get info about RATING STARS and RATING VOTTING of the recipes.
    # some recipes don't have any voting, so there is no div about rating.
    try:
        rating_starts_recipe_css = f"{div_recipe}>div.card__ratingContainer>div>span.review-star-text.visually-hidden"
        rating_voting_recipe_css = f"{div_recipe}>div.card__ratingContainer>div>span.ratings-count.elementFont__details"

        rating_stars_recipe = driver.find_element(
            By.CSS_SELECTOR, rating_starts_recipe_css
        )

        rating_votting_recipe = driver.find_element(
            By.CSS_SELECTOR, rating_voting_recipe_css
        )

        rating_stars_recipe = str(rating_stars_recipe.text)
        rating_stars_recipe = str(rating_stars_recipe.split(':')
                                  [1].strip().split(' ')[0])
        rating_votting_recipe = int(rating_votting_recipe.text)

    except Exception as e:
        msg_error = e
        # print(msg_error)
        rating_stars_recipe = '0'
        rating_votting_recipe = 0

    # get info about SUMMARY of the recipes.
    summary_recipe_css = f"{div_recipe}>div.card__summary.elementFont__details--paragraphWithin.margin-8-tb"

    summary_recipe = driver.find_element(
        By.CSS_SELECTOR, summary_recipe_css
    )

    summary_recipe = summary_recipe.text

    recipe = {
        'title': title_recipe,
        'link': link_recipe,
        'summary': summary_recipe,
        'rating_stars': rating_stars_recipe,
        'rating_votting': rating_votting_recipe,
    }

    all_recipes_list.append(recipe)


pprint(all_recipes_list)

csv_file = "day92\\all_recipes.csv"
all_recipes_panda = pandas.DataFrame(all_recipes_list)
all_recipes_panda.to_csv(csv_file)


# sleep(2)
driver.quit()
# driver.close()
