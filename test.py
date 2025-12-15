import requests

def getPoke():
    response = requests.get(f"/api/v2/facts/random?language=en")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return data

getPoke()