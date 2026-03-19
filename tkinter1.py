import tkinter as tk
from tkinter import messagebox
import csv
import os

root = tk.Tk()
root.title("Student Registration Form")
root.geometry("400x550")

tk.Label(root, text="Student Details Form",
         font=("Arial", 16), fg="white", bg="green",
         width=30, height=2).pack(pady=10)

tk.Label(root, text="Student Name:", font=("Arial", 11)).place(x=40, y=100)
name_entry = tk.Entry(root, width=25, borderwidth=2)
name_entry.place(x=160, y=100)

tk.Label(root, text="Phone Number:", font=("Arial", 11)).place(x=40, y=150)
phone_entry = tk.Entry(root, width=25, borderwidth=2)
phone_entry.place(x=160, y=150)

tk.Label(root, text="Department:", font=("Arial", 11)).place(x=40, y=200)
depart_var = tk.StringVar()
departments = ["CSE", "ECE", "EEE", "MECH", "CIVIL", "IT"]
depart_menu = tk.OptionMenu(root, depart_var, *departments)
depart_menu.place(x=160, y=195)

tk.Label(root, text="Gender:", font=("Arial", 11)).place(x=40, y=250)
gender_var = tk.StringVar(value="None")
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").place(x=160, y=250)
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").place(x=220, y=250)
tk.Radiobutton(root, text="Other", variable=gender_var, value="Other").place(x=290, y=250)

tk.Label(root, text="Mark:", font=("Arial", 11)).place(x=40, y=300)
mark_entry = tk.Entry(root, width=10, borderwidth=2)
mark_entry.place(x=160, y=300)

def save_to_csv(data):
    file_exists = os.path.isfile("students.csv")
    with open("students.csv", "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Name", "Phone", "Department", "Gender", "Mark"])
        writer.writerow(data)

def submit():
    name = name_entry.get()
    phone = phone_entry.get()
    dept = depart_var.get()
    gender = gender_var.get()
    mark = mark_entry.get()

    if name == "" or phone == "" or dept == "" or gender == "None" or mark == "":
        messagebox.showerror("Error", "Please fill all fields!")
        return

    if not phone.isdigit() or len(phone) != 10:
        messagebox.showerror("Error", "Enter a valid 10-digit phone number!")
        return

    save_to_csv([name, phone, dept, gender, mark])

    messagebox.showinfo(
        "Student Saved",
        f"Data Saved Successfully!\n\n"
        f"Name: {name}\nPhone: {phone}\nDepartment: {dept}\nGender: {gender}\nMark: {mark}"
    )

def cancel():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    mark_entry.delete(0, tk.END)
    depart_var.set("")
    gender_var.set("None")
    messagebox.showinfo("Cancelled", "All fields cleared!")

tk.Button(root, text="SUBMIT", width=15, height=2,
          bg="gray", command=submit).place(x=60, y=380)

tk.Button(root, text="CANCEL", width=15, height=2,
          bg="gray", command=cancel).place(x=200, y=380)

root.mainloop()
