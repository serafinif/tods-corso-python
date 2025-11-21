# 🏠 DataHouse – Analisi del Mercato Immobiliare (King County)

Progetto finale del corso **Python Base**  

---

## 🎯 Obiettivo
Analizzare i dati immobiliari di King County (Seattle, USA)  
per estrarre statistiche, generare visualizzazioni e creare un report JSON riassuntivo.

---

## 📁 Struttura della repo

```bash
datahouse/
│
├── data/
│ └── Housing.csv # Dataset originale
│
├── src/
│ ├── main.py # Script principale
│ ├── models.py # Classi: Immobile, Annuncio, ecc.
│ ├── utils_io.py # Lettura/scrittura file CSV/JSON
│ ├── analysis.py # Analisi e statistiche
│ ├── viz.py # Grafici e visualizzazioni
│ └── init.py
│
├── output/
│ ├── report.json # Report finale
│ ├── grafici/ # Cartella per grafici salvati
│ └── logs/ # File di log
│
├── README.md
├── pyproject.toml
└── .gitignore
```


---

## ⚙️ Setup ambiente

1️⃣ Inizializza progetto poetry:
```bash
poetry init

This command will guide you through creating your pyproject.toml config.

Package name [datahouse]:  
Version [0.1.0]:  
Description []:  Esercizio finale riepilogativo
Author [None, n to skip]:  Nome Cognome
License []:  
Compatible Python versions [>=3.12]:  

Would you like to define your main dependencies interactively? (yes/no) [yes] 
        You can specify a package in the following forms:
          - A single name (requests): this will search for matches on PyPI
          - A name and a constraint (requests@^2.23.0)
          - A git url (git+https://github.com/python-poetry/poetry.git)
          - A git url with a revision         (git+https://github.com/python-poetry/poetry.git#develop)
          - A file path (../my-package/my-package.whl)
          - A directory (../my-package/)
          - A url (https://example.com/packages/my-package-0.1.0.tar.gz)
        
Package to add or search for (leave blank to skip): pandas@^2.2.0       
Adding pandas@^2.2.0

Add a package (leave blank to skip): numpy@^1.26.0
Adding numpy@^1.26.0

Add a package (leave blank to skip): matplotlib@^3.8.0
Adding matplotlib@^3.8.0

Add a package (leave blank to skip): seaborn@0.13.0
Adding seaborn@0.13.0

Add a package (leave blank to skip): request@^2.31.0
Adding request@^2.31.0

Add a package (leave blank to skip): 

Would you like to define your development dependencies interactively? (yes/no) [yes] no
Generated file
```

2️⃣ Installa le dipendenze:
```bash
poetry install
poetry lock
```
3️⃣ Entra nell’ambiente virtuale:
```bash
poetry env activate
```
se il kernel non dovesse essere disponibile seguire le istruzione del modulo 1 per leggerlo forzatamente.

## ▶️ Esecuzione

Lancia il programma principale:
```bash
poetry run python3 src/main.py
```

Output attesi:
- `output/report.json` → statistiche aggregate
- `output/grafici/*.png` → grafici Seaborn
- `output/logs/app.log` → log dettagliato

## 📊 Dataset

Usa il dataset **King County House Sales** (formato CSV),
contenente oltre 20.000 case con colonne come:
- `price`, `bedrooms`, `bathrooms`, `sqft_living`, `floors`, `view`, `condition`, `grade`, `zipcode`, `ecc`.

## 🧠 Analisi principali

- Prezzo medio per zona (zipcode)
- Prezzo medio per numero camere
- Distribuzione prezzo per vista mare
- Condizione media per grade
- Percentuale case moderne (post-2000)
- Heatmap correlazioni numeriche

## 🎨 Grafici prodotti

| File                      | Descrizione                |
| ------------------------- | -------------------------- |
| `hist_price.png`          | Distribuzione prezzi       |
| `price_by_bedrooms.png`   | Prezzo medio per camere    |
| `price_by_waterfront.png` | Prezzo per vista mare      |
| `correlation_heatmap.png` | Correlazioni tra variabili |

