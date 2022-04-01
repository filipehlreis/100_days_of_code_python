from typing import Any, Dict
from twilio.rest import Client
import requests
import os

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
lat = -23.223701
lon = -45.900906

chave_weather = os.environ['chave_weather']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
account_sid = os.environ['TWILIO_ACCOUNT_SID']
my_phone_number_twilio = os.environ['my_phone_number_twilio']
my_real_phone = os.environ['my_real_phone']


weather_parameters: Dict[str, Any] = {
    "lat": lat,
    "lon": lon,
    "exclude": "current,minutely,daily",
    "appid": chave_weather,
}


response = requests.get(OWM_Endpoint, params=weather_parameters)
wheather_data = response.json()
weather_slice = wheather_data["hourly"][:12]


""" Teacher solution """
will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True


# """ My solution """
# condition_code = [
#     weather_slice[indice]["weather"][0]["id"]
#     for indice in range(12)
# ]
# bring_umbrela = [
#     "Bring an umbrella." for condition in condition_code if condition < 700
# ]

# if "Bring an umbrella." in bring_umbrela:
#     print("It's going to rain, bring an umbrella.")
# # --------------------------------------------------


if will_rain:
    client = Client(account_sid, auth_token)

    body_message = "It's going to rain today. Remember to bring an Umbrella!"
    message = client.messages \
                    .create(
                        body=body_message,
                        from_=my_phone_number_twilio,
                        to=my_real_phone
                    )

    print(message.status)
