from pprint import pprint
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests


class DataEntryJobAutomation():
    def __init__(self) -> None:
        self.captura_completa = False

    def get_research_houses(self, url_zillow):
        self.url_zillow = url_zillow
        headers_list = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 "
            "Safari/537.36 OPR/83.0.4254.27",
            "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"
        }

        response = requests.get(self.url_zillow, headers=headers_list)
        response.raise_for_status()

        data = response.text
        soup = BeautifulSoup(data, "html.parser")

        print()
        # Getting all the links elements
        links_element = soup.select(".list-card-info a")

        all_links = []
        for link in links_element:
            href = link["href"]
            if "http" not in href:
                href = f"https://www.zillow.com{href}"
            print(href)
            all_links.append(href)
        print(f"Tamanho de links: {len(all_links)}\n")

        # Getting all the rent values
        rent_values_elements = soup.select("div .list-card-price")

        all_rent_values = []
        for rent_value in rent_values_elements:
            value = rent_value.getText().split("/")[0].split("+")[0]
            print(value)
            all_rent_values.append(value)
        print(f"Tamanho de alugueis: {len(all_rent_values)}\n")

        # Getting all the address
        all_address_elements = soup.select(".list-card-addr")

        all_address = []
        for address in all_address_elements:
            address_text = address.getText()
            print(address_text)
            all_address.append(address_text)
        print(f"Tamanho de Enderecos: {len(all_address)}\n")

        if len(all_address) == len(all_links) and \
                len(all_links) == len(all_rent_values):
            self.tamanho = len(all_links)
            self.lista = [
                {
                    "address": all_address[i],
                    "rent-value": all_rent_values[i],
                    "link": all_links[i],
                }
                for i in range(self.tamanho)
            ]
            pprint(self.lista)
            self.captura_completa = True
        else:
            print("Houve problemas na captura dos dados.")
            self.captura_completa = False

    def inicializar_driver(self):
        chrome_driver_path =\
            "C:\\github\\100_days_of_code_python\\chromedriver\\chromedriver.exe"

        ser = Service(chrome_driver_path)
        op = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=ser, options=op)

    def send_forms(self, url_form):
        self.url_form = url_form
        if self.captura_completa:
            self.inicializar_driver()
            self.driver.get(self.url_form)

            for indice in range(self.tamanho):
                sleep(2)

                input_address = self.driver.find_element(
                    By.CSS_SELECTOR,
                    "#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(1) > div > div > div.freebirdFormviewerComponentsQuestionTextRoot > div > div.quantumWizTextinputPaperinputMainContent.exportContent > div > div.quantumWizTextinputPaperinputInputArea > input"
                )
                input_address.send_keys(self.lista[indice]["address"])

                input_rent = self.driver.find_element(
                    By.CSS_SELECTOR,
                    "#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(2) > div > div > div.freebirdFormviewerComponentsQuestionTextRoot > div > div.quantumWizTextinputPaperinputMainContent.exportContent > div > div.quantumWizTextinputPaperinputInputArea > input"
                )
                input_rent.send_keys(self.lista[indice]["rent-value"])

                input_link = self.driver.find_element(
                    By.CSS_SELECTOR,
                    "#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(3) > div > div > div.freebirdFormviewerComponentsQuestionTextRoot > div > div.quantumWizTextinputPaperinputMainContent.exportContent > div > div.quantumWizTextinputPaperinputInputArea > input"
                )
                input_link.send_keys(self.lista[indice]["link"])

                button_send = self.driver.find_element(
                    By.XPATH,
                    '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span'
                )
                button_send.click()

                button_resend = self.driver.find_element(
                    By.LINK_TEXT,
                    "Enviar outra resposta"
                )
                button_resend.click()

            self.driver.close()
        else:
            print("Não foi possivel enviar os dados para o formulario.")
