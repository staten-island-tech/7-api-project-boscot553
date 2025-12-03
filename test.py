import requests
import tkinter as tk
def do_search():
    global query
    query = search_var.get()
    print("Searching for:", query)
    getWord(query)
    
def change_text():
    label.config(text="New text!")
    
def getWord(words):
    num = -1
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{query}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    word = (f"Word:", data[0]["word"])
    for i in data[0]["meanings"]:
        num += 1
    definition = (f"Definition(s):", data[0]["meanings"][num]["definitions"][0]["definition"])
    synonyms = (f"Synonyms:", data[0]["meanings"][0]["synonyms"])
    Output.config(text=word)
    Output.place(x=350, y=350)
    Output1.config(text=definition)
    Output1.place(x=350, y=385)
    Output2.config(text=synonyms)
    Output2.place(x=350, y=445)

root = tk.Tk()
root.title("Dictionary")
root.geometry("3000x1250")
label = tk.Label(root, text="Welcome to dictionary! ")
label.pack(pady=20)
label.place(x=700, y=150)
label.config(font=("Verdana", 30))
Output = tk.Label(root, text="Defintion", wraplength=1000)
Output.place(x=750, y=350)
Output.config(font=("Verdana", 15))
Output.place_forget()
Output1 = tk.Label(root, text="Defintion", wraplength=1500)
Output1.place(x=750, y=350)
Output1.config(font=("Verdana", 10))
Output1.place_forget()
Output2 = tk.Label(root, text="Defintion ")
Output2.place(x=750, y=350)
Output2.config(font=("Verdana", 10))
Output2.place_forget()
Output3 = tk.Label(root, text="Defintion ")
Output3.place(x=750, y=350)
Output3.config(font=("Verdana", 10))
Output3.place_forget()

search_var = tk.StringVar()

entry = tk.Entry(root, width=40, textvariable=search_var, font=('Arial', 12))
entry.pack(side="left", padx=5, pady=10)

button = tk.Button(root, text="Search", command=do_search)
button.pack(side="left", padx=5)
button.place(x=725, y= 300)
entry.place(x=775, y=300)
root.mainloop()






