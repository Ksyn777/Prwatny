import tkinter as tk
import sqlite3 

root = tk.Tk()
root.title("Narzędzie do automatyzacji oprogramowania")
root.geometry("500x400")

label_welcom = tk.Label(root, text="Witaj w aplikacji", font=("Arial", 20))
label_welcom.grid(row=0, padx=10)
label_chose = tk.Label(root, text="Wybierz", font=("Arial", 14))
label_chose.grid(row=2, padx=10)

entries = {}

# --- Otwieramy połączenie z bazą i tworzymy tabelę NA RAZIE ---
baza = sqlite3.connect("baza.db")
cursor = baza.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS dane (
    Names TEXT, 
    Email TEXT,
    Age INTEGER
)
""")
baza.commit()
# NIE ZAMYKAMY bazy tutaj — bo potrzebujemy jej w dalszej części programu

def on_button():
    print("Kliknięto Przycisk") 

def safe_date():
    names = entries["names"].get()
    email = entries["email"].get()
    age = entries["age"].get()

    # Wykonujemy zapytanie do otwartej bazy
    cursor.execute("INSERT INTO dane (Names, Email, Age) VALUES (?, ?, ?)", (names, email, age))
    baza.commit()
    
    # Czyścimy pola po zapisie
    for entry in entries.values():
        entry.delete(0, tk.END)
    
menu_bar = tk.Frame(root)
menu_bar.grid()

btn1 = tk.Button(menu_bar, text="GIT", command=on_button)
btn1.grid(row=4, column=0, padx=5)

btn2 = tk.Button(menu_bar, text="Github Actions", command=on_button)
btn2.grid(row=4, column=1, padx=5)

btn3 = tk.Button(menu_bar, text="Docker", command=on_button)
btn3.grid(row=4, column=2, padx=5)

btn4 = tk.Button(menu_bar, text="Pytest", command=on_button)
btn4.grid(row=4, column=3, padx=5)

login_label = tk.Label(root, text="USERNAME: ")
login_entry = tk.Entry(root)
password_label = tk.Label(root, text="PASSWORD: ")
password_entry = tk.Entry(root)

login_label.grid(row=5, column=0, sticky="W")
login_entry.grid(row=5, column=1)
password_label.grid(row=6, column=0, sticky="W")
password_entry.grid(row=6, column=1)

labels = ["Names", "Email", "Age"]
for i, text in enumerate(labels):
    label = tk.Label(root, text=text)
    label.grid(row=i+7, column=0, sticky="w")
    entry = tk.Entry(root)
    entry.grid(row=i+7, column=1)
    entries[text.lower()] = entry

save_button = tk.Button(root, text="Zapisz do bazy", command=safe_date)
save_button.grid(row=9, column=0, columnspan=2)

root.mainloop()

# Po zamknięciu okna zamykamy połączenie z bazą
baza.close()
