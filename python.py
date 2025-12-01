import requests

def getPoke(poke):
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/hello")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return {
        "name": data[0]["word"],
        "phonetics": data[0]["phonetics"],
        "meanings": data[0]["meanings"]
    }

pokemon = getPoke("Hello")
print(pokemon)