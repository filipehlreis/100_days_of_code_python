from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

URL_PRODUCT = "https://orteil.dashnet.org/cookieclicker"

chrome_driver_path =\
    "C:\\github\\100_days_of_code_python\\day48\\chromedriver.exe"

ser = Service(chrome_driver_path)
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get(URL_PRODUCT)


big_cookie = driver.find_element(By.ID, "bigCookie")


for _ in range(100000000):
    big_cookie.click()
    product_enabled = driver.find_elements(
        By.CLASS_NAME, "unlocked")

    for products in product_enabled:
        products.click()
