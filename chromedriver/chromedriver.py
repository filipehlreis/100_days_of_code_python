from selenium.webdriver.chrome.service import Service
from selenium import webdriver


def get_chromedriver():
    chrome_driver_path =\
        "C:\\github\\100_days_of_code_python\\chromedriver\\chromedriver.exe"
    ser = Service(chrome_driver_path)
    op = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ser, options=op)

    return driver
