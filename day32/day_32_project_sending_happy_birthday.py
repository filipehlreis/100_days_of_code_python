import random
import datetime as dt
import pandas
import smtplib

letter_templates = []
with open(file="day32\\letter_templates\\letter_1.txt", mode="r") as letter:
    letter_templates.append(letter.read())
with open(file="day32\\letter_templates\\letter_2.txt", mode="r") as letter:
    letter_templates.append(letter.read())
with open(file="day32\\letter_templates\\letter_3.txt", mode="r") as letter:
    letter_templates.append(letter.read())

birthday = pandas.read_csv("day32\\birthdays.csv")
birthday_dict = birthday.to_dict(orient="records")

my_email = "filipe1@gmail.com"
password = "senha123"
subject_msg = "Subject:Happy Birthday"

now = dt.datetime.now()
month = now.month
day = now.day

for birthday in birthday_dict:
    if birthday["month"] == month and birthday["day"] == day:
        to_addres_email = birthday["email"]

        content_msg: str = random.choice(letter_templates)
        content_msg = content_msg.replace("[NAME]", birthday["name"])

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=to_addres_email,
                                msg=f"{subject_msg}\n\n{content_msg}"
                                )
