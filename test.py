import cv2
import numpy as np
import requests

url = "https://upload.wikimedia.org/wikipedia/commons/0/02/Websters_Dictionary.jpg"

resp = requests.get(url)
img_array = np.asarray(bytearray(resp.content), dtype=np.uint8)
img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

cv2.imshow("Dictionary", img)
cv2.waitKey(0)
cv2.destroyAllWindows()