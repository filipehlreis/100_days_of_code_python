from datetime import datetime, timedelta
import os
from flight_data import FlightData
import requests


class FlightSearch:
    def __init__(self) -> None:
        self.city = ''
        self.TEQUILA_Endpoint = "https://tequila-api.kiwi.com"
        self.TEQUILA_SEARCH_Endpoint = f"{self.TEQUILA_Endpoint}/v2/search"
        self.TEQUILA_Location_Query_Endpoint = \
            f"{self.TEQUILA_Endpoint}/locations/query"
        self.TEQUILA_Key = os.environ['TEQUILA_Key']
        self.headers_tequila = {
            "apikey": self.TEQUILA_Key,
        }
        # self.home = "GRU"
        self.home = "LON"  # only for testing purpose

    def get_iata_code(self, city: str) -> str:
        parameters_query = {
            "term": city,
        }
        response = requests.get(
            url=self.TEQUILA_Location_Query_Endpoint,
            params=parameters_query,
            headers=self.headers_tequila)
        data_sheet = response.json()

        return data_sheet["locations"][0]["code"]

    def search_flight(self, destination_code):
        today = datetime.now()
        date_from = today + timedelta(1)
        date_to = today + timedelta(6*30)

        parameters_search = {
            "fly_from": self.home,
            "fly_to": destination_code,
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "one_for_city": 1,
            "max_stopovers": 0,
            "flight_type": "round",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "GBP",
        }
        response = requests.get(
            url=self.TEQUILA_SEARCH_Endpoint,
            params=parameters_search,
            headers=self.headers_tequila)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(
            f'Origem: {flight_data.origin_city} - '
            f'Destino: {flight_data.destination_city} - '
            f'Preço: £{flight_data.price}.'
        )
        return flight_data
