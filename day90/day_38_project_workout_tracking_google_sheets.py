from datetime import datetime
import requests
import os
from pprint import pprint

NUTRITIONIX_API = os.environ['NUTRITIONIX_API']
NUTRITIONIX_ID = os.environ['NUTRITIONIX_ID']
NUTRITIONIX_Endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_TOKEN_BEARER = os.environ['SHEETY_TOKEN_BEARER']
SHEETY_Endpoint = os.environ['SHEETY_Endpoint']


GENDER = "male"
WEIGHT_KG = 68.6
HEIGHT_CM = 173.0
AGE = 29


headers_nutritionix = {
    "x-app-id": NUTRITIONIX_ID,
    "x-app-key": NUTRITIONIX_API,
}

headers_sheety = {
    "Authorization": SHEETY_TOKEN_BEARER
}


exercises = input("Tell me which exercises you did: ")
print()

parameters_nutritionix = {
    "query": exercises,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(
    url=NUTRITIONIX_Endpoint,
    json=parameters_nutritionix,
    headers=headers_nutritionix)

result = response.json()
pprint(result)


datenow = datetime.now()
date = datenow.strftime("%d/%m/%Y")
time = datenow.strftime("%H:%M:%S")

for exercise_item in result["exercises"]:
    exercise_name = exercise_item["name"].title()
    exercise_duration = exercise_item["duration_min"]
    exercise_calories = exercise_item["nf_calories"]

    print(
        exercise_name,
        exercise_duration,
        exercise_calories
    )

    parameters_sheety = {
        "workout": {
            "date": str(date),
            "time": str(time),
            "exercise": str(exercise_name),
            "duration": str(exercise_duration),
            "calories": str(exercise_calories),
        }
    }

    response = requests.post(
        url=SHEETY_Endpoint, json=parameters_sheety, headers=headers_sheety)
    result = response.json()
    print(result)
