import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = "TYPE YOUR UNIQUE TOKEN WHICH IS MORE THAN 8 CHARACTERS LONG AND WITH NO SPACE"
USERNAME = "TYPE YOUR UNIQUE USERNAME HERE"

# Run the api requests one by and, don't forget to comment out the previous request before running the next api request

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# api = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(api.text)

GRAPH_END_POINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
GRAPH_ID = "graph1"
graph_params = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai",

}

headers = {
    "X-USER-TOKEN": TOKEN
}

# graph_api = requests.post(url=GRAPH_END_POINT, json=graph_params, headers=headers)
# print(graph_api.text)


POST_PIXEL_END_POINT = f"{GRAPH_END_POINT}/{GRAPH_ID}"

DAY = datetime(year=2024, month=9, day=30).strftime("%Y%m%d")
# DAY = datetime.now().strftime("%Y%m%d")

post_pixel_params = {
    'date': DAY,
    "quantity": '15.5'
}
# post_pixel_api = requests.post(url=POST_PIXEL_END_POINT,json=post_pixel_params, headers=headers)
# print(post_pixel_api.text)


UPDATE_PIXEL_ENDPOINT = f"{POST_PIXEL_END_POINT}/{DAY}"
update_pixel_params = {
    "quantity": "20.8"
}

# update_pixel_api = requests.put(url=UPDATE_PIXEL_ENDPOINT, json=update_pixel_params, headers=headers)
# print(update_pixel_api.text)

DELETE_PIXEL_ENDPOINT = f"{POST_PIXEL_END_POINT}/{DAY}"

# delete_pixel_api = requests.delete(url=DELETE_PIXEL_ENDPOINT, headers=headers)
# print(delete_pixel_api.text)
