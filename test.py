import requests
import mysql.connector
import customtkinter as tk
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

class Password_gen():
    def __init__(self, caps, num, sim, char):
        self.caps = caps
        self.num = num
        self.sim = sim
        self.char = char
        self.generated_password = None

    def Pass_gen(self):
        url = f"https://www.psswrd.net/api/v1/password/?length={self.char}&lower=0&upper={self.caps}&int={self.num}&special={self.sim}"
        response = requests.get(url)
        self.generated_password = response.text

# AES encryption function
def encrypt(text, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(text.encode(), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return iv, ct

# AES decryption function
def decrypt(iv, ct, key):
    iv = base64.b64decode(iv)
    ct = base64.b64decode(ct)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode('utf-8')

def savedata(generated_password, log):
    db_config = {
        'host': '127.0.0.1',
        'user': 'root',
        'password': '123123',
        'database': 'password_generation'
    }
    encryption_key = b'ThisIsASecretKey'

    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    iv, encrypted_password = encrypt(generated_password, encryption_key)
    info = (encrypted_password, iv, log)
    query = "INSERT INTO generated_passwords (password, iv, login) VALUES (%s, %s, %s)"
    cursor.execute(query, info)

    connection.commit()
    cursor.close()
    connection.close()

def showpass():
    db_config = {
        'host': '127.0.0.1',
        'user': 'root',
        'password': '123123',
        'database': 'password_generation'
    }
    encryption_key = b'ThisIsASecretKey'

    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    query = "SELECT iv, password, login FROM generated_passwords"
    cursor.execute(query)

    result = cursor.fetchall()

    showdata = []
    for iv, encrypted_password, login in result:
        decrypted_password = decrypt(iv, encrypted_password, encryption_key)
        showdata.append((login, decrypted_password))

    cursor.close()
    connection.close()

    tk.set_appearance_mode("dark")
    tk.set_default_color_theme("dark-blue")

    root3 = tk.CTk()
    root3.title('Data')
    root3.geometry()

    for login, password in showdata:
        labv = tk.CTkLabel(root3,text=f"Login: {login}, {password}",font=('',22))
        labv.pack(pady= 30, expand=True)

    root3.mainloop()

def generate_password():
    caps = "1" if checkbox1.get() else "0"
    sim = "1" if checkbox2.get() else "0"
    num = "1" if checkbox3.get() else "0"
    char = entry2.get()
    log = entry.get()

    password_generator = Password_gen(caps, num, sim, char)
    password_generator.Pass_gen()
    generated_password = password_generator.generated_password
    frame(generated_password, log)

def frame(generated_password, log):
    tk.set_appearance_mode("dark")
    tk.set_default_color_theme("dark-blue")

    root2 = tk.CTk()
    root2.title('Password')
    root2.geometry()
    
    labvl2 = tk.CTkLabel(root2,text=f"Login: {log}",font=('',22))
    labvl2.pack(pady= 30, expand=True)

    labvl = tk.CTkLabel(root2,text=generated_password,font=('',22))
    labvl.pack(pady= 30,expand=True)

    button = tk.CTkButton(root2, text="Save", font=('', 20),command=lambda: savedata(generated_password, log))
    button.pack(pady=20, padx=30)

    button4 = tk.CTkButton(root2, text="exit",  font=('', 20),command=root2.destroy)
    button4.pack(pady=20, padx=30)

    root2.mainloop()

#dizains aplikācijai
tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")

root = tk.CTk()
root.title('Password generator')
root.geometry("1200x600")

tabview = tk.CTkTabview(root)
tabview.pack(padx=20, pady=10, fill="both", expand=True)

tab_1 = tabview.add("Generate password")
tab_2 = tabview.add("Saved passwords")
tabview.set("Generate password")

entry = tk.CTkEntry(tab_1, placeholder_text="Login", width=1000)
entry.pack(pady=40)

checkbox1 = tk.CTkCheckBox(tab_1, text="Caps", width=900,)
checkbox1.pack(pady=30)

checkbox2 = tk.CTkCheckBox(tab_1, text="Symbol", width=900)
checkbox2.pack(pady=30)

checkbox3 = tk.CTkCheckBox(tab_1, text="Numbers", width=900)
checkbox3.pack(pady=30)

entry2 = tk.CTkEntry(tab_1, placeholder_text="Password length", width=1000)
entry2.pack(pady=40)

button = tk.CTkButton(tab_1, text="Generate password", font=('', 20), width=1000, height=50, command=generate_password)
button.pack(pady=20, padx=30)

Button2= tk.CTkButton(tab_2, text="Show Data", font=('', 20), width=900, height=200, command=showpass)
Button2.pack(pady=200, padx=30)

root.mainloop()
