from typing import Dict
import requests
import os


class DataManager:
    def __init__(self) -> None:
        self.SHEETY_TOKEN_BEARER_FLIGHT = \
            os.environ['SHEETY_TOKEN_BEARER_FLIGHT']
        self.SHEETY_FLIGHT_Endpoint = os.environ['SHEETY_FLIGHT_Endpoint']
        self.SHEETY_FLIGHT_USERS_Endpoint = \
            os.environ['SHEETY_FLIGHT_USERS_Endpoint']
        self.headers_sheety = {
            "Authorization": self.SHEETY_TOKEN_BEARER_FLIGHT
        }

    def get_data_sheet(self) -> Dict:
        response = requests.get(
            url=self.SHEETY_FLIGHT_Endpoint, headers=self.headers_sheety)
        data_sheet = response.json()

        return data_sheet["prices"]

    def get_data_sheet_name_club(self) -> Dict:
        response = requests.get(
            url=self.SHEETY_FLIGHT_USERS_Endpoint, headers=self.headers_sheety)
        data_sheet = response.json()

        return data_sheet["users"]

    def put_data_sheet_iataCode(self, id, iataCode):
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

    def put_data_sheet_name_club(self, first_name, last_name, email):
        parameters_sheety = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
            }
        }
        response = requests.post(
            url=f"{self.SHEETY_FLIGHT_USERS_Endpoint}",
            json=parameters_sheety,
            headers=self.headers_sheety)

        response.raise_for_status()

    def get_customer_emails(self):
        customers_endpoint = self.SHEETY_FLIGHT_USERS_Endpoint
        response = requests.get(
            customers_endpoint, headers=self.headers_sheety)
        data = response.json()
        print(data)
        self.customer_data = data["users"]
        return self.customer_data
