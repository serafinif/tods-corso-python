from src.utils import input_numero, barra_hp
import random


class Battle:
    """Gestisce la logica della battaglia a turni tra due squadre."""

    def __init__(self, team_giocatore, team_pc):
        self.team_giocatore = team_giocatore
        self.team_pc = team_pc

    def turno_giocatore(self, p1, p2):
        """Turno del giocatore: menù mosse e applicazione degli effetti."""
        print(f"\n{p1.nome} (TUO) VS {p2.nome} (CPU)")
        print(f"HP {p1.nome}: {barra_hp(p1.hp, p1.hp_max)}")
        print(f"HP {p2.nome}: {barra_hp(p2.hp, p2.hp_max)}")

        print("\nScegli una mossa:")
        print("1. Attacco base")
        print("2. Mossa speciale")
        print("3. Cura")
        scelta = input_numero("> ", 1, 3)

        if scelta == 1:
            p1.attacco_base(p2)
        elif scelta == 2:
            # L'utente sceglie quale delle due speciali usare (gestito dal metodo)
            p1.mossa_speciale(p2)
        else:
            p1.cura()

    def turno_pc(self, p_cpu, p_player):
        """Turno del computer: scelta casuale tra attacco base, mossa speciale (1 o 2) e cura."""
        print(f"\n🤖 Turno del PC! ({p_cpu.nome})")
        scelta = random.choice(["base", "spec1", "spec2", "cura"])
        if scelta == "base":
            p_cpu.attacco_base(p_player)
        elif scelta == "spec1":
            p_cpu.mossa_speciale(p_player, scelta=1)
        elif scelta == "spec2":
            p_cpu.mossa_speciale(p_player, scelta=2)
        else:
            p_cpu.cura()

    def start(self):
        """Loop principale della battaglia: alterna i turni finché una squadra non è sconfitta."""
        print("\n⚔️  INIZIA LA BATTAGLIA! ⚔️")

        while self.team_giocatore.ha_pokemon_vivi() and self.team_pc.ha_pokemon_vivi():
            p1 = self.team_giocatore.scegli_attivo()
            p2 = self.team_pc.scegli_attivo()
            if not p1 or not p2:
                break

            # Turno del giocatore
            self.turno_giocatore(p1, p2)
            if not p2.is_alive():
                print(f"💀 {p2.nome} è esausto!\n")
                continue  # salta il turno del PC se il suo Pokémon è appena andato K.O.

            # Turno del PC
            self.turno_pc(p2, p1)
            if not p1.is_alive():
                print(f"💀 Il tuo {p1.nome} è esausto!\n")

        # Esito finale
        if self.team_giocatore.ha_pokemon_vivi():
            print("🎉 Hai vinto la battaglia!")
        else:
            print("😵 La tua squadra è stata sconfitta!")
