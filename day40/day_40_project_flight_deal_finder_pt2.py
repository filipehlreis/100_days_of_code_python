from data_manager import DataManager
from notification_manager import NotificationManager
from flight_search import FlightSearch

if __name__ == "__main__":
    sheety = DataManager()
    flight_search = FlightSearch()
    notification_manager = NotificationManager()

    sheet_data = sheety.get_data_sheet()

    print("\nWelcome to Filipe's Flight Club!")
    print("We find the best fligh deals and email you.")
    input_first_name = input("What is your first name?\n")
    input_last_name = input("What is your last name?\n")
    input_email = input("What is your email?\n")
    input_email_confirmation = input("Type your email again.\n")

    if input_email == input_email_confirmation:
        print("You're in the club!")
        sheety.put_data_sheet_name_club(
            input_first_name, input_last_name, input_email)

    for city_info in sheet_data:
        if not city_info['iataCode']:
            city_name = str(city_info["city"])
            city_info["iataCode"] = flight_search.get_iata_code(city_name)

            sheety.put_data_sheet_iataCode(
                city_info["id"], city_info["iataCode"])

        flight = flight_search.search_flight(city_info["iataCode"])

        if flight:
            if flight.price < city_info["lowestPrice"]:
                message_sms = f"Low price alert! Only £{flight.price} to fly "\
                    f"from {flight.origin_city}-{flight.origin_airport} to "\
                    f"{flight.destination_city}-{flight.destination_airport}"\
                    f", from {flight.out_date} to {flight.return_date}."
                notification_manager.send_sms_news(message_sms)

                users = sheety.get_customer_emails()
                emails = [row["email"] for row in users]
                names = [row["firstName"] for row in users]

                message_email = \
                    f"Low price alert! Only £{flight.price} to fly from "\
                    f"{flight.origin_city}-{flight.origin_airport} to "\
                    f"{flight.destination_city}-{flight.destination_airport},"\
                    f" from {flight.out_date} to {flight.return_date}."

                if flight.stop_overs > 0:
                    message_email += \
                        f"\nFlight has {flight.stop_overs} stop over, via "\
                        f"{flight.via_city}."

                link = \
                    f"https://www.google.co.uk/flights?hl=en#flt="\
                    f"{flight.origin_airport}.{flight.destination_airport}."\
                    f"{flight.out_date}*{flight.destination_airport}."\
                    f"{flight.origin_airport}.{flight.return_date}"

                notification_manager.send_emails(emails, message_email, link)
