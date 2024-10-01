import requests
from datetime import datetime

APP_ID = "b16cbfdc"
API_KEY = "38c6a6cc9e3e8f913597f4b4d81e08ba"
date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().time().strftime("%H:%M:%S")
GENDER = "Male"
WEIGHT_KG = 70
HEIGHT_CM = 179
AGE = 25

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
shitty_ENDPOINT = "https://api.sheety.co/ef79976f90df97b4fa7615f09cac5642/workout/sheet1"

params = {
    "query": input("Tell me which exercise you did?: "),
}
response1 = requests.post(url=exercise_endpoint, json=params, headers=headers)
result = response1.json()
print(result)

headers2 = {
    "Authorization": "Basic c2h1YmhhbTpzaHViaGFtd29ya291dA=="
}

duration = response1.json()["exercises"][0]["duration_min"]
calories = response1.json()["exercises"][0]["nf_calories"]
exercise = response1.json()["exercises"][0]["name"]

json = {
    'sheet1':

        {'date': date,
         'time': time,
         'exercise': exercise.title(),
         'duration': int(duration), 'calories': int(calories),
         }

}

response2 = requests.post(url=shitty_ENDPOINT, headers=headers2, json=json)
print(response2.status_code)
print(response2.text)
