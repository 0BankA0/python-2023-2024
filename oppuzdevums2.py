import PySimpleGUI as sg



class noma():
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
    def produktu_info(self):
        pass
    
    
    def save(self):
        with open('info2.txt','w', encoding="utf=8") as fails:
            fails.write('noma')
            fails.write(self.Produkta_kategorija)
            fails.write(self.Produkta_nosaukums)
            fails.write(self.Tehniskie_raksturojumi)
            fails.write(self.Nomas_cena_diena)
            fails.write(self.Produkts_pieejams)
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
        [sg.Radio('Jā', "RADIO", default=True), sg.Radio('Nē', "RADIO", default=False)]
]

layout2 = [
    [sg.Text('ievadi nomnieka informāciju')],
    [sg.Text('Vārds'),sg.InputText()],
    [sg.Text('Uzvārds'),sg.InputText()],
    [sg.Text('Personas kods'),sg.InputText()],
    [sg.Text('Telefona numurs'),sg.InputText()],
    [sg.Text('Nomas sākuma datums'),sg.InputText()],
    [sg.Text('Nomas beigu datums'),sg.InputText()],

    


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
    print(values[0])
    
    #if event in (sg, 'ok'):
    #    save = noma(values[0],values[2],values[3],values[4],values[5])
    #    save.save()

window.close()