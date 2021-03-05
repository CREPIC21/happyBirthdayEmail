import pandas
import datetime
import random
import smtplib
import os

# Getting the today's date and current month
now = datetime.datetime.now()
month = now.month
day = now.day

print(day, month)

# Reading and extracting data from cvs file
birthdays = pandas.read_csv("birthdays.csv")
list_of_months = birthdays["month"].to_list()
list_of_days = birthdays["day"].to_list()
list_of_names = birthdays["name"].to_list()
list_of_emails = birthdays["email"].to_list()
print(list_of_days)
print(list_of_months)

index_number = None
# Checking if current date and month is in the data from csv file
if day in list_of_days and month in list_of_months:
    if list_of_days.index(day) == list_of_months.index(month):
        index_number = list_of_days.index(day)

        letters = []
        # Chosing a random letter template and filling it up with csv data
        for i in range(1, 4):
            with open(f"./letter_templates/letter_{i}.txt") as file:
                letter = file.readlines()
                letters.append(letter)
        random_letter = "".join(random.choice(letters)).replace("[NAME]", list_of_names[list_of_days.index(day)])
        print(random_letter)

        # Sending a Happy Birthday email to a person if the date is in the birthday.csv file
        my_email = os.environ['MY_EMAIL']
        my_password = os.environ['EMAIL_PASSWORD']
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=list_of_emails[index_number],
                                msg=f"Subject:Happy Bday\n\n{random_letter}")
else:
    print("No birthdays today!!!")



