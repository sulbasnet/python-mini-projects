import requests

API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

def convert(amount, from_currency, to_currency):
    try:
        response = requests.get(API_URL)
        data = response.json()

        rates = data["rates"]

        if from_currency not in rates or to_currency not in rates:
            print("Invalid currency code!")
            return

        usd_amount = amount / rates[from_currency]
        converted = usd_amount * rates[to_currency]

        print(f"\n{amount} {from_currency} = {round(converted, 2)} {to_currency}")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    print("=== Currency Converter ===")

    amount = float(input("Enter amount: "))
    from_currency = input("From currency (e.g. USD, EUR, NPR, INR): ").upper()
    to_currency = input("To currency: ").upper()

    convert(amount, from_currency, to_currency)
