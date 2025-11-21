import random
from src.utils import random_variation, clamp, input_numero


class Pokemon:
    """
    Classe base per tutti i Pokémon.
    Ogni Pokémon ha nome, tipo, hp attuali, hp massimi, attacco, difesa e costo (per il budget iniziale).
    """

    def __init__(self, nome: str, tipo: str, hp: int, attacco: int, difesa: int, costo: int):
        self.nome = nome
        self.tipo = tipo
        self.hp_max = hp
        self.hp = hp
        self.attacco = attacco
        self.difesa = difesa
        self.costo = costo

    def is_alive(self) -> bool:
        """True se il Pokémon non è esausto (HP > 0)."""
        return self.hp > 0

    def attacco_base(self, avversario: "Pokemon") -> None:
        """
        Attacco fisico standard.
        Danno = (attacco con piccola variazione) - difesa avversario, minimo 0.
        """
        danno = max(0, random_variation(self.attacco) - avversario.difesa)
        avversario.hp = max(0, avversario.hp - danno)
        print(f"💥 {self.nome} colpisce {avversario.nome} e infligge {danno} danni!")

    def cura(self) -> None:
        """
        Recupera una quantità moderata di HP (5-10), senza superare gli HP massimi.
        """
        heal = random.randint(5, 10)
        self.hp = min(self.hp_max, self.hp + heal)
        print(f"❤️ {self.nome} recupera {heal} HP!")

    # --- Gestione mosse speciali ---
    def mossa_speciale(self, avversario: "Pokemon", scelta: int | None = None) -> None:
        """
        Esegue una delle due mosse speciali.
        - Se 'scelta' è None, la funzione chiede all'utente (uso per il giocatore).
        - Se 'scelta' è 1 o 2, esegue direttamente quella mossa (uso per il PC).
        """
        #si può usare anche input_numero per validare l'input
        if scelta is None:
            while True:
                # Menù testuale per il giocatore (didattico e chiaro)
                print(f"\nScegli una mossa speciale per {self.nome}:")
                print("1. Mossa speciale 1")
                print("2. Mossa speciale 2")
                scelta_input = input("> ").strip()
                if scelta_input in ["1", "2"]:
                    break
                print("Input non valido. Inserisci 1 o 2.")
            scelta = 1 if scelta_input == "1" else 2

        if scelta == 1:
            self.mossa_speciale_1(avversario)
        else:
            self.mossa_speciale_2(avversario)

    def mossa_speciale_1(self, avversario: "Pokemon") -> None:
        """Da ridefinire nelle sottoclassi."""
        print(f"{self.nome} prova a usare una mossa speciale, ma non accade nulla...")

    def mossa_speciale_2(self, avversario: "Pokemon") -> None:
        """Da ridefinire nelle sottoclassi."""
        print(f"{self.nome} prova a usare una mossa speciale, ma non accade nulla...")


# --- Sottoclassi con 2 mosse speciali ciascuna ---

class Pikachu(Pokemon):
    def __init__(self):
        super().__init__("Pikachu", "Elettrico", hp=45, attacco=15, difesa=6, costo=40)

    def mossa_speciale_1(self, avversario):
        # Fulmine: attacco elettrico più forte
        danno = self.attacco + random.randint(5, 10)
        avversario.hp = max(0, avversario.hp - danno)
        print(f"⚡ {self.nome} usa Fulmine! {avversario.nome} perde {danno} HP!")

    def mossa_speciale_2(self, avversario):
        # Carica: aumenta l'attacco di Pikachu di 2 (limitato a +10 extra per evitare crescita eccessiva)
        incremento = 2
        self.attacco = clamp(self.attacco + incremento, 1, 25)
        print(f"⚡ {self.nome} si carica! L'attacco aumenta di {incremento} (ora {self.attacco}).")


class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__("Bulbasaur", "Erba", hp=50, attacco=12, difesa=8, costo=30)

    def mossa_speciale_1(self, avversario):
        # Fotosintesi: recupera HP
        heal = random.randint(8, 12)
        self.hp = min(self.hp_max, self.hp + heal)
        print(f"🌿 {self.nome} usa Fotosintesi e recupera {heal} HP!")

    def mossa_speciale_2(self, avversario):
        # Frustata: attacco moderato
        danno = self.attacco + random.randint(3, 6)
        avversario.hp = max(0, avversario.hp - danno)
        print(f"🌱 {self.nome} usa Frustata! {avversario.nome} subisce {danno} danni!")


class Charmander(Pokemon):
    def __init__(self):
        super().__init__("Charmander", "Fuoco", hp=43, attacco=14, difesa=7, costo=35)

    def mossa_speciale_1(self, avversario):
        # Braciere
        danno = self.attacco + random.randint(6, 9)
        avversario.hp = max(0, avversario.hp - danno)
        print(f"🔥 {self.nome} usa Braciere! {avversario.nome} subisce {danno} danni!")

    def mossa_speciale_2(self, avversario):
        # Lanciafiamme (leggermente più variabile)
        danno = self.attacco + random.randint(4, 8)
        avversario.hp = max(0, avversario.hp - danno)
        print(f"🔥 {self.nome} usa Lanciafiamme! {avversario.nome} perde {danno} HP!")


class Squirtle(Pokemon):
    def __init__(self):
        super().__init__("Squirtle", "Acqua", hp=48, attacco=11, difesa=10, costo=35)

    def mossa_speciale_1(self, avversario):
        # Pistolacqua
        danno = self.attacco + random.randint(4, 7)
        avversario.hp = max(0, avversario.hp - danno)
        print(f"💧 {self.nome} usa Pistolacqua! {avversario.nome} perde {danno} HP!")

    def mossa_speciale_2(self, avversario):
        # Guscioscudo: aumenta difesa
        incremento = 2
        self.difesa = clamp(self.difesa + incremento, 1, 20)
        print(f"💦 {self.nome} si protegge: difesa +{incremento} (ora {self.difesa}).")


class Eevee(Pokemon):
    def __init__(self):
        super().__init__("Eevee", "Normale", hp=46, attacco=13, difesa=7, costo=25)

    def mossa_speciale_1(self, avversario):
        # Attacco rapido
        danno = self.attacco + random.randint(4, 8)
        avversario.hp = max(0, avversario.hp - danno)
        print(f"🐾 {self.nome} usa Attacco Rapido! {avversario.nome} subisce {danno} danni!")

    def mossa_speciale_2(self, avversario):
        # Rigenerazione
        heal = 8
        self.hp = min(self.hp_max, self.hp + heal)
        print(f"✨ {self.nome} si rigenera e recupera {heal} HP!")


class Jigglypuff(Pokemon):
    def __init__(self):
        super().__init__("Jigglypuff", "Normale", hp=52, attacco=10, difesa=6, costo=25)

    def mossa_speciale_1(self, avversario):
        # Canto: riduce l'attacco avversario
        riduzione = 2
        avversario.attacco = clamp(avversario.attacco - riduzione, 1, 25)
        print(f"🎵 {self.nome} canta! L'attacco di {avversario.nome} diminuisce di {riduzione} (ora {avversario.attacco}).")

    def mossa_speciale_2(self, avversario):
        # Ricarica: recupera HP
        heal = random.randint(6, 10)
        self.hp = min(self.hp_max, self.hp + heal)
        print(f"💖 {self.nome} si ricarica di energia e recupera {heal} HP!")


class Geodude(Pokemon):
    def __init__(self):
        super().__init__("Geodude", "Roccia", hp=55, attacco=12, difesa=12, costo=35)

    def mossa_speciale_1(self, avversario):
        # Rocciata
        danno = self.attacco + random.randint(3, 6)
        avversario.hp = max(0, avversario.hp - danno)
        print(f"🪨 {self.nome} usa Rocciata! {avversario.nome} perde {danno} HP!")

    def mossa_speciale_2(self, avversario):
        # Rinforzo: aumenta difesa
        incremento = 3
        self.difesa = clamp(self.difesa + incremento, 1, 25)
        print(f"💪 {self.nome} si rinforza! Difesa +{incremento} (ora {self.difesa}).")


class Psyduck(Pokemon):
    def __init__(self):
        super().__init__("Psyduck", "Acqua", hp=47, attacco=13, difesa=8, costo=30)

    def mossa_speciale_1(self, avversario):
        # Confusione
        danno = self.attacco + random.randint(5, 8)
        avversario.hp = max(0, avversario.hp - danno)
        print(f"🔮 {self.nome} usa Confusione! {avversario.nome} perde {danno} HP!")

    def mossa_speciale_2(self, avversario):
        # Concentrazione: piccola difesa extra
        incremento = 2
        self.difesa = clamp(self.difesa + incremento, 1, 22)
        print(f"😌 {self.nome} si concentra. Difesa +{incremento} (ora {self.difesa}).")
