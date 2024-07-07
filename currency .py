import requests # type: ignore

def get_exchange_rate(api_key, from_currency, to_currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code != 200:
        raise Exception(f"Error fetching exchange rate data: {data['error-type']}")
    
    return data['conversion_rates'][to_currency]

def convert_currency(api_key, amount, from_currency, to_currency):
    exchange_rate = get_exchange_rate(api_key, from_currency, to_currency)
    return amount * exchange_rate

if __name__ == "__main__":
    api_key = "f583af9bb7ba59396afa9b03"  # Replace with your actual API key
    amount = float(input("Enter the amount to convert: "))
    from_currency = input("Enter the currency to convert from (e.g., USD): ").upper()
    to_currency = input("Enter the currency to convert to (e.g., EUR): ").upper()
    
    try:
        converted_amount = convert_currency(api_key, amount, from_currency, to_currency)
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    except Exception as e:
        print(e)
