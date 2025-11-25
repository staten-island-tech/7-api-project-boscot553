import requests

def findstock(stock):
    response = requests.get(f"https://www.stockdata.org/{stock.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    data = response.json()
    return {
        "name": data["data"]["name"],

    }

stockdata = findstock("Tesla inc")
print(stockdata)