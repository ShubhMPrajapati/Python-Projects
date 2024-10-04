import smtplib
import ssl
import requests
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

# User credentials
user = "your_email@example.com"  # Your email address
password = "your_email_password"  # Your email account password or app-specific password

# Setting up travel dates
current_date = datetime.now().date() + timedelta(days=1)
return_date = current_date + timedelta(days=10)

dates = []
for i in range(1, 191):
    current_date = datetime.now().date() + timedelta(days=i)
    dates.append(current_date.strftime("%Y-%m-%d"))

print(dates)

# API header and endpoint setup
shitty_header = {"Authorization": "Basic your_base64_encoded_credentials"}  # Use Base64 encoding for API credentials
sheety_api = "https://api.sheety.co/your_api_key/flightdeals/sheet1"  # Your Sheety API endpoint

# Get flight deals data from Sheety
sheety_call = requests.get(sheety_api, headers=shitty_header)
sheety_data = sheety_call.json()
print(sheety_data)

# API endpoint for OAuth2 token
FLIGHT_END_POINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
client_id = "your_client_id"  # Your Amadeus API client ID
client_secret = "your_client_secret"  # Your Amadeus API client secret

# API endpoint for getting an OAuth2 token
url = FLIGHT_END_POINT

# Headers and data for token request
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret
}

response = requests.post(url=url, data=data)
response_data = response.json()

new_flight_api = "https://test.api.amadeus.com/v1/reference-data/locations/cities"

new_authorization_header = {
    "Authorization": f"Bearer {response_data['access_token']}",  # Use the token retrieved from the previous call
}

count = 2

for city in sheety_data['sheet1']:
    IATA_params = {
        "keyword": city['city']
    }

    call = requests.get(url=new_flight_api, headers=new_authorization_header, params=IATA_params)
    iata_data = call.json()['data'][0]['iataCode']

    for date in dates:
        date_obj = datetime.strptime(date, "%Y-%m-%d").date()
        return_date = (date_obj + timedelta(days=10)).strftime("%Y-%m-%d")

        new_params = {
            "originLocationCode": "LON",  # Change this to your origin IATA code
            "destinationLocationCode": iata_data,
            "departureDate": date,
            "adults": 1,
            "returnDate": return_date,
            "currencyCode": "GBP"  # Change the currency code as needed
        }

        FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"

        call = requests.get(url=FLIGHT_ENDPOINT, headers=new_authorization_header, params=new_params)
        data = call.json()

        # Ensure data is available before accessing it
        if data and "data" in data and len(data["data"]) > 0:
            data1 = float(data["data"][0]["travelerPricings"][0]["price"]["total"])
            print(f"Getting flight for {city['city']} from {date} to {return_date}\nand the price is {data1}")

            if data1 < city["lowestPrice"]:
                content = f"Flight for {city['city']} from {date} to {return_date}\nand the price is {data1}"
                try:
                    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                        connection.starttls(context=ssl.create_default_context())
                        connection.login(user, password)
                        connection.sendmail(
                            user,
                            "recipient@example.com",  # Replace with your recipient's email address
                            msg=f"Subject: Cheap Deal Found to {city['city']}\n\n{content}"
                        )
                        print(f"Email sent successfully!\nand the message was {content}")
                except smtplib.SMTPServerDisconnected as e:
                    print(f"Failed to connect to the server: {e}")
                except smtplib.SMTPAuthenticationError as e:
                    print(f"Authentication error: {e}")
                except Exception as e:
                    print(f"An error occurred: {e}")
        else:
            print("No flight data available.")
