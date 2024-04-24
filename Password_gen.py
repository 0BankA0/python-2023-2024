# Atsauce uz API paroles ģeneratoru https://www.psswrd.net/api/

import requests # Tiek importēta bibliotēka, lai varētu izmantot API.
import mysql.connector # Tiek importēta bibliotēka, kura ļauj savienot kodu ar datu bāzi.
import customtkinter as tk # Tiek importēta bibliotēka, ar kuras palīdzību tiek veidots savienojums ar datu bāzi.

class Password_gen():# Definēta klase Password_gen.
    def __init__(self, caps, num, sim, char):# Definēti argumenti klases sākumā.
        self.caps = caps # Mainīgais, kuram ir noteikta vērtība.
        self.num = num
        self.sim = sim 
        self.char = char 
        self.generated_password = None

    def Pass_gen(self): # Definēta funkcija, kurā notiek paroles ģenerēšana.
        url = f"https://www.psswrd.net/api/v1/password/?length={self.char}&lower=0&upper={self.caps}&int={self.num}&special={self.sim}" # Mainīgais, kurā ir URL uz API, kurš ģenerē paroli.
        response = requests.get(url) # Mainīgais, kurā glabājas dati no API.
        self.generated_password = response.text # Mainīgais no funkcijas __init__, kurā glabājas informācija no API str formātā.

def frame(generated_password, log): # Tiek izveidota funkcija, kurai ir nepieciešamas vērtības generated_password, log.
    tk.set_appearance_mode("dark") # Tiek norādīta galvenā krāsa priekš GUI.
    tk.set_default_color_theme("dark-blue") # Tiek norādīta otra krāsa priekš GUI.

    root2 = tk.CTk() # Mainīgais, kurā glabājas tk.CTk().
    root2.title('Password')# Tiek piešķirts nosaukums logam.
    root2.geometry() # Tiek norādīts izmērs logam.
    
    labvl2 = tk.CTkLabel(root2,text=f"Login: {log}",font=('',22)) # Tiek izveidots teksts, kurā tiek parādīta informācija no loga login.
    labvl2.pack(pady= 30, expand=True) # Tiek norādītas īpašības priekš objekta dizaina.

    labvl = tk.CTkLabel(root2,text=generated_password,font=('',22)) # Tiek izveidots teksts (parole).
    labvl.pack(pady= 30,expand=True)# Tiek norādītas īpašības priekš objekta dizaina.

    button = tk.CTkButton(root2, text="Save", font=('', 20),command=lambda: savedata(generated_password, log)) # Tiek izveidota poga, kura aizsūta visas vērtības uz funkciju generate_password.
    button.pack(pady=20, padx=30)

    button4 = tk.CTkButton(root2, text="exit",  font=('', 20),command=root2.destroy) 
    button4.pack(pady=20, padx=30)

    root2.mainloop() # Tiek palaižts GUI šajā funkcijā.
    
def savedata(generated_password, log): # Funkcija savedata, kurā notiek savienojums ar datu bāzi.
    db_config = {
        'host': '127.0.0.1',
        'user': 'root',
        'password': '123123',
        'database': 'password_generation'
    }

    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    
    info = (generated_password, log)
    query = "INSERT INTO generated_passwords (password, login) VALUES (%s, %s)"
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

    connection = mysql.connector.connect(**db_config)

    cursor = connection.cursor()

    query = "SELECT login, password FROM generated_passwords"
    cursor.execute(query)

    result = cursor.fetchall()

    showdata = []
    for row in result:
        showdata.append(row)
            

    cursor.close()
    connection.close()

    tk.set_appearance_mode("dark") 
    tk.set_default_color_theme("dark-blue") 

    root3 = tk.CTk() # Mainīgais, kurā glabājas tk.CTk().
    root3.title('Data')# Tiek piešķirts nosaukums logam.
    root3.geometry() # Tiek norādīts izmērs logam.
    for login, password in showdata:
        labv = tk.CTkLabel(root3,text=f"Login: {login}, {password}",font=('',22)) # Tiek izveidots teksts, kurā tiek parādīta informācija no loga login.
        labv.pack(pady= 30, expand=True) # Tiek norādītas īpašības priekš objekta dizaina.

    root3.mainloop()

def generate_password():
    caps = "1" if checkbox1.get() else "0" # Tiek saņemta vienība no checkbox, kur, ja vienība ir 1, tad tā būs vienāda ar mainīgo, citādi šī vienība būs 0.
    sim = "1" if checkbox2.get() else "0"
    num = "1" if checkbox3.get() else "0" 
    char = entry2.get() # Tiek saņemta informācija no input lodziņiem GUI.
    log = entry.get() 

    password_generator = Password_gen(caps, num, sim, char) # Mainīgais, kurā tiek ievadīti dati priekš klases objektiem.
    password_generator.Pass_gen() # Šeit tiek ģenerēta un glabāta parole.
    print(password_generator.generated_password) # Šeit ir dota pieeja pie ģenerētas paroles.
    generated_password = password_generator.generated_password # Tiek izveidots mainīgais, kurā tiek glabāta parole.
    frame(generated_password, log) # Mainīgie no šīs funkcijas ir savienoti ar funkciju frame.


# Dizains aplikācijai.
tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue") 

root = tk.CTk()
root.title('Password generator')
root.geometry("1200x600")

tabview = tk.CTkTabview(root) # Tiek izveidoti tabi.
tabview.pack(padx=20, pady=10, fill="both", expand=True) # Tiek piešķirtas īpašības objektam dizainā.

tab_1 = tabview.add("Generate password") # Tiek izveidots tab.
tab_2 = tabview.add("Saved passwords") 
tabview.set("Generate password") # Tiek norādīts, ka šis tabs būs pirmais, kuru atversies, kad programma tiek palaista.

entry = tk.CTkEntry(tab_1, placeholder_text="Login", width=1000)# Tiek izveidots input lodziņš.
entry.pack(pady=40) # Tiek piešķirtas īpašības objektam dizainā.

checkbox1 = tk.CTkCheckBox(tab_1, text="Caps", width=900,) 
checkbox1.pack(pady=30) 

checkbox2 = tk.CTkCheckBox(tab_1, text="Symbol", width=900)
checkbox2.pack(pady=30)

checkbox3 = tk.CTkCheckBox(tab_1, text="Numbers", width=900) 
checkbox3.pack(pady=30)

entry2 = tk.CTkEntry(tab_1, placeholder_text="Password length", width=1000)
entry2.pack(pady=40) 

button = tk.CTkButton(tab_1, text="Generate password", font=('', 20), width=1000, height=50, command=generate_password) # Tiek izveidota poga, kura aizsūta visas vērtības uz funkciju generate_password.
button.pack(pady=20, padx=30)

Button2= tk.CTkButton(tab_2, text="Show Data", font=('', 20), width=900, height=200, command=showpass) # Tiek izveidota poga, kura aizsūta visas vērtības uz funkciju showpass.
Button2.pack(pady=200, padx=30)

root.mainloop()# Tiek palaista koda daļa, kur attiecas uz GUI.
