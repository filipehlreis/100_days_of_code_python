from datetime import datetime
import requests
import os

PIXELA_Endpoint = "https://pixe.la/v1/users"
USERNAME = "filipehenriquereis"
GRAPH_ID = "graph1"
TOKEN_PIXELA = os.environ['TOKEN_PIXELA']

today = datetime.now()
today_formatted = today.strftime('%Y%m%d')

GRAPH_Endpoint = f"{PIXELA_Endpoint}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN_PIXELA
}


def formatted_date():
    today = datetime.now()
    formatted = today.strftime("%Y%m%d")
    return formatted


def create_user_pixela():
    user_parameters = {
        "token": TOKEN_PIXELA,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }

    response = requests.post(url=PIXELA_Endpoint, json=user_parameters)
    print(response.text)


def create_graph():
    global headers, GRAPH_Endpoint
    graph_config = {
        "id": GRAPH_ID,
        "name": "Cycling Graph",
        "unit": "Km",
        "type": "float",
        "color": "sora",
    }

    response = requests.post(
        url=GRAPH_Endpoint, json=graph_config, headers=headers)
    print(response.text)


def create_pixel():
    global headers, GRAPH_Endpoint

    date_formatted = input(
        "What date do you want to create? 'yyyyMMdd': ")
    quantity_km = input("How many kilometers did you ride? '0.0': ")

    if date_formatted == '0':
        date_formatted = formatted_date()

    PIXEL_Creation_Endpoint = f"{GRAPH_Endpoint}/{GRAPH_ID}"

    pixel_data = {
        "date": date_formatted,
        "quantity": quantity_km,
    }

    response = requests.post(
        url=PIXEL_Creation_Endpoint,
        json=pixel_data,
        headers=headers)
    print(response.text)


def update_pixel():
    global headers, GRAPH_Endpoint

    date_formatted = input("What date do you want to update? 'yyyyMMdd': ")
    quantity_km = input("How many kilometers did you ride? '0.0': ")

    if date_formatted == '0':
        date_formatted = formatted_date()

    PIXEL_Update_Endpoint = f"{GRAPH_Endpoint}/{GRAPH_ID}/{date_formatted}"
    new_pixel_data = {
        "quantity": quantity_km
    }

    response = requests.put(url=PIXEL_Update_Endpoint,
                            json=new_pixel_data, headers=headers)
    print(response.text)


def delete_pixel():
    global headers, GRAPH_Endpoint
    date_formatted = input("What date do you want to delete? 'yyyyMMdd': ")

    if date_formatted == '0':
        date_formatted = formatted_date()

    PIXEL_Delete_Endpoint = f"{GRAPH_Endpoint}/{GRAPH_ID}/{date_formatted}"
    response = requests.delete(url=PIXEL_Delete_Endpoint, headers=headers)
    print(response.text)


if __name__ == "__main__":

    while True:
        choice = input(
            "\nMENU - Cycling Graph:\
            \n1 - Add a pixel.\
            \n2 - Update a pixel.\
            \n3 - Delete a pixel.\
            \n0 - Exit.\
            \n\nWhat do you want to do? ")

        if choice == '1':
            create_pixel()
        elif choice == '2':
            update_pixel()
        elif choice == '3':
            delete_pixel()
        else:
            break
