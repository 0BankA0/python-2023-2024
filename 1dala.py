class Csdd:
    def __init__(self, zimols, modelis, registracijas_datums, pilna_masa, degvielas_veids):
        self.zimols = zimols
        self.modelis= modelis
        self.registracijas_datums = registracijas_datums
        self.pilna_masa = pilna_masa
        self.degvielas_veids = degvielas_veids

info = Csdd("Audi",'A4','22.10.2019','1800','BG')

print("Zimols: ",info.zimols)
print("Modelis: ",info.modelis)
print("Reģistrācijas datums:",info.registracijas_datums)
print("Pilna masa: ",info.pilna_masa)
print("Degvielas veids:",info.degvielas_veids)