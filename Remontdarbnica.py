import PySimpleGUI as ps

class Remontdarbnica():
    # Konstruktora izveide
    def __init__(self,klienta_vards,klienta_uzvards, telefona_numurs, remontdarbu_cena, telefona_modelis, Telefonam_peiskirtais_numurs, remontdarbu_sakuma_datums, remontdarbu_beigu_datums):
        self.klienta_vards = klienta_vards
        self.klienta_uzvards = klienta_uzvards
        self.telefona_numurs = telefona_numurs
        self.remontdarbu_cena  =  remontdarbu_cena
        self.telefona_modelis = telefona_modelis
        self.Telefonam_peiskirtais_numurs = Telefonam_peiskirtais_numurs
        self.remontdarbu_sakuma_datums = remontdarbu_sakuma_datums
        self.remontdarbu_beigu_datums = remontdarbu_beigu_datums
    # metodes (work in progress)
    def Remontdarbu_info(self):
        pass
    def Remontdarbu_info_print(self):
        pass

ps.theme('Black')

layout =[

        [ps.Text('Ievadi klienta datus')],
        [ps.Text('Klienta vārds'),ps.InputText()],
        [ps.Text('Klienta uzvārds'),ps.InputText()],
        [ps.Text('Telefona numurs'),ps.InputText()],
        [ps.Text('Remontdarbu cena'),ps.InputText()],
        [ps.Text('Telefona modelis'),ps.InputText()],
        [ps.Text('Telefonam pieškirtais numurs'),ps.InputText()],
        [ps.Text('Remontdarbu sākuma datums'),ps.InputText()],
        [ps.Text('Remontdarbu beigu datums'),ps.InputText()],
        [ps.Button('Apstiprināt'), ps.Button('Apskatīt datus'), ps.Button('Beigt')]
        ]
window = ps.Window('Remontdarbnīca', layout)

while True:
    event,values = window.read()

    if event in (ps.WINDOW_CLOSED,'Beigt'):
        break
    
    # work in progress
    if event == 'Apstiprināt':
        pass
    if event == 'Apskatīt datus':
        pass    

window.close()