
import tkinter as tk

root = tk.Tk()

root.title(" Your App")


label = tk.Label(root, text="Hello, Tkinter!")
#def on_button_click():
#    print("button click")

#button = tk.Button(root, text="Click me", command=on_button_click)
#button.pack()
#entry = tk.Entry(root, width=30)
#entry.pack()

#scale = tk.Scale(root, from_=10, to=100, orient=tk.HORIZONTAL)
#scale.pack()


scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox = tk.Listbox(root,yscrollcommand=scrollbar.set)
for i in range(50):
    listbox.insert(tk.END, f"item{i}")
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=listbox.yview)
root.mainloop()





