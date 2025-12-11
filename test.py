import tkinter as tk
from PIL import Image, ImageTk
import os

# File name here — change this to your actual file
image_path = "https://upload.wikimedia.org/wikipedia/commons/4/41/Sunflower_from_Silesia2.jpg"

print("Current working directory:", os.getcwd())

# Check if the file exists before loading it
if not os.path.exists(image_path):
    print("ERROR: File not found:", image_path)
else:
    root = tk.Tk()
    root.title("Image Viewer")

    img = Image.open(image_path)  # If this fails, the path is wrong or unsupported format
    photo = ImageTk.PhotoImage(img)

    label = tk.Label(root, image=photo)
    label.image = photo
    label.pack()

    root.mainloop()