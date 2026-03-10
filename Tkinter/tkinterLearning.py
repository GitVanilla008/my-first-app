import tkinter as tk
from tkinter import ttk #treeview is not in tkinter so we have to add it

root = tk.Tk() #this creates the window
root.title("Student Table") #this sets the title of the window
root.geometry("500x300") #this sets the size of the window, width x height

tree = ttk.Treeview.root #this creates a table in the window

root.mainloop() #this keeps the window open