import tkinter as tk

root = tk.Tk()
root.title("Narzędzie do automatyzacji oprogramowania")
root.geometry("300x200")
label_welcom = tk.Label(root, text="Witaj w aplikacji", font=("Arial", 14))
label_welcom.pack(pady=20)
label_chose = tk.Label(root, text="Wybierz", font=("Arial", 14))
label_chose.pack(pady= 10)

menu_bar = tk.Frame(root)
menu_bar.pack(side=tk.TOP, fill=tk.X)

btn1 = tk.Button(menu_bar, text="GIT")
btn1.pack(side=tk.LEFT, padx=5)

btn2 = tk.Button(menu_bar, text="Github Actions")
btn2.pack(side=tk.LEFT, padx=5 )

btn3 = tk.Button(menu_bar, text="Docker")
btn3.pack(side=tk.LEFT, padx=5 )

btn4 = tk.Button(menu_bar, text="Pytest")
btn4.pack(side=tk.LEFT, padx=5 )

root.mainloop()

 