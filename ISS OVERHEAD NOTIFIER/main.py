import datetime

import requests
import smtplib
import ssl
import time

LAT = 51.507351
LONG = -0.127758
my_location = (LAT, LONG)
params = {'lat': LAT,
          'lng': LONG,
          'formatted': 0
          }
USER = "YOUR GMAIL ADREESS"
PASSWORD = "YOUR APP PROVIDER PASSWORD"
TO_ADDRESS = "receiver email address"


def is_overhead():
    response1 = requests.get(" http://api.open-notify.org/iss-now.json")
    response1.raise_for_status()
    longitude = float(response1.json()['iss_position']['longitude'])
    latitude = float(response1.json()['iss_position']['latitude'])
    if LAT-5 <= latitude <= LAT+5 and LONG-5 <= longitude <= LONG+5:
        return True


def is_dark():
    response = requests.get(f" https://api.sunrise-sunset.org/json", params=params)
    response.raise_for_status()
    sunrise = int(response.json()["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(response.json()["results"]["sunset"].split("T")[1].split(":")[0])
    hour = datetime.datetime.now().hour
    if sunset <= hour <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_overhead() and is_dark():

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls(context=ssl.create_default_context())
                connection.login(USER, PASSWORD)
                connection.sendmail(USER,
                                    TO_ADDRESS,
                                    msg=f"Subject:Happy Birthday\n\nIts at your place")
                print(f"Email sent successfully!\nand the message was Its at your place")
        except Exception as e:
            print(f"An error occurred: {e}")
