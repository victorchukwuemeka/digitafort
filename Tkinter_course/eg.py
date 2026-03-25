import tkinter as tk 
from tkinter import messagebox




def convert_temp():
    "convertion button  function  happens here"
    cel_entry = c_entry.get()
    fah_entry = f_entry.get()

    if cel_entry:
        cel_entry_float = float(cel_entry)
        fah_result = (cel_entry_float * 9/5) + 32

        fah_result.delete(0, tk.END)
        fah_result.insert(0, f"{fah_result:.2f}")

    elif fah_entry:
        fah_entry_float = float(fah_entry)
        cel_result = (fah_entry_float - 32) * 5/9

        cel_result.delete(0,tk.END)
        cel_result.insert(0, f"{fah_result:.2f}")
        
    else :
        messagebox.showerror("INPUT ERROR","Put a proper input ")


def clear_temp():
    c_entry.delete(0,tk.END)
    f_entry.delete(0,tk.END)


root = tk.Tk()
root.title("temperature converter ")
root.geometry("300x150")




# creating the widget s
c_label = tk.Label(root, text="Celsuis")
c_entry = tk.Entry(root,width=30)



f_label = tk.Label(root, text="F")
f_entry = tk.Entry(root, width=30)




#command=convert_tem
#command=clear_temp
temp_convert_button = tk.Button(root, text="Convert", command=convert_temp)
clear_temp_button  = tk.Button(root, text="Clear", command=clear_temp)



#arranging our widgets 
c_label.grid(row=0, column=0, padx=10 , pady=5, sticky="w")
c_entry.grid(row=0, column=1, padx=10, pady=5)


f_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
f_label.grid(row=1, column=1, padx=10, pady=5)



temp_convert_button.grid(row=2, columnspan=2, pady=10)
clear_temp_button.grid(row=3, column=0, columnspan=2, pady=5)



root.mainloop()













