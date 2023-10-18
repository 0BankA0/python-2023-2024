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
        with open('Remontdarbnica.txt','w',encoding="utf-8") as fails:
            fails.write('=Remontdarbnica=')
            fails.write(f'{self.klienta_vards}\n')
            fails.write(f'{self.klienta_uzvards}\n')
            fails.write(f'{self.telefona_numurs}\n')
            fails.write(f'{self.remontdarbu_cena} EUR\n')
            fails.write(f'{self.telefona_modelis}\n')
            fails.write(f'{self.Telefonam_peiskirtais_numurs}\n')
            fails.write(f'{self.remontdarbu_sakuma_datums}\n')
            fails.write(f'{self.remontdarbu_beigu_datums}\n')
    def Remontdarbu_info_print(self):
        print(self.klienta_vards)
        print(self.klienta_uzvards)
        print(self.telefona_numurs)
        print(f'{self.remontdarbu_cena} EUR')
        print(self.telefona_modelis)
        print(self.Telefonam_peiskirtais_numurs)
        print(self.remontdarbu_sakuma_datums)
        print(self.remontdarbu_beigu_datums)



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
        print(values)
        klienta_vards = values[0]
        klienta_uzvards = values[1]
        telefona_numurs = values[2]
        remontdarbu_cena = values[3]
        telefona_modelis = values[4]
        Telefonam_peiskirtais_numurs = values[5]
        remontdarbu_sakuma_datums = values[6]
        remontdarbu_beigu_datums = values[7]
        save = Remontdarbnica(klienta_vards, klienta_uzvards, telefona_numurs, remontdarbu_cena, telefona_modelis, Telefonam_peiskirtais_numurs, remontdarbu_sakuma_datums, remontdarbu_beigu_datums)
        save.Remontdarbu_info()
        save.Remontdarbu_info_print()
    if event == 'Apskatīt datus':
        ps.theme("Black")
        layout = [
                    [ps.Text("Apskatīt datus")],
                    [ps.Text(klienta_vards)],
                    [ps.Text(klienta_uzvards)],
                    [ps.Text(telefona_numurs)],
                    [ps.Text(remontdarbu_cena)],
                    [ps.Text(telefona_modelis)],
                    [ps.Text(Telefonam_peiskirtais_numurs)],
                    [ps.Text(remontdarbu_sakuma_datums)],
                    [ps.Text(remontdarbu_beigu_datums)],

                ]
        window2 = ps.Window('',layout)
        while True:
            event,values = window2.read()
            if event in (ps.WIN_CLOSED,):
                break
         

window2.close()  
window.close()