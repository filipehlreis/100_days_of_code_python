"""
# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day
# before yesterday then print("Get News").

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for
# the COMPANY_NAME.

# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title
# and description to your phone number.

"""


# ------------------------------ IMPORTS -------------------------------------
from typing import Dict
from twilio.rest import Client
import datetime as dt
import requests
import os

# ------------------------------ Constantes ----------------------------------
STOCK = "TSLA"
COMPANY_NAME = "Tesla"


# ------------------------------ Keys ----------------------------------------
key_alphavantage = os.environ['ALPHAVANTAGE']
key_newsapi = os.environ['NEWSAPI']
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
my_phone_number_twilio = os.environ['my_phone_number_twilio']
my_real_phone = os.environ['my_real_phone']


# ------------------------------ Functions -----------------------------------


def get_data_stock(symbol: str) -> Dict:
    ALPHAVANTAGE_Endpoint = "https://www.alphavantage.co/query"

    parameters_stock = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": key_alphavantage,
    }

    response = requests.get(ALPHAVANTAGE_Endpoint, params=parameters_stock)
    response.raise_for_status()
    data_stock_daily = response.json()["Time Series (Daily)"]

    return data_stock_daily


def get_data_news(company: str, datenow) -> Dict:
    NEWSAPI_Endpoint = "https://newsapi.org/v2/everything"

    parameters_newsapi = {
        "qInTitle": company,
        "from": str(datenow.date),
        "sortBy": "popularity",
        "apiKey": key_newsapi,
    }

    response = requests.get(NEWSAPI_Endpoint, params=parameters_newsapi)
    response.raise_for_status()
    data_news_articles = response.json()["articles"]
    return data_news_articles


def send_sms_news(data_news: Dict, percentage: float, qtd_news: int) -> None:
    client = Client(account_sid, auth_token)

    if percentage > 0:
        increased_emoji = "🔺"
    else:
        increased_emoji = "🔻"

    # It's seems to be better use list slice instead.

    for indice in range(qtd_news):
        body_message = f"{STOCK}: {increased_emoji} {percentage}%\
        \nHeadline: {data_news[indice]['title']}\
        \nBrief: {data_news[indice]['description']}\n"

        message = client.messages \
                        .create(
                            body=body_message,
                            from_=my_phone_number_twilio,
                            to=my_real_phone
                        )

        print(body_message)
        print(message.status)


def get_percentage_price_stock(data_stock: Dict, datenow) -> float:
    # Its possible to simplify the code by using List comprehension instead
    # of using timedelta().

    day_week_now = datenow.weekday()

    if day_week_now == 6:
        pass
    elif day_week_now == 0:
        day_now_stock = datenow - dt.timedelta(3)
        day_now_stock_previous = datenow - dt.timedelta(4)
    elif day_week_now == 1:
        day_now_stock = datenow - dt.timedelta(1)
        day_now_stock_previous = datenow - dt.timedelta(4)
    else:
        day_now_stock = datenow - dt.timedelta(1)
        day_now_stock_previous = datenow - dt.timedelta(2)

    price_close = float(data_stock[str(day_now_stock.date())]["4. close"])
    price_close_previous = float(
        data_stock[str(day_now_stock_previous.date())]["4. close"])

    if price_close >= price_close_previous:
        percentage = round((price_close/price_close_previous - 1) * 100, 2)
    else:
        percentage = - round((1 - price_close/price_close_previous) * 100, 2)

    return percentage


def main():
    datenow = dt.datetime.now()

    data_stock = get_data_stock(STOCK)
    data_news = get_data_news(COMPANY_NAME, datenow)
    percentage = get_percentage_price_stock(data_stock, datenow)

    if abs(percentage) >= 3:
        send_sms_news(data_news, percentage, 3)


if __name__ == "__main__":
    main()
