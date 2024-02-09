#Atsauce uz api paroles ģeneratoru https://github.com/fawazsullia/password-generator

import requests #Tiek importēta bibliotēka lai varētu izmantot api
import mysql.connector #Tiek importēta bibliotēka ar kuras palīdzību tike veidots savienojums ar datu bāzi
import customtkinter as tk


class Password_gen():# Definēta klase Passwrod_gen
    def __init__(self,caps,num,sim,char): # definēti argumenti klases sākuma
        self.caps = caps # mainigais kuram ir noteikta vērība
        self.num = num #mainigais kuram ir noteikta vērība
        self.sim = sim #mainigais kuram ir noteikta vērība
        self.char = char #mainigais kuram ir noteikta vērība
        self.generated_password = None #tukš mainigais
    
    def Paramentri(self, caps, sim, char, num ):
        self.caps = caps #mainigais kuram ir noteikta vērība
        self. num = num #mainigais kuram ir noteikta vērība
        self. sim = sim #mainigais kuram ir noteikta vērība 
        self. char = char #mainigais kuram ir noteikta vērība 

    def Pass_gen(self): #Definēta funkcija kurā notiek paroles ģenerēšana
        
        url = f"https://passwordinator.onrender.com?{self.num}&{self.sim}&{self.caps}&len={self.char}" #Mainīgais kura ir url uz api kurš ģenerē paroli
        response = requests.get(url) # mainigais kurš kurā glabajas dati no api
        self.generated_password = response.text #Mainigais no funkcijas __init__ kurā glabājas info no api str formāta



# tk.set_appearance_mode("dark")
# tk.set_default_color_theme("dark-blue")

# root = tk.CTk()
# root.title('Password generator')
# root.geometry("1200x600")

# # frame = tk.CTkFrame(master=root)
# # frame.pack(pady=20, padx=25, fill="both", expand=True)

# tabview = tk.CTkTabview(root)
# tabview.pack(padx=20, pady=10 , fill="both", expand=True)

# tab_1= tabview.add("Generate password")  # add tab at the end
# tab_2= tabview.add("Saved passwords")  # add tab at the end
# tabview.set("Generate password")  # set currently visible tab

# #label1 = tk.CTkLabel(tab_1, text='')

# def qwe():
#     print(checkbox1.get())


# entry = tk.CTkEntry(tab_1,placeholder_text="Login", width=1000)
# entry.pack(pady=40)

# checkbox1 = tk.CTkCheckBox(tab_1, text="Caps",width= 900)
# checkbox1.pack(pady = 20, )

# checkbox2 = tk.CTkCheckBox(tab_1, text="Symbol",width= 900)
# checkbox2.pack(pady = 20, )

# checkbox3 = tk.CTkCheckBox(tab_1, text="Numbers",width= 900)
# checkbox3.pack(pady = 20, )

# entry = tk.CTkEntry(tab_1,placeholder_text="Password lenght", width=200)
# entry.place(x=120, y=325)

# Button = tk.CTkButton(tab_1,text='Generate passwor',font=('',20), height=100 ,width=200,command=qwe, variable=checkbox1 , onvalue="on", offvalue="off", )
# Button.pack(pady= 100)



# root.mainloop()

password_generator = Password_gen(num='num=true', sim='char=true',caps= 'caps=true',char=30) #mainigais kurāt tiek ievaditi dati priekš klases objektiem
password_generator.Pass_gen()  # šeit tiek ģenerēta un glabāta parole
print(password_generator.generated_password)  # šet ir dota pieeja pie ģenerētas paroles


 #notiek tas pats kas iepriekš tikai dati tiek aizsūtīti uz funkciju Parametri ne vis uz klasi Password_gen
password_generator.Paramentri(num='num=true', sim='', caps= '',char=15)
password_generator.Pass_gen()
print(password_generator.generated_password)


# # savienojums ar datu bāzi
# db_config = {
#     'host': '127.0.0.1',
#     'user': 'root',
#     'password': '123123',
#     'database': 'password_generation'
# }

# connection = mysql.connector.connect(**db_config)

# cursor = connection.cursor()

# query = "SELECT * FROM user"
# cursor.execute(query)

# result = cursor.fetchall()
# for row in result:
#     print(row)
        

# cursor.close()
# connection.close()


