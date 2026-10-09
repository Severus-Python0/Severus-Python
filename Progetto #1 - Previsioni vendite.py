


import pandas as pd
import numpy as np


dati = {
    "Data" : ["2023 -08-01", None, "2023-07 -13", None, "2023   -12-01"],
    "Prodotto" : ["Tiragra ffi", None, "PETTine", "Cr occheTTe", "AntiPULCI"],
    "Vendite" : [100, 121, 20, None, 100],
    "Prezzo" : [40.00, 15.00, 12.00, 45.00, 70.00],
    }

df = pd.DataFrame(dati)

# sistemazione valori di Prodotto #

df["Prodotto"] = df["Prodotto"].map(lambda x : x.replace(' ', '').capitalize() if pd.notnull(x) else x)


# sistemazione valori mancanti #

df["Vendite"] = df["Vendite"].fillna(df["Vendite"].mean())
df["Prodotto"] = df["Prodotto"].fillna("Sconosciuto")


# conversione di Data in DateTime #


df["Data"] = df["Data"].map(lambda x : x.replace(' ', '') if pd.notnull(x) else x)
df["Data"] = pd.to_datetime(df["Data"])


# calcolare le vendite totali per prodotto #
 

vendite_totali = df.groupby(df["Prodotto"])["Vendite"].sum()
print(vendite_totali)



# individuare il prodotto più venduto e quello meno venduto # 

vendite_totali_max = vendite_totali.max()
vendite_totali_min = vendite_totali.min()
vendite_totali_max_nome = vendite_totali.idxmax()
vendite_totali_min_nome = vendite_totali.idxmin()

print(vendite_totali_max)
print(vendite_totali_min)
print(vendite_totali_max_nome)
print(vendite_totali_min_nome)


# Calcolare vendite medie giornaliere #

vendite_giornaliere = df.groupby(df["Data"])["Vendite"].sum()
vendite_medie_giornaliere = vendite_giornaliere.mean()
print(vendite_medie_giornaliere)



print(df.head())
df.info()
print(df.describe())


