
---

# Tecnologie Utilizzate

- Python 3
- NumPy
- Pandas
- Matplotlib

---

# Struttura del Progetto

progetto3/
│
├── progetto3.py
├── prenotazioni_analizzate.csv
└── README.txt

---

# Obiettivi Didattici

Questo progetto è stato sviluppato per:
- consolidare le basi Python,
- applicare OOP a uno scenario reale,
- introdurre la data analysis,
- imparare la visualizzazione dati,
- sviluppare logica progettuale completa.

---

# Possibili Estensioni Future

- database SQLite/MySQL
- interfaccia grafica
- autenticazione utenti
- esportazione PDF report
- dashboard interattive
- API Flask/FastAPI
- integrazione machine learning

---

# Autore

Cesare D’Agostino

Progetto sviluppato durante il percorso di studio Python, AI & Machine Learning.
"""

output_path = "/mnt/data/README_progetto3.txt"

pypandoc.convert_text(
    content,
    'plain',
    format='md',
    outputfile=output_path,
    extra_args=['--standalone']
)

print(f"File creato: {output_path}")
