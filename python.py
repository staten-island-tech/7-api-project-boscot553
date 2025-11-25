import requests
chess = requests.get(f"https://www.chess.com/news/view/published-data-api")
print(chess["username"])