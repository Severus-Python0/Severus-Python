

import numpy as np

nome1 = "Aldo"
cognome1 = "Baglio"
codice_fiscale1 = "ADBGL9485503HF"
eta1 = 60
peso1 = 80.5
analisi1 = ["emocromo", "emoglobina", "ferro"]


nome2 = "Giovanni"
cognome2 = "Storti"
codice_fiscale2 = "GVNNST9485503HF"
eta2 = 61
peso2 = 75.5
analisi2 = ["emocromo", "tiroide", "ferro"]

nome3 = "Giacomo"
cognome3 = "Poretti"
codice_fiscale3 = "GCMPRTT09485503HF"
eta3 = 62
peso3 = 76.5
analisi3 = ["globuli rossi", "colesterolo", "ferro"]


class Paziente:
    def __init__(self, nome, cognome, codice_fiscale, eta, peso, analisi_effettuate, risultati_analisi):
        self.nome = nome
        self.cognome = cognome
        self.codice_fiscale = codice_fiscale
        self.eta = eta
        self.peso = peso
        self.analisi_effettuate = analisi_effettuate
        self.risultati_analisi = np.array(risultati_analisi)

    def statistiche_analisi(self):
        return (f"Risultati analisi: {np.mean(self.risultati_analisi)}, {np.max(self.risultati_analisi)}, {np.min(self.risultati_analisi)}, {np.std(self.risultati_analisi)}")
        
    
    def scheda_personale(self):
        return (f"Dati principali del paziente: {self.nome}, {self.cognome}, {self.codice_fiscale}, {self.eta}, {self.peso}, {self.analisi_effettuate}")


class Medico:
    def __init__(self, nome, cognome, specializzazione):
        self.nome = nome
        self.cognome = cognome
        self.specializzazione = specializzazione
    
    def visita_paziente(self, paziente):
        print (f"Il medico {self.nome}, {self.cognome}, sta visitando il paziente {paziente.nome}, {paziente.cognome}")


class Analisi:
    def __init__(self, tipo_analisi, risultati):
        self.tipo_analisi = tipo_analisi
        self.risultati = risultati
    
    def valuta(self):
        if self.risultati > 70 and self.risultati < 100:
            return ("I valori sono nella norma")
        else:
            return "Attenzione i valori non sono nella norma"
        

valore_esami = np.array([50, 55, 67, 70, 73, 80, 91, 92, 95, 100])

media = np.mean(valore_esami)
print(media)

valore_massimo = np.max(valore_esami)
print(valore_massimo)

valore_minimo = np.min(valore_esami)
print(valore_minimo)

deviazione_standard = np.std(valore_esami)
print(deviazione_standard)



if __name__ == "__main__":
    m1 = Medico("Alfio", "Guglia", "Cardiochirurgo")
    m2 = Medico("Oscar", "Trunviu", "Psicologo")
    m3 = Medico("Renzo", "Frumu", "Dermatologo")

    p1 = Paziente("Andrea", "Barba", "ANDRBRB98765432", 18, 75.00, ["Emocromo", "Emoglobina", "Colesterolo"], [70, 70, 100])
    print(p1.scheda_personale())
    print(p1.statistiche_analisi())
    m1.visita_paziente(p1)
    
    p2 = Paziente("Antonio", "Berba", "ANTBERB0987654", 20, 78.00, ["Emocromo", "Piastrine", "Colesterolo"], [70, 56, 90])
    print(p2.scheda_personale())
    print(p2.statistiche_analisi())
    m2.visita_paziente(p2)

    p3 = Paziente("Antonio", "Fuksas", "ANTFKS0987654", 21, 79.00, ["Emocromo", "Piastrine", "Colesterolo"], [72, 58, 99])
    print(p3.scheda_personale())
    print(p3.statistiche_analisi())
    m1.visita_paziente(p3)

    p4 = Paziente("Ansimo", "Birba", "ANSBIRB0987654", 20, 78.00, ["Emocromo", "Piastrine", "Colesterolo"], [74, 58, 93])
    print(p4.scheda_personale())
    print(p4.statistiche_analisi())
    m3.visita_paziente(p4)

    p5 = Paziente("Augusto", "Burbino", "AGSTBRBB0987654", 21, 79.00, ["Emocromo", "Piastrine", "Colesterolo"], [79, 60, 91])
    print(p5.scheda_personale())
    print(p5.statistiche_analisi())
    m3.visita_paziente(p5)






                
            
