import smtplib
import requests
from bs4 import BeautifulSoup

URL_PRODUCT = "https://www.amazon.com.br/dp/B084BNVRFQ"

headers_list = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 "
    "Safari/537.36 OPR/83.0.4254.27",

    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"
}

response = requests.get(URL_PRODUCT, headers=headers_list)
response.raise_for_status()

data = response.text
soup = BeautifulSoup(data, "html.parser")

title_product = soup.find(id="productTitle").get_text().strip()

prices_whole = soup.find(class_="a-price-whole").get_text()
prices_fraction = soup.find(class_="a-price-fraction").get_text()
price_product = float(str(prices_whole+prices_fraction).replace(',', '.'))


if price_product < 8:
    my_email = "filipe1@gmail.com"
    password = "senha123"
    to_addres_email = my_email

    subject_msg = "Alerta de Preço Amazon!!!📣📣📣"
    content_msg = f"Corre! O produto '{title_product}' está baratinho!\n"\
        f"Neste momento está por R${price_product}.\n\nSegue o link para"\
        f" comprar logo:\n{URL_PRODUCT}"

    print(f"{subject_msg}\n\n{content_msg}")

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_addres_email,
                            msg=f"{subject_msg}\n\n{content_msg}"
                            )
