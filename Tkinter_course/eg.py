import tkinter as tk 
from tkinter import messagebox

root = tk.Tk()
root.title("temperature converter ")
root.geometry("300x150")




# creating the widget s
c_label = tk.Label(root, text="Celsuis")
c_entry = tk.Entry(root,width=30)



f_label = tk.Label(root, text="F")
f_entry = tk.Entry(root, width=30)




temp_convert_button = tk.Button(root, text="Convert", command=convert_tem)
clear_temp_button  = tk.Button(root, text="Clear", command=clear_temp)



#arranging our widgets 

c_label.grid(row=0, column=0, padx=10 , pady=5, sticky="w")





