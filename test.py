import requests
from tkinter import BooleanVar
import customtkinter as tk

class Password_gen():
    def __init__(self, caps, num, sim, char):
        self.caps = caps
        self.num = num
        self.sim = sim
        self.char = char
        self.generated_password = None

    def generate_password(self):
        url = f"https://passwordinator.onrender.com?{self.num}&{self.sim}&{self.caps}&len={self.char}"
        response = requests.get(url)
        self.generated_password = response.text
        return self.generated_password

def generate_password_callback():
    print("Button clicked")
    caps = "caps=true" if caps_var.get() else ""
    num = "num=true" if num_var.get() else ""
    sim = "char=true" if sim_var.get() else ""
    char = length_entry.get()
    print(f"caps: {caps}, num: {num}, sim: {sim}, char: {char}")
    password_generator.caps = caps
    password_generator.num = num
    password_generator.sim = sim
    password_generator.char = char
    generated_password = password_generator.generate_password()
    print("Generated password:", generated_password)  # Add this line for debugging
    password_label.configure(text=generated_password)


password_generator = Password_gen(False, False, False, 8)

tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")

root = tk.CTk()
root.title('Password generator')
root.geometry("1200x600")

tabview = tk.CTkTabview(root)
tabview.pack(padx=20, pady=10 , fill="both", expand=True)

tab_1 = tabview.add("Generate password")
tabview.set("Generate password")

caps_var = BooleanVar()
caps_checkbox = tk.CTkCheckBox(tab_1, text="Caps", variable=caps_var, width=900)
caps_checkbox.pack(pady=20)

sim_var = BooleanVar()
sim_checkbox = tk.CTkCheckBox(tab_1, text="Symbol", variable=sim_var, width=900)
sim_checkbox.pack(pady=20)

num_var = BooleanVar()
num_checkbox = tk.CTkCheckBox(tab_1, text="Numbers", variable=num_var, width=900)
num_checkbox.pack(pady=20)

length_entry = tk.CTkEntry(tab_1, placeholder_text="Password length", width=200)
length_entry.place(x=120, y=325)

generate_button = tk.CTkButton(tab_1, text='Generate password', font=('', 20), height=100, width=200, command=generate_password_callback)
generate_button.pack(pady=100)

password_label = tk.CTkLabel(tab_1, text='', width=900)
password_label.pack(pady=20)

root.mainloop()
