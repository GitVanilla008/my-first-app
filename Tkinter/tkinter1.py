import tkinter as tk
root = tk.Tk()
root.title("My First App")
root.geometry("300x200")

label = tk.Label(root, text="Hello, Tkinter!")
label.place(x = 110, y = 40)
button = tk.Button(root, text="Click Me", command = lambda:label.config(text = "you clicked the button!"))
button.place(x = 110, y = 80)
root.mainloop()