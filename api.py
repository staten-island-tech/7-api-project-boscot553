import tkinter as tk
import keyboard

x = 0

root = tk.Tk()
root.title("Cookie clicker")
root.geometry("300x200")
label = tk.Label(root, text="0")
label.pack(pady=20)



class cookies():
    def __init__ (self, num):
        self.num = num
    
def on_button_click():
    cookie.num += 1    
    label.config(text=cookie.num)
        
cookie = cookies(0)

def upgrade():
    cost1 = 9
    if cookie.num > cost1:
        cookie.num -= 10
        label.config(text=cookie.num)
        cost1 += 1
        cost1 = cost1 * 2

keyboard.add_hotkey('z', upgrade)
button = tk.Button(root, text="Click Me", command=on_button_click, width = 20, height= 20)
button.pack()

root.mainloop()
