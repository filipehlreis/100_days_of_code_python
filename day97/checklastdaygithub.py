from datetime import datetime
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from twilio.rest import Client
import os

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
my_phone_number_twilio = os.environ['my_phone_number_twilio']
my_real_phone = os.environ['my_real_phone']


class CheckLastDayGitHubBot():
    def __init__(self, USER) -> None:
        self.USER = USER

        chrome_driver_path =\
            "C:\\github\\100_days_of_code_python\\chromedriver\\chromedriver.exe"

        ser = Service(chrome_driver_path)
        op = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=ser, options=op)

    def get_last_day_github(self):
        commit_level = 0

        URL_LINK = f"https://github.com/{self.USER}"
        self.driver.get(URL_LINK)

        contribuitions = self.driver.find_elements(
            By.CLASS_NAME, "ContributionCalendar-day"
        )
        today_day = str(datetime.today().date())

        try:
            for contribuition in contribuitions:
                if today_day == contribuition.get_attribute('data-date'):
                    commit_level = contribuition.get_attribute('data-level')
                    return commit_level
        except Exception as e:
            msg_error = e
            e = msg_error
            return commit_level

        return commit_level

    def send_sms_github(self, commit_level):
        client = Client(account_sid, auth_token)

        try:
            commit_level = int(commit_level)
            if commit_level == 0:
                body_message = "Vamos lá, Filipe, voce consegue codar alguma coisinha hoje!"
            elif commit_level == 1:
                body_message = "Muito bom, Filipe, objetivo diário alcançado!"
            elif commit_level > 1:
                body_message = "Excelente, Filipe! Vamos que vamos que o céu é o limite!"
            else:
                body_message = 'Erro. Partiu codar hoje resolvendo o possivel bug aqui.'
        except Exception as e:
            body_message = str(e)
            print(body_message)

        message = client.messages.create(
            body=body_message,
            from_=my_phone_number_twilio,
            to=my_real_phone
        )

        print(body_message)
        print(message.status)
