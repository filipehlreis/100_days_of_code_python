"""
- If the ISS is close to my current position
- and it is currently dark
- Then send me an email to tell me to look up.
- BONUS: run the code every 60 seconds.
"""

import time
import smtplib
import requests
from datetime import datetime

MY_LAT = 51.507351  # Your latitude -23.190590
MY_LONG = -0.127758  # Your longitude -45.875610


def is_iss_overhead():
    """ If the ISS is close to my current position"""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and \
            (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5):
        return True
    return False


def is_night():
    """ if it is currently dark"""
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        # Its dark
        return True
    return False


while True:
    time.sleep(60)  # tomar cuidado pois pode virar spam no email
    if is_iss_overhead() and is_night():
        """Then send me an email to tell me to look up."""
        my_email = "filipe1@gmail.com"
        password = "senha123"
        subject_msg = "Subject:Look to the Sky"
        to_addres_email = my_email

        content_msg = "The ISS is above you in the sky."

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=to_addres_email,
                                msg=f"{subject_msg}\n\n{content_msg}"
                                )
