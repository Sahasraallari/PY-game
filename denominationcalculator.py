import tkinter as tk
from tkinter import messagebox


def calculate_denomonations():
    try:
        amount = int(amount_entry.get())
        if amount <= 0:
            messagebox.showerror("Error", "Please enter a positive amount")
            return
        denomonations  =[500, 200, 100, 50, 20, 10, 5, 2, 1]
        result = ""
        for denom in denomonations:
            count = amount // denom
            if count > 0:
                result += f"{denom} : {count}\n"
            amount = amount % denom

        result_label.config(test=result)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")



root = tk.Tk()
root.title("Denomination Calculator")
root.geometry("400x300")

tk.Label(root, text = "Enter Amount:")
amount_entry = tk.Entry(root)
amount_entry.pack(pady=5)


tk.Button(root, text = "Calculate", command=calculate_denomonations).pack(pady=10)


result_label = tk.Label(root, text = "", justify = "left", font=("Arial, 12") )

root.mainloop()






    






