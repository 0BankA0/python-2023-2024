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

    def laboshana(self, veids, modelis,cena):
        self.veids = veids
        self.modelis = modelis
        self.cena = cena
    def save(self):
        with open('info.txt','W', encoding="utf=8") as fails:
            fails.write("-personala datora sastavdala-\n")
            fails.write(f"Veids: {self.veids}\n")
            fails.write(f"modelis: {self.modelis}\n")
            fails.write(f"Cena: {self.cena} EUR\n")

jauns = info("RAM", 'Corsair Vengeance LPX 16GB',99.99)
jauns.apskate()
jauns.save()


psg.theme('darkamber')
layout = [
            [psg.Text('Komponentes')]
            [psg.Text('Veids')]
          
          ]

layout2 = [[psg.Text('Redigešana')]]

tabgrp = [
    psg.TabGroup(
        [
            [
                psg.Tab('Datu ievade')
            ]
        ]
    )
]