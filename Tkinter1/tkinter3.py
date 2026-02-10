import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#set up root and frame
root = tk.Tk()
root.title("Student Information")
root.geometry("500x250")
root.columnconfigure(0, weight=1)  
root.rowconfigure(0, weight=1)

style = ttk.Style()
style.configure('pink.TFrame', background='pink')

frame = ttk.Frame(root, padding = 12, style='pink.TFrame')
frame.grid(row=0, column=0, sticky= "NSEW") 
frame.columnconfigure(0, weight=1)

name_var = tk.StringVar()
id_var = tk.StringVar()
ttk.Label(frame, text = "Student ID:").grid(row=0, column=0, sticky="W", pady = 6, padx = 6)
id_entry = ttk.Entry(frame, textvariable = id_var).grid(row=0, column=1, sticky="EW", pady = 6, padx = 6)
ttk.Label(frame, text = "Name:").grid(row=1, column=0, sticky="W", pady = 6, padx = 6)
ttk.Entry(frame, textvariable = name_var).grid(row=1, column=1, sticky="EW", pady = 6, padx = 6)

def save(_event=None):
    if not id_var.get().strip().isdigit():
        messagebox.showerror("Invalid", "Student ID must be a number.")
        return
    if not name_var.get().strip():
        messagebox.showerror("Invalid", "Name is required.")
        return
    messagebox.showinfo("Student Information", f'Saved Student ID: {id_var.get().strip()}, Name: {name_var.get().strip()}')
ttk.Button(frame, text = "Save", command = save).grid(row=2, column=0, columnspan=2, pady = 6, padx = 6)

root.mainloop()

