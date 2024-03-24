import requests

def get_bitcoin_price(currency='USD'):
    url = f'https://api.coindesk.com/v1/bpi/currentprice/{currency}.json'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        bitcoin_price = data['bpi'][currency]['rate']
        return bitcoin_price
    else:
        return None

currency = 'USD'  # Валюта, за якою буде проводитись запит
bitcoin_price = get_bitcoin_price(currency)
if bitcoin_price is not None:
    print(f"Ціна Bitcoin в {currency}: {bitcoin_price}")
else:
    print("Помилка при виконанні запиту до API CoinDesk")
