# This code won't compile, you need an API key from apilayer.com at line 14
import requests


class SimpleCurrencyConverter:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def convert(self, destination):
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={destination}&from={self.currency}&amount={self.amount}"

        headers = {
            "apikey": ""
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            result = response.json()
            converted_amount = result["result"]
            print(f"{self.amount} {self.currency} is equal to {converted_amount} {destination}.")
        else:
            print(f"An error occurred. Status code: {response.status_code}")


print("Enter the currency you want to convert (3 Letter Code): ")
baseCurrency = input()
print("Enter the amount you would like to convert: ")
baseAmount = input()
instance = SimpleCurrencyConverter(baseCurrency, baseAmount)
print("What would you like to convert your currency to (3 Letter Code): ")
resultCurrency = input()
instance.convert(resultCurrency)
