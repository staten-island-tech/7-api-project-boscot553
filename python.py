import requests
import tkinter as tk
x = ''
def do_search():
    global query
    query = search_var.get()
    print("Searching for:", query)
    change_text
    
def change_text():
    label.config(text="New text!")
    label.pack_configure

root = tk.Tk()
root.title("Dictionary")
root.geometry("3000x1250")
label = tk.Label(root, text="Welcome to dictionary! ")
label.pack(pady=20)
label.place(x=700, y=150)
label.config(font=("Verdana", 30))

output = tk.Label(root, text="")
output.pack(pady=20)
output.place(x=700, y=400)
output.config(font=("Verdana", 30))
search_var = tk.StringVar()

entry = tk.Entry(root, width=40, textvariable=search_var, font=('Arial', 12))
entry.pack(side="left", padx=5, pady=10)

button = tk.Button(root, text="Search", command=do_search)
button.pack(side="left", padx=5)
button.place(x=725, y= 300)
entry.place(x=775, y=300)
root.mainloop()

x = query
def getWord(words):
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{x}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    print(f"Word:", {data[0]["word"]})
    print(f"Phonetics:", data[0]["phonetics"])
    print(f"Meanings:", data[0]["meanings"][0]["definitions"][0]["definition"])
    print(f"Synonyms:", data[0]["meanings"][0]["synonyms"])
    change_text


word = getWord(x)
print(word)