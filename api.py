import tkinter as tk
import keyboard

x = 0


root = tk.Tk()
root.title("Cookie clicker")
root.geometry("3000x1250")
label = tk.Label(root, text="0")
label.pack(pady=20)
label.place(x=885, y=150)
label.config(font=("Verdana", 30))

class cookies():
    def __init__ (self, num, cost, production):
        self.num = num
        self.cost = cost
        self.production = production


def on_button_click():
    cookie.num += cookie.production    
    label.config(text=cookie.num)
        
cookie = cookies(0, 10, 1)

def upgrade():
    if cookie.num >= cookie.cost:
        cookie.num -= cookie.cost
        label.config(text=cookie.num)
        cookie.cost = cookie.cost 
        cookie.production += 1
        
button = tk.Button(root, text="Click Me", command=on_button_click, width = 20, height= 10)
upgrade_button = tk.Button(root, text="Upgrade", command=upgrade, width = 20, height= 5)
button.pack()
upgrade_button.pack()
button.place(x=830,y=250)
upgrade_button.place(x=0, y=900)
root.mainloop()
