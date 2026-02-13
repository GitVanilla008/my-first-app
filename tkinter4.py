import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#set up root and frame
root = tk.Tk()
root.title("Student Information")
root.geometry("950x450")
root.columnconfigure(0, weight=1)  
root.rowconfigure(0, weight=1)


style = ttk.Style()
style.configure('pink.TFrame', background='pink')

frame = ttk.Frame(root, padding = 12, style='pink.TFrame')
frame.grid(row=0, column=0, sticky= "NSEW") 
frame.columnconfigure(0, weight=1)

id_var = tk.StringVar()
name_var = tk.StringVar()
bus_var = tk.BooleanVar()

ttk.Label(frame, text = "Student ID:").grid(row=0, column=0, sticky="W", pady = 6, padx = 6)
ttk.Entry(frame, textvariable = id_var).grid(row=0, column=1, sticky="EW", pady = 6, padx = 6)

ttk.Label(frame, text = "Name:").grid(row=1, column=0, sticky="W", pady = 6, padx = 6)
ttk.Entry(frame, textvariable = name_var).grid(row=1, column=1, sticky="EW", pady = 6, padx = 6)

ttk.Label(frame, text = "Bus Traveller:").grid(row=2, column=0, sticky="W", pady = 6, padx = 6)
ttk.Checkbutton(frame, text = "True", variable = bus_var).grid(row=2, column=1, sticky="W", pady = 6, padx = 6)

treeview = ttk.Treeview(frame, columns=("Id","Name", "Bus"),show="headings")
treeview.grid(row=5, column=0, columnspan=2, sticky = "EW",pady = 6)
treeview.heading("Id", text = "Id")
treeview.heading("Name", text = "Name")
treeview.heading("Bus", text = "Bus")
treeview.column("Id", minwidth = 100, width= 100)
treeview.column("Name", minwidth = 100, width= 100)
treeview.column("Bus", minwidth = 100, width= 100)

treeview.insert("", tk.END, values=("123456", "Sudharshini", False))
treeview.insert("", tk.END, values=("654321", "Bob", False))

style = ttk.Style()
style.configure("Treeview", rowheight = 30)

def save(_event=None):
    if not id_var.get().strip().isdigit():
        messagebox.showerror("Invalid", "Student ID must be a number.")
        return
    if not name_var.get().strip():
        messagebox.showerror("Invalid", "Name is required.")
        return
    
    messagebox.showinfo("Student Information", f'Saved Student ID: {id_var.get().strip()}, Name: {name_var.get().strip()}, Bus: {bus_var.get()}')
ttk.Button(frame, text = "Save", command = save).grid(row=3, column=0, columnspan=2, pady = 6, padx = 6)

root.mainloop()