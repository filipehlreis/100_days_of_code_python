from local_settings.local_settings import TWITTER_EMAIL, TWITTER_USERNAME
from local_settings.local_settings import TWITTER_PASSWORD
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By


class InternetSpeedTwitterBot():
    def __init__(self, PROMISED_DOWN, PROMISED_UP) -> None:
        self.PROMISED_DOWN = PROMISED_DOWN
        self.PROMISED_UP = PROMISED_UP

        chrome_driver_path =\
            "C:\\github\\100_days_of_code_python\\chromedriver\\chromedriver.exe"

        ser = Service(chrome_driver_path)
        op = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=ser, options=op)

        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        URL_LINK = "https://www.speedtest.net"
        self.driver.get(URL_LINK)
        sleep(3)
        button_go = self.driver.find_element(
            By.CSS_SELECTOR, "div.start-button > a")
        button_go.click()

        sleep(55)

        try:
            popup_msg = self.driver.find_element(
                By.LINK_TEXT, "Back to test results")
            popup_msg.click()
            sleep(2)
        except Exception as e:
            print(f"\n\n{e}\n\n")
        finally:
            download = self.driver.find_element(
                By.CSS_SELECTOR, "span.result-data-large.number.result-data-value.download-speed")
            self.down = float(download.text)
            upload = self.driver.find_element(
                By.CSS_SELECTOR, "span.result-data-large.number.result-data-value.upload-speed")
            self.up = float(upload.text)
            print(f"\nDownload: {self.down}\nUpload: {self.up}")

    def tweet_at_provider(self):
        URL_LINK = "https://twitter.com/i/flow/login"
        self.driver.get(URL_LINK)
        self.driver.maximize_window()

        sleep(2)
        input_username = self.driver.find_element(
            By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input')
        input_username.send_keys(TWITTER_EMAIL)
        input_username.send_keys(Keys.ENTER)
        sleep(2)

        try:
            popup_confirmation = self.driver.find_element(
                By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            popup_confirmation.send_keys(TWITTER_USERNAME)
            popup_confirmation.send_keys(Keys.ENTER)
            sleep(2)
        except Exception as e:
            print(f"\n\n{e}\n\n")
        finally:
            input_password = self.driver.find_element(
                By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input')
            input_password.send_keys(TWITTER_PASSWORD)
            input_password.send_keys(Keys.ENTER)

        sleep(2)
        input_msg_twitt = self.driver.find_element(
            By.CSS_SELECTOR, "div.public-DraftStyleDefault-block.public-DraftStyleDefault-ltr > span")

        msg_twit = f"Hey Provedor de Internet, por que minha velocidade de"\
            f"internet está {self.down}down/{self.up}up enquanto que eu pago"\
            f"{self.PROMISED_DOWN}down/{self.PROMISED_UP}up?"

        input_msg_twitt.send_keys(msg_twit)

        sleep(2)
        button_msg_twettar = self.driver.find_element(
            By.XPATH,
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div'
        )
        button_msg_twettar.click()
