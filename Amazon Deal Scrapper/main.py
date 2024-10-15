import time
from bs4 import BeautifulSoup
import requests
import smtplib
import ssl

# Replace with your email
user = "your_email@example.com"

# Replace with your app password or email password (if using SMTP)
password = "your_app_password_here"

# Amazon product link
link = "https://www.amazon.ca/LG-24MP60G-B-Full-Monitor-FreeSync/dp/B093R6C6B4/?_encoding=UTF8&ref_=pd_hp_d_atf_dealz_cs"

# Headers for the web request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-GB,en;q=0.9"
}

# Send a request to the product page
response = requests.get(link, headers=headers)

# Parse the page content
soup = BeautifulSoup(response.content, 'html.parser')

# Extract product title and price
title = soup.select(selector="#productTitle")
price_decimal = soup.select(selector=".a-price-whole")

# Print the product price (incremented by 1 for testing)
print(int((price_decimal[0].text).strip("."))+1)

# Uncomment the below code to enable the monitoring loop
# and email alert when the price drops below a certain threshold.

# is_on = True
# while is_on:
#     response = requests.get(link, headers=headers)
#
#     soup = BeautifulSoup(response.content, 'html.parser')
#
#     price_whole = soup.select(selector=".a-price-whole")
#     price_decimal = soup.select(selector=".a-price-fraction")
#     number = float(f"{price_whole[0].getText()}{price_decimal[0].getText()}")
#     product_title = soup.select("#productTitle")[0].getText().strip()
#     print(number)
#
#     if number < 100:
#         content = f"{product_title} is now at ${number}, Link:- {link}"
#         try:
#             with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#                 connection.starttls(context=ssl.create_default_context())
#                 connection.login(user, password)
#                 connection.sendmail(
#                     user,
#                     "recipient_email@example.com",  # Replace with recipient's email
#                     msg=f"Subject:Cheap Deal Found\n\n{content}".encode('utf-8')  # Ensuring utf-8 encoding
#                 )
#                 print(f"Email sent successfully!\nand the message was {content}")
#                 time.sleep(30)
#         except smtplib.SMTPServerDisconnected as e:
#             print(f"Failed to connect to the server: {e}")
#         except smtplib.SMTPAuthenticationError as e:
#             print(f"Authentication error: {e}")
#         except Exception as e:
#             print(f"An error occurred: {e}")
#     time.sleep(30)
