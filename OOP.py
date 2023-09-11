class Masinas():
    def __init__(self, baakstilpums, pasažieruskaits, motoratilpums, motorajauda):
        self.bakatilpums = baakstilpums
        self.pasažierusjaits = pasažieruskaits
        self.motoratipums = motoratilpums
        self.mtorajauda = motorajauda
audi = Masinas(55, 5, 2, 130)

print(audi.motoratipums)