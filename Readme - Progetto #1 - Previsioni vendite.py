# Progetto #1 – Previsioni vendite

## Descrizione

Questo progetto Python analizza un piccolo dataset di vendite storiche utilizzando Pandas.

L’obiettivo è esercitarsi nelle principali operazioni di pulizia, trasformazione e analisi dei dati, partendo da un dataset contenente valori mancanti e formati non uniformi.

---

## Funzionalità implementate

### Parte 1 – Creazione ed esplorazione del dataset

Il DataFrame contiene le colonne:

- Data
- Prodotto
- Vendite
- Prezzo

Per l’esplorazione vengono utilizzati:

- `head()`
- `info()`
- `describe()`

---

### Parte 2 – Pulizia dei dati

Sono state gestite diverse situazioni:

- pulizia dei nomi dei prodotti;
- rimozione degli spazi non necessari;
- uniformazione delle stringhe;
- sostituzione dei prodotti mancanti con `Sconosciuto`;
- sostituzione dei valori mancanti di `Vendite` con la media della colonna.

---

### Parte 3 – Gestione delle date

La colonna `Data` viene ripulita dagli spazi e successivamente convertita in formato datetime tramite Pandas.

I valori di data mancanti vengono rappresentati come `NaT`.

---

### Parte 4 – Analisi delle vendite per prodotto

Le vendite vengono raggruppate per prodotto tramite `groupby()`.

Il progetto calcola:

- vendite totali per prodotto;
- valore massimo delle vendite;
- valore minimo delle vendite;
- prodotto più venduto;
- prodotto meno venduto.

---

### Parte 5 – Vendite medie giornaliere

Le vendite vengono raggruppate per data e sommate.

Successivamente viene calcolata la media delle vendite giornaliere considerando le righe con una data valida.

---

## Concetti utilizzati

- DataFrame
- valori mancanti
- `fillna()`
- `mean()`
- `map()`
- funzioni `lambda`
- pulizia delle stringhe
- `pd.to_datetime()`
- `groupby()`
- `sum()`
- `max()` e `min()`
- `idxmax()` e `idxmin()`
- `head()`, `info()` e `describe()`

---

## Tecnologie utilizzate

- Python 3
- Pandas

---

## File principale

`Progetto #1 - Previsioni vendite.py`

---

## Obiettivo didattico

Il progetto è stato sviluppato per consolidare l’utilizzo di Pandas nella pulizia, trasformazione e analisi di un dataset, con particolare attenzione alla gestione dei valori mancanti, delle date e delle aggregazioni.

---

## Autore

Cesare D’Agostino

Progetto sviluppato durante il percorso EPICODE in Python, Data Science e Data Analysis.
