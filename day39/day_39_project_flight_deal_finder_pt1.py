from data_manager import DataManager
from notification_manager import NotificationManager
from flight_search import FlightSearch

if __name__ == "__main__":
    sheety = DataManager()
    sheet_data = sheety.get_data_sheet()
    flight_search = FlightSearch()
    notification_manager = NotificationManager()

    for city_info in sheet_data:
        if not city_info['iataCode']:
            city_name = str(city_info["city"])
            city_info["iataCode"] = flight_search.get_iata_code(city_name)

            sheety.put_data_sheet(city_info["id"], city_info["iataCode"])

        flight = flight_search.search_flight(city_info["iataCode"])

        if flight:
            if flight.price < city_info["lowestPrice"]:
                message = f"Low price alert! Only £{flight.price} to fly "\
                    f"from {flight.origin_city}-{flight.origin_airport} to "\
                    f"{flight.destination_city}-{flight.destination_airport}"\
                    f", from {flight.out_date} to {flight.return_date}."
                notification_manager.send_sms_news(message)
