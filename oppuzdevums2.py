import PySimpleGUI as sg



class Noma():
    def __init__(self, Produkta_kategorija, Produkta_nosaukums, Tehniskie_raksturojumi, Nomas_cena_diena, Produkts_pieejams, Nomnieks_vards, Nomnieks_uzvards, Nomnieks_pk,Nomnieks_tel_numurs, Nomas_sakuma_datums, Nomas_beigu_datums):
        self.Produkta_kategorija = Produkta_kategorija
        self.Produkta_nosaukums = Produkta_nosaukums
        self.Tehniskie_raksturojumi = Tehniskie_raksturojumi
        self.Nomas_cena_diena = Nomas_cena_diena
        self.Produkts_pieejams = Produkts_pieejams
        self.Nomnieks_vards = Nomnieks_vards
        self.Nomnieks_uzvards = Nomnieks_uzvards
        self.Nomnieks_pk = Nomnieks_pk
        self.Nomnieks_tel_numurs = Nomnieks_tel_numurs
        self.Nomas_sakuma_datums = Nomas_sakuma_datums
        self.Nomas_beigu_datums = Nomas_beigu_datums
    
    def apskate(self):
        print(self.Produkta_kategorija)
        print(self.Produkta_nosaukums)
        print(self.Tehniskie_raksturojumi)
        print(self.Nomas_cena_diena)
        print(self.Produkts_pieejams)
        print(self.Nomnieks_vards)
        print(self.Nomnieks_uzvards)
        print(self.Nomnieks_pk)
        print(self.Nomnieks_tel_numurs)
        print(self.Nomas_sakuma_datums)
        print(self.Nomas_beigu_datums)
        

    def Produkta_info(self):
        with open('Nomnieks_info.txt','w', encoding="utf=8") as fails:
            fails.write('noma')
            fails.write(self.Produkta_kategorija)
            fails.write(self.Produkta_nosaukums)
            fails.write(self.Tehniskie_raksturojumi)
            fails.write(self.Nomas_cena_diena)
            fails.write(self.Produkts_pieejams)

    def Nomnieks_info(self):
        with open('Nomnieks_info.txt','w', encoding="utf=8") as fails:
            fails.write(self.Nomnieks_vards)
            fails.write(self.Nomnieks_uzvards)
            fails.write(self.Nomnieks_pk)
            fails.write(self.Nomnieks_tel_numurs)
            fails.write(self.Nomas_sakuma_datums)
            fails.write(self.Nomas_beigu_datums)
sg.theme('dark')


layout = [ 
        [sg.Text('ievadi produkta informaciju')],
        [sg.Text('Produkta kategorija'), sg.InputText()],
        [sg.Text('Produkta nosaukums'), sg.InputText()],
        [sg.Text('Produkta raksturojums'), sg.InputText()],
        [sg.Text('nomas cena diean'), sg.InputText()],
        [sg.Text('Vai produkts ir pieejams?')],
        [sg.Text('Jā/Nē'), sg.InputText()]
        
]

layout2 = [
    [sg.Text('ievadi nomnieka informāciju')],
    [sg.Text('Vārds'),sg.InputText()],
    [sg.Text('Uzvārds'),sg.InputText()],
    [sg.Text('Personas kods'),sg.InputText()],
    [sg.Text('Telefona numurs'),sg.InputText()],
    [sg.Text('Nomas sākuma datums'),sg.InputText()],
    [sg.Text('Nomas beigu datums'),sg.InputText()]
    

    


]

tabgrup = [
    [
    sg.TabGroup(
        [   
            [
                sg.Tab('Produkta info', layout),
                sg.Tab('Nomnieka info', layout2)
                
            ]
            
        ]
        
    )],
    [sg.Button('Ok'), sg.Button('Cancel')]

]


window = sg.Window('Noma', tabgrup)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': 
        break
    if event in (sg,'Ok'):
        print(values[0],values[1],values[2],values[4],values[5],values[6],values[7],values[8],values[9],values[10],values[11])
        

window.close()