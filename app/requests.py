import requests


def getQuotes():
    response = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    if response.status_code == 200:
        print(response.json())
        return response.json()
