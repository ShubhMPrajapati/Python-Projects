##################### Normal Starting Project ######################
import random
from datetime import datetime
import pandas as pd
import smtplib
import ssl
user = "shubham90Days@gmail.com"
password = "qmjn xpgf gabh awun"

today = (datetime.now().day,datetime.now().month )

# HINT 2: Use pandas to read the birthdays.csv
data = pd.read_csv("birthdays.csv")

#Dictionary comprehension templates for pandas DataFrame looks like this:
birthdays_dict = {(data_row.month, data_row.day):data_row for (index, data_row) in data.iterrows()}

#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
if today in birthdays_dict:
    name = birthdays_dict[today]["name"]
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as file:
      letter = file.read()
      content = letter.replace("[NAME]", name)

    try:
        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls(context=ssl.create_default_context())
            connection.login(user, password)
            connection.sendmail(user,
                                birthdays_dict[today]["email"],
                                msg=f"Subject:Happy Birthday\n\n{content}")
            print(f"Email sent successfully!\nand the message was {content}")

    except smtplib.SMTPServerDisconnected as e:
            print(f"Failed to connect to the server: {e}")
    except smtplib.SMTPAuthenticationError as e:
        print(f"Authentication error: {e}")
    except Exception as e:
            print(f"An error occurred: {e}")

