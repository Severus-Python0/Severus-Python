


titolo = "Qualcuno volò sul nido del cuculo"
copie = 40
prezzo_medio = 15.80
stato = True

print(f"{titolo}, {copie}, {prezzo_medio}, {stato}")


lista_libri = ["Qualcuno volò sul nido del cuculo", "Abracabra", "Rivoluzione russa", "Moby Dick", "La porta di Coraline"]


lib = {"Qualcuno volò sul nido del cuculo" : 30,
       "Abracabra" : 20,
       "Rivoluzione russa" : 30,
       "Moby Dick" : 40,
       "La porta di Coraline" : 10}


utenti_registrati = {"Cesare", "Paolo", "Damiano", "Luca", "Pio"}


class Libro:
    def __init__(self, titolo, autore, anno, copie_disponibili):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.copie_disponibili = copie_disponibili

    def info(self):
        return f"Il libro è {self.titolo}, scritto da {self.autore}, nell'anno {self.anno}. Le copie disponibili sono: {self.copie_disponibili}"
        
libro = Libro("Un aereo super pazzo", "Cesare D'Agostino", 1970, 40)

print(libro.info())


class Utente:
    def __init__(self, nome, eta, id_utente):
        self.nome = nome
        self.eta = eta
        self.id_utente = id_utente

    def scheda(self):
        print (f"{self.nome}, {self.eta}, {self.id_utente}")

utente = Utente("Willy", 30, "willy_idfalco")

utente.scheda()

class Prestito:
    def __init__(self, utente, libro, giorni):
        self.utente = utente
        self.libro = libro
        self.giorni = giorni

    def dettagli(self):
        print (f"{self.utente}, {self.libro}, {self.giorni}")

libro = Libro("Moby Dick", "Herman Melville", 1970, 40)
utente = Utente("Mirko", 45, "mi_rko_45")
p = Prestito(utente, libro , 4)

p.dettagli()

def presta_libro(utente, libro, giorni):
    if libro.copie_disponibili >= 1:
        libro.copie_disponibili -= 1
        prestito = Prestito(utente, libro, giorni)
        return prestito
    else:
        print("Libro non disponibile in giacenze")
        return None
    
l1 = Libro("Caccia a Ottobre Rosso", "Tom Clancy", 1984, 33)
l2 = Libro("Fuga da Alcatraz", " J. Campbell Bruce", 1963, 50)
l3 = Libro("Abracadabra", "Mago Othelma", 1998, 50)

u1 = Utente("Phil", 34, "phil_34.id")
u2 = Utente("Jean-Claude", 65, "jeanclaude_65.id")

prestal1 = presta_libro(u1, l1, 14)
prestal2 = presta_libro(u2, l2, 21)
prestal3 = presta_libro(u2, l3 , 40)

prestiti_effettuati =[]
if prestal1:
    prestiti_effettuati.append(prestal1)

if prestal2:
    prestiti_effettuati.append(prestal2)

if prestal3:
    prestiti_effettuati.append(prestal3)

print(l1.copie_disponibili)
print(l1.titolo)

print(l2.copie_disponibili)
print(l2.titolo)

print(l3.copie_disponibili)
print(l3.titolo)






            


























       
       
 





