from selenium.webdriver.common.keys import Keys
from pprint import pprint
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

URL_PRODUCT = "https://pt.wikipedia.org/wiki/Wikipédia:Página_principal"

chrome_driver_path =\
    "C:\\github\\100_days_of_code_python\\day48\\chromedriver.exe"

ser = Service(chrome_driver_path)
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)


# driver.get(URL_PRODUCT)

# numbers_artigos_element = driver.find_element(
#     By.XPATH, '//*[@id="mw-content-text"]/div[1]/div[1]/div/div[1]/table/tbody/tr/td[2]/div/p/b[1]')


# numbers_artigos = numbers_artigos_element.text.replace(' ', '')

# print(
#     int(numbers_artigos)
# )

# all_portals = driver.find_element(By.LINK_TEXT, "Portais")
# # all_portals.click()
# search_input = driver.find_element(By.NAME, "search")
# search_input.send_keys("Python")
# search_input.send_keys(Keys.ENTER)


URL_PRODUCT = "http://secure-retreat-92358.herokuapp.com"
driver.get(URL_PRODUCT)

fname = driver.find_element(By.NAME, "fName")
lname = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
button = driver.find_element(By.CLASS_NAME, "btn-primary")


fname.send_keys("Filipe")
lname.send_keys("Reis")
email.send_keys("filipe@email.com.br")
button.click()


# driver.close()
