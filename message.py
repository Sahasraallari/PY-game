import tkinter as tk
from tkinter import messagebox

def info_box():
    messagebox.showinfo("Information",  "This is an information message.")


def warning_box():
    messagebox.showwarning("Warning",  "This is an warning message!")
    

def error_box():
    messagebox.showerror("Error",  "An erroe has occured!")
    
def question_box():
    response = messagebox.askquestion("Question", "Do you like Python!")
    print("Response:", response)

def ok_cancle_box():
    response = messagebox.askokcancle("Confrim", "Do you want to proceed!")
    print("Response:", response)


def yes_no_box():
    response = messagebox.askyesno("Confrim", "Do you want to save changes!")
    print("Response:", response)


def retrey_cancle_box():
    response = messagebox.askquestion("Retrey", "Operation failed.retrey!")
    print("Response:", response)

root = tk.Tk()
root.title("Message Box Examples")
root.geometry("400x300")

tk.Button(root, text="Show Info", command=info_box).pack(pady=5)
tk.Button(root, text="Show Warning", command=warning_box).pack(pady=5)
tk.Button(root, text="Show Error", command=error_box).pack(pady=5)
tk.Button(root, text="Ask Question", command=question_box).pack(pady=5)
tk.Button(root, text="Ask Ok Cancle", command=ok_cancle_box).pack(pady=5)
tk.Button(root, text="Ask Yes NO", command=yes_no_box).pack(pady=5)
tk.Button(root, text="Ask Retrey Cancle", command=retrey_cancle_box).pack(pady=5)

root.mainloop()









    

