from random import random
from local_settings.local_settings import INSTAGRAM_PASSWORD
from local_settings.local_settings import INSTAGRAM_USER
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By


class InstagramFollowersBot():
    def __init__(self) -> None:

        chrome_driver_path =\
            "C:\\github\\100_days_of_code_python\\chromedriver\\chromedriver.exe"

        ser = Service(chrome_driver_path)
        op = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=ser, options=op)

    def login(self):
        URL_PAGE = "https://www.instagram.com/accounts/login"

        self.driver.get(URL_PAGE)
        sleep(2)
        input_email = self.driver.find_element(
            By.CSS_SELECTOR, "input._2hvTZ.pexuQ.zyHYP")
        input_email.send_keys(INSTAGRAM_USER)
        input_password = self.driver.find_element(
            By.CSS_SELECTOR,
            "#loginForm > div > div:nth-child(2) > div > label > input"
        )
        input_password.send_keys(INSTAGRAM_PASSWORD)
        input_password.send_keys(Keys.ENTER)
        sleep(3)

        try:
            input_ativar_notif = self.driver.find_element(
                By.CSS_SELECTOR,
                "button.aOOlW.HoLwm")
            input_ativar_notif.click()
        except Exception:
            # print(f"\n\n{e}\n\n")
            pass

    def find_followers(self, user):
        self.driver.get(f"https://www.instagram.com/{user}")
        sleep(2)
        button_followers = self.driver.find_element(
            By.CSS_SELECTOR,
            "#react-root > section > main > div > header > section > ul > li:nth-child(3)"
        )
        button_followers.click()

    def follow(self):
        for _ in range(3):
            sleep(random()+random()+1)
            followers_list = self.driver.find_elements(
                By.CSS_SELECTOR,
                "body > div.RnEpo.Yx5HN > div > div > div > div.isgrP > ul > div > li"
            )
            for follower in followers_list:
                sleep(0.3)
                try:
                    follower.find_element(
                        By.CSS_SELECTOR,
                        "button.sqdOP.L3NKy.y3zKF"
                    ).click()
                except Exception as e:
                    print(f"\n\n{e}\n\n")
