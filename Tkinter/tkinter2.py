import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.title("Hello Tkinter")
root.geometry("500x250")
root.columnconfigure(0, weight=1)  
root.rowconfigure(0, weight=1)

style = ttk.Style()
style.configure('pink.TFrame', background='pink')

frame = ttk.Frame(root, padding = 12, style='pink.TFrame')
frame.grid(row=0, column=0, sticky= "NSEW") 
frame.columnconfigure(0, weight=1)

name_var = tk.StringVar()
ttk.Label(frame, text = "Name:").grid(row=0, column=0, sticky="W", pady = 6, padx = 6)
ttk.Entry(frame, textvariable = name_var).grid(row=0, column=1, sticky="EW", pady = 6, padx = 6)

def greet():
    messagebox.showinfo("Hello", f'hi {name_var.get().strip()}')
ttk.Button(frame, text = "Greet", command = greet).grid(row=1, column=0, columnspan=2, pady = 6, padx = 6)

root.mainloop()
