"""
Challenge: Create an Automated Game Playing Bot
1. Go to the game website and familiarise yourself with how it works:

http://orteil.dashnet.org/experiments/cookie/ (classic version)

2. Create a bot using Selenium and Python to click on the cookie as fast
as possible.


3. Every 5 seconds, check the right-hand pane to see which upgrades are
affordable and purchase the most expensive one. You'll need to check how
much money (cookies) you have against the price of each upgrade.

e.g. both Grandma and Cursor are affordable as we have 103 cookies, but
Grandma is the more expensive one, so we'll purchase that instead of the
cursor.


HINT 1: https://www.w3schools.com/python/ref_string_split.asp

HINT 2: https://www.w3schools.com/python/ref_string_strip.asp

HINT 3: https://www.w3schools.com/python/ref_string_replace.asp

HINT 4: https://stackoverflow.com/questions/13293269/how-would-i-stop-a
-while-loop-after-n-amount-of-time

4. After 5 minutes have passed since starting the game, stop the bot
and print the "cookies/second". e.g. this is mine:


5. Once you've managed to get the bot to work, feel free to tweak the
algorithm if you think there is a better way to play the game. e.g.
Change the time, instead of every 5 seconds to check the upgrades, what
if you did every second. Or maybe the bot should buy all the affordable
upgrades. Post your algorithm in the Q&A and impress us all if you
manage to get a higher cookies/second with your algo.
"""


from __future__ import annotations
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

import time


# URL_PRODUCT = "https://orteil.dashnet.org/cookieclicker"
URL_PRODUCT = "http://orteil.dashnet.org/experiments/cookie"

chrome_driver_path =\
    "C:\\github\\100_days_of_code_python\\day48\\chromedriver.exe"

ser = Service(chrome_driver_path)
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get(URL_PRODUCT)


cookie = driver.find_element(By.ID, "cookie")
money = driver.find_element(By.ID, "money")


def get_resources_list():
    resources = driver.find_elements(By.CSS_SELECTOR, "div div div div")
    resources_inverted = [resources[-i-1] for i in range(len(resources))]
    return resources_inverted


resources = get_resources_list()

# for resource in resources:
#     print(resource.text)
#     print(resource.get_attribute("class"))

print("\n\n")

info_begin = time.time()
info_round = info_begin
print(info_begin)


def get_cost_resource(resource_text):
    _item_cost = resource_text.split("-")
    _cost = _item_cost[1].split("\n")
    _cost_item = _cost[0].strip()

    return int(_cost_item)


while True:
    info_time = time.time()
    cookie.click()
    # print(money.text)

    if (info_time - info_begin) > 10:
        print(f"Time's UP! {info_time}")
        break
    elif (info_time - info_round) > 2:
        print(f"Deu 5 segundos: {info_time}")
        info_round = info_time

        resources = get_resources_list()

        if resources[-1].get_attribute("class") == "":
            cost = get_cost_resource(resources[-1].text)
            print(cost)

            while True:
                cost = get_cost_resource(resources[-1].text)
                if cost < int(money.text):
                    resources[-1].click()
                else:
                    break

driver.close()
