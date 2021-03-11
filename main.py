import datetime as dt
import smtplib
import pandas as pd
import random
data = pd.read_csv("birthdays.csv")
dictionar = data.to_dict()
time = dt.datetime.now()
month = time.month
day = time.day
MAIL = "email"
PASS = "password"

for i in range(len(data)):
    if dictionar["month"][i] == month and dictionar["day"][i] == day:
        adress = dictionar["email"][i]
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as fl:
            content = fl.read()
        content = content.replace("[NAME]", dictionar["name"][i])
        with smtplib.SMTP("smtp.gmail.com") as conect:
            conect.starttls()
            conect.login(MAIL, PASS)
            conect.sendmail(from_addr=MAIL, to_addrs=adress, msg=f"Subject:Happy Birthday!\n\n{content}")



