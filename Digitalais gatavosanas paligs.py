import json

class Recepte:
    def __init__(self, nosaukums, apraksts, sastavdalas, soļi, gatavosanas_laiks):
        self.nosaukums = nosaukums
        self.apraksts = apraksts
        self.sastavdalas = sastavdalas
        self.solu_saraksts = soļi
        self.gatavosanas_laiks = gatavosanas_laiks

    def paradi_recepti(self):
        print(f"Nosaukums: {self.nosaukums}")
        print(f"Apraksts: {self.apraksts}")
        print("Sastāvdaļas:")
        for sastavdala in self.sastavdalas:
            print(f"- {sastavdala}")
        print("Gatavošanas soli:")
        for i, solis in enumerate(self.solu_saraksts, start=1):
            print(f"{i}. {solis}")
        print(f"Gatavošanas laiks: {self.gatavosanas_laiks} minūtes\n")


class DigitalaisEdienaPaligs:
    def __init__(self):
        self.receptes = []

    def ielade_receptes(self, fails="receptes.json"):
        try:
            with open(fails, "r") as fails:
                dati = json.load(fails)
                for receptes_dati in dati["receptes"]:
                    recepte = Recepte(**receptes_dati)
                    self.receptes.append(recepte)
        except FileNotFoundError:
            print(f"Fails {fails} nav atrasts. Nav ielādētas nekādas receptes.")

    def saglabaj_receptes(self, fails="receptes.json"):
        dati = {"receptes": []}
        for recepte in self.receptes:
            receptes_dati = {
                "nosaukums": recepte.nosaukums,
                "apraksts": recepte.apraksts,
                "sastavdalas": recepte.sastavdalas,
                "soļi": recepte.solu_saraksts,
                "gatavosanas_laiks": recepte.gatavosanas_laiks,
            }
            dati["receptes"].append(receptes_dati)

        with open(fails, "w") as fails:
            json.dump(dati, fails, indent=2)
        print(f"Receptes saglabātas failā {fails}.")

    def pievieno_recepti(self, recepte):
        self.receptes.append(recepte)
        print(f"Recepte '{recepte.nosaukums}' veiksmīgi pievienota.")

    def paradi_receptes(self):
        for i, recepte in enumerate(self.receptes, start=1):
            print(f"{i}. {recepte.nosaukums}")

    def iegut_recepti_pa_indeksu(self, indekss):
        try:
            return self.receptes[indekss - 1]
        except IndexError:
            print("Nederīgs receptes indekss.")
            return None


# Piemēra izmantošana:
paligs = DigitalaisEdienaPaligs()
paligs.ielade_receptes()

while True:
    print("\nDigitālais Ēdiena Gatavošanas Palīgs - Izvēlne:")
    print("1. Parādīt Receptes")
    print("2. Pievienot Recepti")
    print("3. Iziet")

    izvele = input("Ievadiet izvēli (1/2/3): ")

    if izvele == "1":
        paligs.paradi_receptes()
        receptes_indekss = int(input("Ievadiet receptes numuru, lai redzētu detalizētu informāciju (0, lai atgrieztos): "))
        if receptes_indekss != 0:
            recepte = paligs.iegut_recepti_pa_indeksu(receptes_indekss)
            if recepte:
                recepte.paradi_recepti()
    elif izvele == "2":
        nosaukums = input("Ievadiet receptes nosaukumu: ")
        apraksts = input("Ievadiet receptes aprakstu: ")
        sastavdalas = input("Ievadiet sastāvdaļas (atslēgas, atdalītas ar komatiem): ").split(", ")
        soli_saraksts = input("Ievadiet gatavošanas soļus (atslēgas, atdalītas ar komatiem): ").split(", ")
        gatavosanas_laiks = int(input("Ievadiet gatavošanas laiku (minūtēs): "))

        jauna_recepte = Recepte(nosaukums, apraksts, sastavdalas, soli_saraksts, gatavosanas_laiks)
        paligs.pievieno_recepti(jauna_recepte)
        paligs.saglabaj_receptes()
    elif izvele == "3":
        print("Iziet no Digitālā Ēdiena Gatavošanas Palīga. Uz redzēšanos!")
        break
    else:
        print("Nederīga izvēle. Lūdzu, ievadiet 1, 2 vai 3.")
