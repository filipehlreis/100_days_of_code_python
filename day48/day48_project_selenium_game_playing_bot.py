from pprint import pprint
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

# URL_PRODUCT = "https://www.amazon.com.br/dp/B084BNVRFQ"
# URL_PRODUCT = "https://www.amazon.com.br/dp/B084BNWNWC"
# URL_PRODUCT = "https://www.amazon.com.br/BAW-WAW-AREIA-SANIT%C3%81RIA
# -GATOS/dp/B084BNWNWC/ref=pd_bxgy_img_2/131-6021336-0818824?pd_rd_w=
# ReSjV&pf_rd_p=f6d6e5b8-8da7-4a7b-8303-08e67f79afcf&pf_rd_r=
# JAAFYPG40749VVDY6621&pd_rd_r=095de7aa-fbe6-4600-a61c-1be84a894393&pd_rd_wg=
# xmOko&pd_rd_i=B084BNWNWC&psc=1"

URL_PRODUCT = "https://www.python.org"


chrome_driver_path =\
    "C:\\github\\100_days_of_code_python\\day48\\chromedriver.exe"

ser = Service(chrome_driver_path)
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)


driver.get(URL_PRODUCT)


# ########################
# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribte("placeholder"))
# ########################
# logo = driver.find_element_by_class_name("python-logo")
# ########################
# documentation_link = driver.find_element_by_css_selector(
#     ".documentarion-widget a")
# print(documentation_link.text)
# ########################
# bug_link = driver.find_element_by_xpath('//*[@id="tabs--1-tab-7"]/span')
# print(bug_link.text)
# ########################

# ################ amazon price alert ##########################
# prices_whole = driver.find_element(By.CLASS_NAME, "a-price-whole")
# prices_fraction = driver.find_element(By.CLASS_NAME, "a-price-fraction")

# price_product = float(str(prices_whole.text+"."+prices_fraction.text))
# # print(prices_whole.text)
# # print(prices_fraction.text)
# print(f"R${price_product}")
# ################ amazon price alert ##########################


upcoming_events_elements = driver.find_elements(
    By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul')

upcoming_events = []
for upcoming_event_element in upcoming_events_elements:
    texto = upcoming_event_element.text
    upcoming_events.append(texto)

upcoming_events_splited = upcoming_events[0].split('\n')

upcoming_events_dict = {
    i: {
        "time": upcoming_events_splited[2*i],
        "name": upcoming_events_splited[2*i+1]
    }
    for i in range(int(len(upcoming_events_splited)/2))
}

pprint(upcoming_events_dict)

# driver.close()
# driver.quit()
