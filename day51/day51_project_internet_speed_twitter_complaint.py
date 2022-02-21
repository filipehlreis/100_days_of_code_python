from internetspeedtwitterbot import InternetSpeedTwitterBot


if __name__ == "__main__":
    PROMISED_DOWN = 200
    PROMISED_UP = 100

    istb = InternetSpeedTwitterBot(PROMISED_DOWN, PROMISED_UP)

    istb.get_internet_speed()
    istb.tweet_at_provider()

    # driver.close()
