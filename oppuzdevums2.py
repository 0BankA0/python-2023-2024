import PySimpleGUI as ps



class noma():
    def __init__(self, Produkta_kategorija, Produkta_nosaukums, Tehniskie_raksturojumi, Nomas_cena_dienā, Produkts_pieejams, Nomnieks_vārds, Nomnieks_uzvārds, Nomnieks_pk,Nomnieks_tel_numurs, Nomas_sākuma_datums, Nomas_beigu_datums):
        self.Produkta_kategorija = Produkta_kategorija
        self.Produkta_nosaukums = Produkta_nosaukums
        self.Tehniskie_raksturojumi = Tehniskie_raksturojumi
        self.Nomas_cena_dienā = Nomas_cena_dienā
        self.Produkts_pieejams = Produkts_pieejams
        self.Nomnieks_vārds = Nomnieks_vārds
        self.Nomnieks_uzvārds = Nomnieks_uzvārds
        self.Nomnieks_pk = Nomnieks_pk
        self.Nomnieks_tel_numurs = Nomnieks_tel_numurs
        self.Nomas_sākuma_datums = Nomas_sākuma_datums
        self.Nomas_beigu_datums = Nomas_beigu_datums
    def produktu_info(self):
        pass

ps.theme('dark')
layout = [
    [ps.Text('A')]
]



window = ps.Window('Produktu noma', layout)



window.close() 

