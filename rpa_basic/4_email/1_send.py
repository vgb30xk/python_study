import smtplib
from account import *

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()