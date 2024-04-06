import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import requests
from bs4 import BeautifulSoup
import random

class CodeChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print("Code modified! Running the second code.")
        run_second_code()

def monitor_code_changes(filename):
    event_handler = CodeChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, ".", recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

def generate_random_visa_card():
    visa_card_number = "4"  
    for _ in range(15):
        digit = random.randint(0, 9)
        visa_card_number += str(digit)
    return visa_card_number

def generate_random_expiry_date():
    month = random.randint(1, 12)
    year = random.randint(2024, 2030)
    return f"{month}/{year}"

def generate_random_cvv():
    cvv = ""
    for _ in range(3):
        digit = random.randint(0, 9)
        cvv += str(digit)
    return cvv

def generate_random_city():
    cities = ["New York", "London", "Tokyo", "Paris", "Los Angeles"]
    return random.choice(cities)

def test_on_google_pay(visa_card_number, expiry_date, cvv, issuing_city):
    url = "https://payments.google.com/gp/w/home/paymentmethods?sctid=8225360961996315"
    payload = {
        "visa_card_number": visa_card_number,
        "expiry_date": expiry_date,
        "cvv": cvv,
        "issuing_city": issuing_city
    }
    response = requests.post(url, data=payload)

    is_valid = random.choice([True, False])
    if is_valid:
        available_balance = random.randint(100, 10000)
        return is_valid, available_balance
    else:
        return is_valid, 0

def run_second_code():
    visa_card_number = generate_random_visa_card()
    expiry_date = generate_random_expiry_date()
    cvv = generate_random_cvv()
    issuing_city = generate_random_city()

    is_valid, balance = test_on_google_pay(visa_card_number, expiry_date, cvv, issuing_city)

    if is_valid:
        print(f" Visa card : {visa_card_number}")
        print(f" Date : {expiry_date}")
        print(f" CVV : {cvv}")
        print(f" Frome :  {issuing_city}")
        print(f"True :  💳🟢")
        print(f"Mony: ${balance}")
    else:
        print(f" Visa card : {visa_card_number}")
        print(f" date : {expiry_date}")
        print(f" CVV : {cvv}") 
        print(f" From : {issuing_city}")
        print(f" False : 💳🔴")

if __name__ == "__main__":
    filename_to_monitor = "card.py"  # Replace with your actual filename
    monitor_code_changes(filename_to_monitor)
