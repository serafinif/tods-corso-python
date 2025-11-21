from src.pokemon import Pikachu, Bulbasaur, Charmander, Squirtle, Eevee, Jigglypuff, Geodude, Psyduck
from src.utils import input_numero
import random


class Team:
    """Rappresenta una squadra di Pokémon (giocatore o computer)."""

    def __init__(self, nome: str):
        self.nome = nome
        self.pokemon = []

    def aggiungi_pokemon(self, pokemon) -> None:
        """Aggiunge un Pokémon alla squadra."""
        self.pokemon.append(pokemon)

    def scegli_attivo(self):
        """
        Ritorna un Pokémon vivo per combattere.
        - Se la squadra è del computer: scelta casuale tra i vivi.
        - Se è del giocatore: chiede quale Pokémon attivo selezionare.
        """
        vivi = [p for p in self.pokemon if p.is_alive()]
        if not vivi:
            return None

        if self.nome == "Computer":
            return random.choice(vivi)

        print("\nScegli il Pokémon attivo:")
        for i, p in enumerate(vivi, 1):
            print(f"{i}. {p.nome} (HP: {p.hp}/{p.hp_max})")
        scelta = input_numero("> ", 1, len(vivi))
        return vivi[scelta - 1]

    def ha_pokemon_vivi(self) -> bool:
        """True se c'è almeno un Pokémon non esausto nella squadra."""
        return any(p.is_alive() for p in self.pokemon)


# Mappa dei nomi a classi (per costruire le istanze dalla scelta utente/CPU)
POKEMON_CLASSI = {
    "Pikachu": Pikachu,
    "Bulbasaur": Bulbasaur,
    "Charmander": Charmander,
    "Squirtle": Squirtle,
    "Eevee": Eevee,
    "Jigglypuff": Jigglypuff,
    "Geodude": Geodude,
    "Psyduck": Psyduck,
}
