# # smtplib.SMTP("smtp.gmail.com", port=587)


# import smtplib


# my_email = "frix.henriquejogo@gmail.com"
# password = "&S2$j0TGL9yjv=^F"


# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="filipe.henrique.reis@gmail.com",
#                         msg="Subject:Hello\n\nThis is the body of my email."
#                         )


import smtplib
import random
import datetime as dt

now = dt.datetime.now()
# year = now.year
# print(now)
# print(year)
# month = now.month
# date_of_birth = dt.datetime(year=1992, month=11, day=12, hour=4)
# print(date_of_birth)

day_of_week = now.weekday()


with open(file="day32\\quotes.txt", mode="r") as quotes:
    quotes_list = quotes.readlines()


if day_of_week == 1:
    my_email = "frix.henriquejogo@gmail.com"
    password = "&S2$j0TGL9yjv=^F"
    to_addres_email = "filipe.henrique.reis@gmail.com"
    subject_msg = "Subject:Tuesday Quotes"
    contend_msg = random.choice(quotes_list)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_addres_email,
                            msg=f"{subject_msg}\n\n{contend_msg}"
                            )
