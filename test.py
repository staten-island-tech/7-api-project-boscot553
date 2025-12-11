import requests
from PIL import Image
from io import BytesIO

url = "https://upload.wikimedia.org/wikipedia/commons/0/02/Websters_Dictionary.jpg"

response = requests.get(url)
img = Image.open(BytesIO(response.content))

img.show()