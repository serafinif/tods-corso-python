# 🐍 Programma del Corso Introduttivo di Python – 2025

**Durata:** 40 ore (10 moduli da 4 ore)

<p align="center">
  <img src="SDG Group - Logo.png" alt="SDG Group" width="120"/>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="tods.png" alt="Tod's" width="120"/>
</p>

---

## 🎯 Obiettivi del corso

Il corso si propone di introdurre i partecipanti al linguaggio **Python** e al suo ecosistema, fornendo solide basi teoriche e pratiche per lo sviluppo di programmi e piccoli progetti.

Al termine, gli studenti saranno in grado di:

- Installare e configurare un ambiente di sviluppo moderno (Python, WSL, VS Code, Git, Poetry).
- Comprendere i concetti fondamentali di programmazione con Python.
- Utilizzare strutture dati, funzioni, file e pacchetti.
- Gestire progetti con Git e Poetry.
- Applicare la programmazione a oggetti.

> 💡 **Curiosità – Storia di Python:**  
> Python è nato nel 1989 grazie a **Guido van Rossum** nei laboratori del **CWI** in Olanda.  
> Il nome deriva dal gruppo comico britannico *Monty Python* e non dal serpente.

---

## 📘 Programma dettagliato

### 🧩 Modulo 1 – Setup & Introduzione
- Breve storia di **Python** e filosofia dello Zen of Python.  
- Installazione di **Visual Studio Code**
- Installazione di **Ubuntu**
- Intallazione di Python con **WSL** (Ubuntu)
- Installazione **Poetry** e gestione dipendenze
- Configurazione iniziale di VS Code
- Git e GitHub:
  - `init`, `clone`, `commit`, `push`, `pull`.
  - `branch`, `merge`, conflitti, pull request.
- Gestione dipendenze con **Poetry**.  
- Creazione di un progetto con struttura standard (`src/`, `tests/`).  
- Primo programma: `hello.py`.
- Esercizio riepilogativo

---

### 🧮 Modulo 2 – Fondamenti di Python
- Variabili e tipi di dato primitivi (`int`, `float`, `str`, `bool`).  
- Conversioni di tipo.
- **Input/output** e **formattazione stringhe**.  
- **Operatori** aritmetici, logici e di confronto.  
- Tipi di **mutabili vs immutabili**.

**🧠 Esercizi pratici**
1. Calcolatrice base. 
2. Conversione Celsius → Fahrenheit.  
3. In che anno compirai 100 anni?
4. Calcolo del costo medio giornaliero.
5. Valutazione del budget personale.
6. Tipi mutabili e immutabili.
7. Formattazione di output con stile. 

---

### 🔁 Modulo 3 – Strutture di controllo
- Condizioni: `if`, `elif`, `else`.  
- Cicli: `for`, `while`.  
- Istruzioni speciali: `break`, `continue`, `pass`.  
- Funzioni built-in utili: `range()`, `enumerate()`, `zip()`.

**🧠 Esercizi pratici**
1. Gioco "Indovina il numero".
2. Calcolare la somma delle cifre di un numero.
3. FizzBuzz.
4. Caccia al numero segreto 2.0 (limite di tentativi).
5. Conta parole.
6. Il primo numero di Fibonacci maggiore di N.

---

### 📦 Modulo 4 – Strutture dati
- **Liste**, **tuple**, **set** e **dizionari**.  
- Metodi principali e operazioni comuni.  
- **Slicing**, **unpacking** e **copy** (shallow vs deep).
- Saper sceglire quando usare ciascuna struttura.
- Comprehension rapide (bonus)
- Funzioni **lambda**

**🧠 Esercizi pratici**
1. Rubrica telefonica con dizionari.
2. Parole uniche in una frase.
3. Ordinare una lista e trovare massimo/minimo.
4. Analisi di un sondaggio.
5. Prezzi in sconto (liste, tuple e slicing).
6. Report studenti (dizionari e unpacking).
7. Analisi del testo (set, dict, slicing e copy).
8. Classifica prodotti per prezzo.

---

### 🧭 Modulo 5 – Funzioni
- Definizione e richiamo.  
- Parametri: posizionali, keyword, default, `*args`, `**kwargs`.  
- Scope delle variabili.  
- Documentazione con **docstring** e **hint di tipo**.
- Distinguere tra **funzioni pure** e **con effetti collaterali**.

**🧠 Esercizi pratici**
1. Calcola area cerchio con hint di tipo.
2. Generatore di password casuale.
3. Verifica di una funzione con **assert**.
4. Calcolatrice multi-numero.
5. Convertitore di temperature (C, F, K).
6. Classifica dei film con **lambda** e dizionari.
7. Analizzatore di test flessibile.
8. Simulatore di dadi.

---

### 📂 Modulo 6 – File ed Eccezioni
- Lettura/scrittura file (`txt`, `csv`, `json`).  
- Uso del context manager `with`.  
- Gestione errori con `try/except/finally`. 
- Approfondimento logging con `loguru`. 
- Creazione di eccezioni personalizzate.

**🧠 Esercizi pratici**
1. Media dei voti da CSV.
2. Log parser (conta parole in file).
3. Gestione input errati con `try/except`.
4. Generatore di log di sessione.
5. Classifica studenti da CSV.
6. Gestione di un piccolo budget.
7. Roulette semplificata.

---

### 🧱 Modulo 7 – Moduli e Pacchetti
- Import librerie standard e personalizzate.  
- Creazione moduli (`.py`) e pacchetti (`__init__.py`).
- Capire `__name__ == '__main__'` e `sys.path`.  
- Utilizzo di `requests` e gestione `JSON`.

**🧠 Esercizi pratici**
1. Aggiungi `clamp(x,lo,hi)` a `math_utils`.
2. Scarica TODOs e salva solo i titoli (fallback offline).
3. Rileggi il JSON salvato e stampa i primi 3 titoli.
4. Mini-Progetto: Weather Reporter (pacchetto multi-modulo).

---

### 🧠 Modulo 8 – Programmazione ad Oggetti
- Differenza tra programmazione procedurale e **OOP**.
- **Classi**, **oggetti** e **costruttori** (`__init__`).  
- **Metodi** e **attributi**.  
- **Ereditarietà**, **overriding** e **polimorfismo**.  
- Introduzione a `@dataclass`.

**🧠 Esercizi pratici**
1. Conto Bancario.
2. Timer da cucina.
3. Gestionale di biblioteca con ereditarietà.
4. Simulatore di Pokemon.
5. Distributore automatico di snack.
6. Gestore di animali in un rifugio.

---

### ⚙️ Modulo 9 – Strumenti avanzati
- Comprehension avanzate.  
- `lambda`, `map`, `filter`, `reduce`.  
- Conoscere librerie utili: datetime, pathlib, requests, collections.
- Introduzione a Pandas e Numpy
- Introduzione a Matplotlib e Seaborn

**🧠 Esercizi pratici**
1. Analisi temperatura settimanale.
2. Gestione movimenti bancari con Pandas.
3. Mini data analysis con Numpy.
4. Meteo e statistica mensile.
5. Analisi vendite globali e visualizzazione.

---

### 🧾 Modulo 10 – Prova finale del corso
Sviluppo e presentazione di un mini progetto.

Traccia:

Realizzare un progetto Python completo che analizzi il dataset immobiliare **"House Sales in King County (USA)"**, contenente informazioni su oltre 20.000 case.

---

📄 *Il presente programma è indicativo e potrà essere soggetto a modifiche qualora necessario.*
