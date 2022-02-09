from typing import Dict
import requests
import os


class DataManager:
    def __init__(self) -> None:
        self.SHEETY_TOKEN_BEARER_FLIGHT = \
            os.environ['SHEETY_TOKEN_BEARER_FLIGHT']
        self.SHEETY_FLIGHT_Endpoint = os.environ['SHEETY_FLIGHT_Endpoint']
        self.headers_sheety = {
            "Authorization": self.SHEETY_TOKEN_BEARER_FLIGHT
        }

    def get_data_sheet(self) -> Dict:
        response = requests.get(
            url=self.SHEETY_FLIGHT_Endpoint, headers=self.headers_sheety)
        data_sheet = response.json()

        return data_sheet["prices"]

    def put_data_sheet(self, id, iataCode):
        parameters_sheety = {
            "price": {
                "iataCode": iataCode,
            }
        }
        response = requests.put(
            url=f"{self.SHEETY_FLIGHT_Endpoint}/{id}",
            json=parameters_sheety,
            headers=self.headers_sheety)

        response.raise_for_status()
