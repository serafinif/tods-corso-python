# 🐉 Pokémon Battle Arena – Progetto finale

Progetto finale del corso **Python Base**

---

## 🎯 Obiettivo

Realizzare un gioco interattivo a turni che simula una battaglia Pokémon a squadre tra il giocatore e il computer.

Il progetto integra:

- gestione del gioco tramite classi e oggetti (ereditarietà e composizione),
- uso di file JSON per leggere i dati dei Pokémon,
- un loop di gioco interattivo con input da tastiera,
- logica di combattimento e aggiornamento dello stato dei Pokémon.

## 🧩 Requisiti didattici

Questo esercizio riassume i principali concetti affrontati nel corso:

- Strutturazione di un progetto in più moduli Python.
- Uso di classi, attributi e metodi.
- Ereditarietà e overriding di metodi.
- Lettura/scrittura di file JSON.
- Gestione di input/output e flusso di controllo.
- Simulazione interattiva con elementi casuali.

---

## 📁 Struttura della repository

```bash
pokemon_battle_arena/
│
├── main.py                # entry point del gioco
│
├── src/
│   ├── pokemon.py         # classi Pokemon e sottoclassi 
│   ├── team.py            # gestione delle squadre (giocatore e CPU)
│   ├── battle.py          # logica della battaglia a turni
│   └── utils.py           # funzioni di utilità (input validato, barra HP, ecc.)
│
├── data/
│   └── pokedex.json       # statistiche base e costi dei Pokémon
│
└── README.md              # questo file
```

--- 

## ⚙️ Setup ambiente

Il Kernel poetry usato durante il corso dovrebbe essere sufficiente per l'esecuzione del pacchetto.

## ▶️ Esecuzione

Lancia il programma principale:
```bash
poetry run python3 main.py
```

---

## 🧠 Come funziona il gioco
**Scelta della squadra**

- Hai 100 crediti iniziali.
- Scegli 3 Pokémon tra quelli disponibili nel Pokédex (pokedex.json).
- Ogni Pokémon ha un costo differente in base alla sua potenza e alle sue statistiche.
- Il Computer seleziona casualmente la propria squadra.

**Battaglia**

- Ogni turno puoi scegliere una delle seguenti mosse:
    1. **Attacco base** – infligge danni standard in base a `attacco` e `difesa`.
    2. **Mossa speciale** – ogni Pokémon ha 2 mosse speciali con effetti diversi.
    3. **Cura** – recupera una piccola quantità di HP.

- Il computer sceglie casualmente una mossa a ogni turno.
- Vince la squadra che **mantiene almeno un Pokémon vivo** quando tutti gli altri sono esausti (HP ≤ 0).

---

## 🧩 Concetti chiave del progetto

| Concetto                  | Dove viene applicato                         |
| ------------------------- | -------------------------------------------- |
| **Classi e oggetti**      | `Pokemon`, `Team`, `Battle`                  |
| **Ereditarietà**          | Ogni Pokémon è una sottoclasse di `Pokemon`  |
| **Composizione**          | Una `Team` contiene più Pokémon              |
| **Gestione file JSON**    | Lettura del file `pokedex.json` in `main.py` |
| **Controllo di flusso**   | Loop principale in `Battle.start()`          |
| **Input e validazione**   | Funzioni in `utils.py`                       |
| **Casualità controllata** | Attacchi e cure con `random`                 |
