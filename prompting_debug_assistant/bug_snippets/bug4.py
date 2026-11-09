import json
from datetime import datetime


def load_config(raw):
    return json.loads(raw)


def total_price(prices):
    total = 0
    for p in prices:
        total += p
    return total


config = load_config({"currency": "AZN", "tax": 0.18})
print("Currency:", config["currency"])

prices = ["10.5", "20", "5.25"]
print("Total:", total_price(prices))

age = input("Enter your age: ")
if age > 18:
    print("Adult")

deadline = datetime.strptime("2026-11-09", "%d/%m/%Y")
print("Deadline:", deadline)
