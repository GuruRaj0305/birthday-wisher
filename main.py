import datetime as dt
import random
import smtplib
import pandas

my_id = "gururajhr0305l@gmail.com"
my_password = "jkmakcpvcrpckyog"

now = dt.datetime.now()
today_mandy =(now.month,now.day)

data = pandas.read_csv("birthdays.csv")
data_dict = {(data_row["month"],data_row["day"]): data_row for (index,data_row) in data.iterrows()}

if today_mandy in data_dict:
    birthday_person = data_dict[today_mandy]
    filepath = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(filepath) as letter_file:
        contents = letter_file.read()

        contents = contents.replace("[NAME]",birthday_person["name"])


    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_id,my_password)
        connection.sendmail(
            from_addr=my_id,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!...\n\n{contents}")





