import random


def input_numero(messaggio: str, minimo: int, massimo: int) -> int:
    """
    Richiede un numero intero tra minimo e massimo (inclusi), con validazione semplice.
    Riprova finché l'utente non inserisce un valore valido.
    """
    while True:
        try:
            val = int(input(messaggio))
            if minimo <= val <= massimo:
                return val
            print(f"⚠️  Inserisci un numero tra {minimo} e {massimo}.")
        except ValueError:
            print("❌ Valore non valido. Riprova.")


def barra_hp(hp: int, hp_max: int) -> str:
    """
    Restituisce una rappresentazione testuale della barra HP.
    Esempio: [██████----------] 30/60
    """
    hp = max(0, hp)
    lunghezza = 20
    filled = int(lunghezza * hp / max(1, hp_max))
    return "[" + "█" * filled + "-" * (lunghezza - filled) + f"] {hp}/{hp_max}"


def random_variation(value: int, variation: int = 3) -> int:
    """
    Applica una piccola variazione casuale a 'value' nell'intervallo [-variation, +variation].
    Utile per rendere il danno meno deterministico.
    """
    return value + random.randint(-variation, variation)


def clamp(value: int, minimo: int, massimo: int) -> int:
    """Limita value nell'intervallo [minimo, massimo]."""
    return max(minimo, min(massimo, value))
