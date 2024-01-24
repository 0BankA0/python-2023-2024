#Atsauce uz api paroles ģeneratoru https://github.com/fawazsullia/password-generator

import requests #Tiek importēta bibliotēka lai varētu izmantot api

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
        
password_generator = Password_gen(num='', sim='char=true',caps= 'caps=true',char=12) #mainigais kurāt tiek ievaditi dati priekš klases objektiem
password_generator.Pass_gen()  # šeit tiek ģenerēta un glabāta parole
print(password_generator.generated_password)  # šet ir dota pieeja pie ģenerētas paroles


#notiek tas pats kas iepriekš tikai dati tiek aizsūtīti uz funkciju Parametri ne vis uz klasi Password_gen
password_generator.Paramentri(num='num=true', sim='', caps= '',char=15)
password_generator.Pass_gen()
print(password_generator.generated_password)




     
