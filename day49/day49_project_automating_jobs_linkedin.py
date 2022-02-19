from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_driver_path =\
    "C:\\github\\100_days_of_code_python\\day48\\chromedriver.exe"

ser = Service(chrome_driver_path)
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

USUARIO = "email@email.com"
SENHA = "senha123"
CIDADE = "cidade"
TERMO_BUSCA = "cargo"
TELEFONE = "telefone"

URL_LINK = "https://www.linkedin.com/login"
driver.get(URL_LINK)

input_email = driver.find_element(By.ID, "username")
input_email.send_keys(USUARIO)
input_password = driver.find_element(By.ID, "password")
input_password.send_keys(SENHA)
input_password.send_keys(Keys.ENTER)


URL_LINK = "https://www.linkedin.com/jobs/search/?currentJobId="\
    "2924526745&distance=25&f_AL=true&f_E=3&geoId=105104646&keywords"\
    "=python&location=S%C3%A3o%20Jos%C3%A9%20dos%20Campos%2C%20S%C3%A"\
    "3o%20Paulo%2C%20Brasil&sortBy=R"
driver.get(URL_LINK)

sleep(5)
button_applied = driver.find_element(
    By.CSS_SELECTOR, ".jobs-apply-button--top-card button")
button_applied.click()

sleep(2)
button_first_avancar = driver.find_element(
    By.XPATH, "/html/body/div[3]/div/div/div[2]/div/form/footer/"
    "div[2]/button")
button_first_avancar.click()

sleep(2)
input_telefone = driver.find_element(
    By.XPATH,
    '/html/body/div[3]/div/div/div[2]/div/form/div/div/div[2]/div[2]'
    '/div/div/input')

if input_telefone == "":
    input_telefone.send_keys(TELEFONE)

button_revisar = driver.find_element(
    By.XPATH,
    "/html/body/div[3]/div/div/div[2]/div/form/footer/div[2]/button[2]")
button_revisar.click()

sleep(2)
button_enviar = driver.find_element(
    By.XPATH,
    "/html/body/div[3]/div/div/div[2]/div/div[2]/footer/div[3]/button[2]")
button_enviar.click()


sleep(2)
button_sair = driver.find_element(
    By.XPATH,    "/html/body/div[3]/div/div/button")
button_sair.click()

sleep(5)
driver.quit()
driver.close()
