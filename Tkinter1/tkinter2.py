import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Hello Tkinter")
root.geometry("500x500")


frame = ttk.Frame(root, padding = 12)
frame.grid(row=0, column=0, sticky= "NSEW")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)   
frame.columnconfigure(1, weight=1)

name_var = tk.StringVar()
ttk.Label(frame, text = "Name:").grid(row=0, column=0, sticky="W", pady = 6)
ttk.Entry(frame, textvariable = name_var).grid(row=0, column=1, sticky="EW", pady = 6)
root.mainloop()
