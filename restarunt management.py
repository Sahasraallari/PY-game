import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Restarunt Management System")
root.geometry("500x500")

menu = {
    "Burger": 100,
    "Pizza": 200,
    "Fries": 60,
    "Chicken Popcorn": 150,
    "Chilli Chicken": 200,
    "Ice Creams": 80,
    "Drinks": 50
}

variables = {}
quantities  = {}

tk.Label(root, text = "Restarunt Menu", font=('Arial',18, 'bold' )).pack(pady=10)

menu_frame = tk.Frame(root)
menu_frame.pack()

for item, price in  menu.items():
    var = tk.IntVar()
    qty = tk.StringVar(value="0")
    variables[item] = var
    quantities[item] = qty

    frame  = tk.Frame(menu_frame)
    frame.pack(anchor="w", padx=20)

    tk.Checkbutton(frame, text=f"{item} - ₹{price}", variable=var).pack(side="left")
    tk.Entry(frame, width=5, textvariable=qty ).pack(side="left", padx=10)

def calculate_total():
    total = 0
    order_details = ""
    for item in menu:
        if variables[item].get == 1:
            try:

                qty = int(quantities[item].get())
                if qty < 0 :
                    raise ValueError
                price = menu[item] * qty
                total += price
                order_details += f"{item} x {qty} =  ₹{price}\n "
            except ValueError:
                messagebox.showerror("Invalid input",f"Enter a valid quantity for{item}" )

    if total == 0:

      messagebox.showinfo("No Selection", "Please select at least one item.")
    else:
      messagebox.showinfo("Bill", f"{order_details}\nTotal = ₹{total}")
# Button
tk.Button(root, text="Generate Bill", command=calculate_total, bg="green", fg="white", font=('Arial', 12)).pack(pady=20)
root.mainloop()




 


                




















