#Atsauce uz api paroles ģeneratoru https://github.com/fawazsullia/password-generator

import requests #Tiek importēta bibliotēka lai varētu izmantot api
import json #Tiek importēta json biblieotēka
import PySimpleGUI as sg

def password_gen():
    URL = "https://passwordinator.onrender.com?num=true&char=true&caps=true&len=10" #Mainīgais kura ir url uz api kurš ģenerē paroli

    a = requests.get(URL) #Mainīgais kurā tiek pieprasīti dati no mainīga URL
    dati = a.json() #Mainīgais kurā dati no mainīga a tiek parveidoti json formāta
    print(json.dumps(dati,indent = 2)) # Tiek izvaditi dati konsole no mainigā dati

password_gen()


sg.theme('DarkAmber')
window = sg.Window('Password generator')
layout = [ 
        [sg.Text('test')],
        
]

window.close()


     
