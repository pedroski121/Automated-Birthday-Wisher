

import pandas as pd
import datetime as dt
import random
import smtplib

MY_EMAIL = "obipedrochinomso@gmail.com"
MY_PASSWORD = 'pedroski121'


def send_message(receiver_mail, message):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=receiver_mail, msg=message)
        print('message sent')


now = dt.datetime.now()
this_month = int(now.strftime('%m'))
this_day = int(now.strftime("%d"))


def read_change_letter(user_name):
    with open(f'letter_templates/letter_{random_numbers}.txt', 'r') as letter:
        the_letter = letter.read()
        return the_letter.replace(
            '[NAME]', user_name).replace('Angela', 'Pedro')


df_birthday = pd.read_csv('birthdays.csv')
df_birthday.set_index("name", drop=True, inplace=True)
df_birthdays = df_birthday.to_dict(orient="index")
for (name, details) in df_birthdays.items():
    birthday_month = int(details["month"])
    birthday_day = int(details["day"])
    email = details['email']
    if this_month == birthday_month and this_day == birthday_day:
        random_numbers = random.randint(1, 3)
        your_letter = read_change_letter(user_name=name)
        send_message(receiver_mail=email,
                     message=f'Subject:Happy Birthday\n\n{your_letter}')
