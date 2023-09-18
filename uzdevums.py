import PySimpleGUI as psg

#minimalas prasības
class info():
    def __init__(self,veids, modelis, cena):
        self.veids = veids
        self.modelis = modelis
        self.cena = cena

    def apskate(self):
        print(self.modelis)
        print(self.cena)
        print(self.veids)

    def laboshana(self, veids, modelis,cena,):
        self.veids = veids
        self.modelis = modelis
        self.cena = cena

    
    
    
    def save(self):
        with open('info.txt','w', encoding="utf=8") as fails:
            fails.write("-Personālā datora sastāvdaļa-\n")
            fails.write(f"Veids: {self.veids}\n")
            fails.write(f"modelis: {self.modelis}\n")
            fails.write(f"Cena: {self.cena} EUR\n")


psg.theme('darkamber')
layout = [
            [psg.Text('Komponentes')],
            [psg.Text('Veids'),psg.InputText()],    
            [psg.Text('Modelis'),psg.InputText()],
            [psg.Text('Cena'),psg.InputText()],
            [psg.Button('submit')]
            
          ]

layout2 = [
    
        [psg.Text('Redigēšana')],
        [psg.Text('Veids'),psg.InputText()],
        [psg.Text('Modelis'),psg.InputText()],
        [psg.Text('Cena'),psg.InputText()],
        [psg.Button('Rediģēt')]        

    
    
    ]

tabgrp = [[
    psg.TabGroup(
        [
            [
                psg.Tab('Datu ievade', layout),
                psg.Tab('Datu redigēšana', layout2)
            
            ]
        ]
    ),
    psg.Button('Aizvērt')
    
    
]]

window = psg.Window('Datora komponentes', tabgrp)

while True:
    event,values = window.read() #Nolasa ievadītās vērtības un darbības
    #Apgalvojumi
    if event in (psg.WIN_CLOSED,'Aizvērt'):
    
        break


    
    if event in (psg, 'submit'):
        jauns = info(values[0],values[1],values[2])
        jauns.apskate()
        jauns.save()
        
    
    if event == "Rediģēt":
        veids = values[0]
        modelis = values[1]
        cena = values[2]
        jauns.laboshana(veids,modelis,cena)
        jauns.save()

window.close()