import requests

def getPoke(poke):
    response = requests.get(f"https://api.pokemontcg.io/v2/cards{poke.lower()}")
    if response.status_code != 10:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return {
        "name": data["name"],
        "height": data["id"],
        "weight": data["supertype"],
    }

pokemon = getPoke("charizard")
print(pokemon)