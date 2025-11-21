from __future__ import annotations

import json
import random
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List, Set, Literal


# ==============================
# 📁 Costanti per i file
# ==============================

PAROLE_FILE = Path("parole.txt")
STORICO_FILE = Path("storico.json")


# ==============================
# 📊 Dataclass per lo storico
# ==============================

@dataclass
class RisultatoPartita:
    parola: str
    tentativi_usati: int
    tentativi_max: int
    difficolta: str   # "facile" o "difficile"
    vittoria: bool


# ==============================
# 📁 Gestione parole.txt
# ==============================

LISTA_PAROLE = [
        "amico", "anello", "animale", "antico", "armadio",
        "bambino", "barcone", "binocolo", "biscotto", "bottone",
        "calcolo", "calzino", "camerun", "cammino", "capanna",
        "carbone", "cascata", "castoro", "cavallo", "civetta",
        "colombo", "cometa", "cornice", "corridoio", "cravatta",
        "delfino", "dentista", "diarrea", "disegno", "dormire",
        "elefante", "elogio", "energia", "esempio", "esterno",
        "fattore", "fermata", "finestra", "fiorire", "formica",
        "fragola", "funzione", "galassia", "gelatina", "gelso",
        "giardino", "giocare", "giornale", "girasole", "gommone",
        "gradino", "grappolo", "gravita", "guadagno", "guardia",
        "imbuto", "incanto", "incrocio", "ingresso", "inverno",
        "lattuga", "lavorare", "legenda", "leonessa", "lettera",
        "libreria", "limonata", "lucertola", "luminoso", "lunetta",
        "macchina", "maglietta", "majore", "massimo", "matrice",
        "melone", "mentale", "mercato", "metallo", "minestra",
        "montagna", "morbido", "muscosa", "navigare", "nebbioso",
        "nocciolo", "operaio", "ordinare", "orologia", "ossigeno",
        "palazzo", "panetteria", "panorama", "parlare", "passero",
        "pensiero", "perdono", "pesciolo", "pianeta", "pinguino",
        "piramide", "pistone",
]


def carica_o_crea_parole(path: Path = PAROLE_FILE) -> List[str]:
    """
    Se parole.txt non esiste, lo crea con circa 400 parole di esempio.
    Poi legge il file e restituisce la lista di parole (in minuscolo, senza spazi).
    """
    if not path.exists():
        parole = LISTA_PAROLE
        path.write_text("\n".join(parole), encoding="utf-8")
        print(f"📄 File {path.name} non trovato: creato automaticamente con {len(parole)} parole di esempio.")

    testo = path.read_text(encoding="utf-8")
    parole = [riga.strip().lower() for riga in testo.splitlines() if riga.strip()]
    if not parole:
        raise ValueError(f"⚠️ Il file {path.name} è vuoto. Aggiungi qualche parola.")
    return parole


# ==============================
# 🧩 Classe principale del gioco
# ==============================

Difficolta = Literal["facile", "difficile"]

class Impiccato:
    """
    Classe che incapsula la logica del gioco dell'Impiccato.
    """

    def __init__(self, parola_segreta: str, difficolta: Difficolta) -> None:
        self.parola_segreta: str = parola_segreta.lower()
        self.difficolta: Difficolta = difficolta

        # Tentativi massimi in base alla difficoltà
        self.tentativi_max: int = 10 if difficolta == "facile" else 6
        self.tentativi_errati: int = 0

        # Insiemi di lettere indovinate e tentate (comodi da usare)
        self.lettere_indovinate: Set[str] = set()
        self.lettere_tentate: Set[str] = set()

    # ---------- Stato ----------

    def parola_mostrata(self) -> str:
        """
        Restituisce la parola con lettere indovinate e '_' per quelle mancanti.
        Esempio: 'python' + {p, o} → 'p _ _ _ o _'
        """
        return " ".join(
            c if c in self.lettere_indovinate else "_"
            for c in self.parola_segreta
        )

    def vittoria(self) -> bool:
        """
        True se tutte le lettere della parola sono state indovinate.
        """
        return all(c in self.lettere_indovinate for c in self.parola_segreta)

    def partita_finita(self) -> bool:
        """
        True se la partita è vinta oppure se i tentativi sono esauriti.
        """
        return self.vittoria() or self.tentativi_errati >= self.tentativi_max

    # ---------- Output utente ----------

    def mostra_stato(self) -> None:
        """
        Stampa a video lo stato corrente: parola parziale, tentativi, lettere tentate.
        """
        print("\nParola:", self.parola_mostrata())
        print(f"Tentativi: {self.tentativi_errati}/{self.tentativi_max}")
        if self.lettere_tentate:
            print("Lettere tentate:", ", ".join(sorted(self.lettere_tentate)))
        else:
            print("Lettere tentate: (nessuna)")

    # ---------- Logica di un tentativo ----------

    def _normalizza_lettera(self, lettera: str) -> str:
        """
        Normalizza la lettera inserita dall'utente (strip + minuscolo).
        """
        return lettera.strip().lower()

    def tenta(self, lettera_raw: str) -> None:
        """
        Gestisce un tentativo dell'utente.

        Regole comuni:
        - se non è una singola lettera alfabetica:
          - in facile → avvisa ma non penalizza
          - in difficile → penalizza
        - se lettera già tentata:
          - in facile → avvisa, non penalizza
          - in difficile → penalizza
        - se lettera non nella parola → penalizza
        - se nella parola → aggiungi a lettere_indovinate
        """
        lettera = self._normalizza_lettera(lettera_raw)

        # Controllo validità carattere
        if len(lettera) != 1 or not lettera.isalpha():
            if self.difficolta == "facile":
                print("⚠️ Inserisci UNA sola lettera alfabetica (nessuna penalità in facile).")
            else:
                print("❌ Modalità difficile: input non valido → penalità!")
                self.tentativi_errati += 1
            return

        # Controllo se già tentata
        if lettera in self.lettere_tentate:
            if self.difficolta == "facile":
                print("ℹ️ Lettera già tentata, nessuna penalità in facile.")
            else:
                print("❌ Lettera già tentata → penalità in difficile!")
                self.tentativi_errati += 1
            return

        # Aggiungiamo la lettera alle tentate
        self.lettere_tentate.add(lettera)

        # Verifichiamo se è nella parola
        if lettera in self.parola_segreta:
            print(f"✅ '{lettera}' è nella parola!")
            self.lettere_indovinate.add(lettera)
        else:
            print(f"❌ '{lettera}' non è nella parola.")
            self.tentativi_errati += 1


# ==============================
# 📊 Gestione storico (JSON)
# ==============================

def carica_storico(path: Path = STORICO_FILE) -> List[RisultatoPartita]:
    """
    Carica lo storico delle partite da JSON.
    Se il file non esiste o è corrotto, restituisce una lista vuota.
    """
    if not path.exists():
        return []

    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
        # Ogni elemento è un dict con le chiavi della dataclass
        return [RisultatoPartita(**entry) for entry in raw]
    except Exception:
        print("⚠️ Impossibile leggere lo storico. Verrà sovrascritto.")
        return []


def salva_risultato(risultato: RisultatoPartita, path: Path = STORICO_FILE) -> None:
    """
    Aggiunge un risultato allo storico e riscrive il file JSON.
    """
    storico = carica_storico(path)
    storico.append(risultato)
    data = [asdict(r) for r in storico]
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def mostra_riassunto_finale(path: Path = STORICO_FILE) -> None:
    """
    Mostra un breve riassunto delle partite giocate (totale, vittorie, sconfitte).
    """
    storico = carica_storico(path)
    if not storico:
        print("\n📊 Nessuna statistica disponibile (nessuna partita registrata).")
        return

    tot = len(storico)
    vinte = sum(1 for r in storico if r.vittoria)
    perse = tot - vinte
    facili = [r for r in storico if r.difficolta == "facile"]
    difficili = [r for r in storico if r.difficolta == "difficile"]

    print("\n📊 Statistiche globali:")
    print(f"- Partite totali: {tot}")
    print(f"- Vittorie: {vinte} | Sconfitte: {perse}")
    if facili:
        v_facili = sum(1 for r in facili if r.vittoria)
        print(f"- Modalità FACILE: {len(facili)} partite, {v_facili} vittorie")
    if difficili:
        v_difficili = sum(1 for r in difficili if r.vittoria)
        print(f"- Modalità DIFFICILE: {len(difficili)} partite, {v_difficili} vittorie")


# ==============================
# 🎛️ Input difficoltà e loop partita
# ==============================

def scegli_difficolta() -> Difficolta:
    """
    Chiede all'utente la difficoltà e restituisce 'facile' o 'difficile'.
    """
    while True:
        print("\nScegli la difficoltà:")
        print("1) Facile (10 tentativi, input non valido e duplicate non penalizzano)")
        print("2) Difficile (6 tentativi, input non valido e duplicate penalizzano)")
        scelta = input("> ").strip()
        if scelta == "1":
            return "facile"
        if scelta == "2":
            return "difficile"
        print("⚠️ Scelta non valida. Inserisci 1 o 2.")


def gioca_una_partita() -> None:
    """
    Gestisce una singola partita:
    - carica/crea le parole
    - seleziona difficoltà
    - estrae una parola casuale
    - esegue il loop di tentativi
    - salva il risultato in storico.json
    """
    parole = carica_o_crea_parole()
    parola = random.choice(parole)  # parola segreta
    difficolta = scegli_difficolta()
    gioco = Impiccato(parola, difficolta)

    print("\n🪢 Benvenuto nel gioco dell'Impiccato!")
    # Per debug durante lo sviluppo:
    # print(f"[DEBUG] La parola segreta è: {parola}")

    # Loop principale del gioco
    while not gioco.partita_finita():
        gioco.mostra_stato()
        lettera = input("Inserisci una lettera: ")
        gioco.tenta(lettera)

    # Fine partita
    gioco.mostra_stato()
    if gioco.vittoria():
        print(f"\n🎉 Complimenti! Hai indovinato la parola: '{gioco.parola_segreta}'")
    else:
        print(f"\n💀 Hai esaurito i tentativi. La parola era: '{gioco.parola_segreta}'")

    # Salviamo il risultato nello storico
    risultato = RisultatoPartita(
        parola=gioco.parola_segreta,
        tentativi_usati=gioco.tentativi_errati,
        tentativi_max=gioco.tentativi_max,
        difficolta=gioco.difficolta,
        vittoria=gioco.vittoria(),
    )
    salva_risultato(risultato)


def main() -> None:
    """
    Entry point del programma:
    permette di giocare più partite e mostra un riassunto finale.
    """
    while True:
        gioca_una_partita()
        # Chiediamo se l'utente vuole rigiocare
        scelta = ""
        while scelta not in ["s", "n"]:
            scelta = input("\nVuoi giocare un'altra partita? (s/n): ").strip().lower()
            if scelta not in ["s", "n"]:
                print("⚠️ Scelta non valida. Inserisci 's' o 'n'.")
        
        if scelta != "s":
            break
        
    mostra_riassunto_finale()
    print("\n👋 Grazie per aver giocato all'Impiccato!")


if __name__ == "__main__":
    main()
