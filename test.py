#Klase
#Trīs īpašības: veids, modelis, cena

#Informācijas ievade
#Informācijas apskate
#Informācijas labošana

#Informācijas saglabāšana

#Lietotāja grafiskā saskarne
# #Minimālās prasības
# class Sastavdala():
#     #Konstruktora izveide
#     def __init__(self,veids, modelis, cena):
#         self.veids = veids
#         self.modelis = modelis
#         self.cena = cena
#     #Datu izvade
#     def apskate(self):
#         print(self.veids)
#         print(self.modelis)
#         print(self.cena)
#     #Datu labošana
#     def labosana(self,veids, modelis, cena):
#         self.veids = veids
#         self.modelis = modelis
#         self.cena = cena
# #Jauna objekta izveide    
# jauns = Sastavdala("RAM","Corsair Vengeance LPX 16GB",99.99)
# #Datu nolasīšanas metodes apskate() izsaukšana
# jauns.apskate()
# #Datu labošanas metodes labosana() izsaukšana
# jauns.labosana("GPU","GeForce",75.5)
# #Datu nolasīšanas metodes apskate() izsaukšana
# jauns.apskate()


class Sastavdala():
    #Konstruktora izveide
    def __init__(self,veids, modelis, cena):
        self.veids = veids
        self.modelis = modelis
        self.cena = cena
    #Datu izvade
    def apskate(self):
        print(self.veids)
        print(self.modelis)
        print(self.cena)
    #Datu labošana
    def labosana(self,veids, modelis, cena):
        self.veids = veids
        self.modelis = modelis
        self.cena = cena
    #Datu saglabāšana
    def saglabat(self):
        with open('sastavdalas.txt','w',encoding="utf-8") as fails:
            fails.write(self.modelis)

# jauns = Sastavdala("RAM","Corsair Vengeance LPX 16GB",99.99)
# jauns.apskate()
# jauns.saglabat()

import PySimpleGUI as psg

psg.theme('DarkAmber')
logs = [
          [psg.Text('Komponentes')],
          [psg.Text('Veids'),psg.InputText()],
          [psg.Text('Modelis'),psg.InputText()],
          [psg.Text('Cena'),psg.InputText()],
          [psg.Button('Saglabāt')]
          ]
logs2 = [[psg.Text("Rediģēšana")],
         [psg.Text('Veids'),psg.InputText()],
          [psg.Text('Modelis'),psg.InputText()],
          [psg.Text('Cena'),psg.InputText()],
          [psg.Button('Rediģēt')]]
#Grupēsim divus logus
loguGrupa = [[
    [psg.TabGroup(
        [
            [
                psg.Tab('Datu ievade',logs),
                psg.Tab('Datu rediģēšana',logs2)
            ]
        ]
    )],
    [psg.Button('Aizvērt'),
    psg.Button('Datu apskate')]
]]
window = psg.Window('Datora komponentes', loguGrupa)
#Pārbauda notikumus grafiskajā saskarnē
while True:
    event,values = window.read() #Nolasa ievadītās vērtības un darbības
    #Apgalvojumi
    if event == "Saglabāt":
        print(values) #Dati tiek glabāti vārdnīcā (dictionary), piekļūst, izmantojot atslēgas vērtības
        veids = values[0]
        modelis = values[1]
        cena = values[2]
        jauns = Sastavdala(veids,modelis,cena)
        jauns.saglabat()
    if event == "Rediģēt":
        veids = values[3]
        modelis = values[4]
        cena = values[5]
        jauns.labosana(veids,modelis,cena)
        jauns.saglabat()
    if event == "Datu apskate":
        psg.theme("BlueMono")
        layout = [
                  [psg.Text("Esošās komponentes")],
                  [psg.Text("Veids: " + jauns.veids)],
                  [psg.Text("Modelis: " + jauns.modelis)],
                  [psg.Text("Cena: " + jauns.cena)],
                  [psg.Button("Iziet")]
                  ]
        window2 = psg.Window('',layout)
        while True:
            event,values = window2.read()
            if event == "Iziet":
                break 
        window2.close()
    if event in (psg.WIN_CLOSED,'Aizvērt'):
        break

window.close()