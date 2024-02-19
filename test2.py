import requests #Tiek importēta bibliotēka lai varētu izmantot api
import customtkinter as tk #Tiek importēta bibliotēka ar kuras palīdzību tike veidots savienojums ar datu bāzi

class Password_gen():# Definēta klase Passwrod_gen
    def __init__(self, caps, num, sim, char):# definēti argumenti klases sākuma
        self.caps = caps # mainigais kuram ir noteikta vērība
        self.num = num # mainigais kuram ir noteikta vērība
        self.sim = sim # mainigais kuram ir noteikta vērība
        self.char = char # mainigais kuram ir noteikta vērība
        self.generated_password = None #tukš mainigais

    def Pass_gen(self): #Definēta funkcija kurā notiek paroles ģenerēšana
        url = f"https://www.psswrd.net/api/v1/password/?length={self.char}&lower=0&upper={self.caps}&int={self.num}&special={self.sim}" #Mainīgais kura ir url uz api kurš ģenerē paroli
        response = requests.get(url) # mainigais kurš kurā glabajas dati no api
        self.generated_password = response.text #Mainigais no funkcijas __init__ kurā glabājas info no api str formāta

def frame(generated_password, log): # tiek izveoidota funkcija kurai ir nefieciešamas veribas  generated_password, log
    tk.set_appearance_mode("dark") #tiek norādīta galvēnā krāsa prieš gui
    tk.set_default_color_theme("dark-blue") #tiek norādīta otra krāsa prieš gui

    root2 = tk.CTk() # manigais kura glaabājas tk.CTk()
    root2.title('Password')# tiek pieškirts nosaukums logam
    root2.geometry("400x200") #tiek norādīts izmērs logam
    
    labvl2 = tk.CTkLabel(root2,text=log,font=('',22)) #tiek izveidots teks kura tiek parādita informācija no loga login
    labvl2.pack(pady= 30) # tiek norādītas īpašības priekšobjecta dizaina

    labvl = tk.CTkLabel(root2,text=generated_password,font=('',22)) #tiek izveidots teks (parole)
    labvl.pack(pady= 30)# tiek norādītas īpašības priekšobjecta dizaina

    root2.mainloop() #palaiž gui šaja funkcija 

def generate_password():
    caps = "1" if checkbox1.get() else "0" #tiek saņemta vieniba no checkbox kur ja vienība 1 tad tā bus vienada ar mainīgo else ši vienība būs 0
    sim = "1" if checkbox2.get() else "0" #tiek saņemta vieniba no checkbox kur ja vienība 1 tad tā bus vienada ar mainīgo else ši vienība būs 0
    num = "1" if checkbox3.get() else "0" #tiek saņemta vieniba no checkbox kur ja vienība 1 tad tā bus vienada ar mainīgo else ši vienība būs 0
    char = entry2.get() #tiek saņemta informācija no input lodziņiem gui
    log = entry.get() #tiek saņemta informācija no input lodziņiem gui

    password_generator = Password_gen(caps, num, sim, char) #mainigais kurāt tiek ievaditi dati priekš klases objektiem
    password_generator.Pass_gen() # šeit tiek ģenerēta un glabāta parole
    print(password_generator.generated_password) # šet ir dota pieeja pie ģenerētas paroles
    generated_password = password_generator.generated_password # tiek izveidots mainigais kura tiek glabāta parole
    frame(generated_password, log) #maniegie no šis funkcijas ir savienoti ar funkciju frame



#dizains aplikācijai
tk.set_appearance_mode("dark") #tiek norādīta galvēnā krāsa prieš gui
tk.set_default_color_theme("dark-blue")  #tiek norādīta otra krāsa prieš gui

root = tk.CTk()# manigais kura glaabājas tk.CTk()
root.title('Password generator') # tiek pieškirts nosaukums logam
root.geometry("1200x600") #tiek norādīts izmērs logam

tabview = tk.CTkTabview(root) # tiek izveidoti tab 
tabview.pack(padx=20, pady=10, fill="both", expand=True) # tiek pieškirtas īpašibas objetam dizaina

tab_1 = tabview.add("Generate password") # tiek izveidoti tabi
tab_2 = tabview.add("Saved passwords") # tiek izveidoti tabi
tabview.set("Generate password") # tiek norādits ka šis tab bus pirmais kuru atversies kad programa tiek palaista

entry = tk.CTkEntry(tab_1, placeholder_text="Login", width=1000)# tiek izveidots input lodziņš
entry.pack(pady=40) # tiek pieškirtas īpašibas objetam dizaina

checkbox1 = tk.CTkCheckBox(tab_1, text="Caps", width=900,) # tiek izvedots checkbox
checkbox1.pack(pady=30) # tiek pieškirtas īpašibas objetam dizaina

checkbox2 = tk.CTkCheckBox(tab_1, text="Symbol", width=900) # tiek izvedots checkbox
checkbox2.pack(pady=30) # tiek pieškirtas īpašibas objetam dizaina 

checkbox3 = tk.CTkCheckBox(tab_1, text="Numbers", width=900) # tiek izvedots checkbox
checkbox3.pack(pady=30) # tiek pieškirtas īpašibas objetam dizaina 

entry2 = tk.CTkEntry(tab_1, placeholder_text="Password length", width=1000) # tiek izveidots input lodziņš
entry2.pack(pady=40) # tiek pieškirtas īpašibas objetam dizaina 

button = tk.CTkButton(tab_1, text="Generate password", font=('', 20), width=1000, height=50, command=generate_password) #tiek izveidota poga kura aizsūta visas vērtības uz funkciju generate_password
button.pack(pady=20, padx=30) # tiek pieškirtas īpašibas objetam dizaina

root.mainloop()#tiek palaista koda daļa kur atiecas uz gui
