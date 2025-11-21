
import json
import random

from src.team import Team, POKEMON_CLASSI
from src.battle import Battle
from src.utils import input_numero


def main():
    
    rigioca = True
    while rigioca:
        print("🐉 Benvenuto in Pokémon Battle Arena!")
        print("Hai 100 crediti per scegliere la tua squadra (3 Pokémon).\n")

        # Carica il pokedex
        with open("data/pokedex.json", "r", encoding="utf-8") as f:
            pokedex = json.load(f)

        budget = 100
        team_player = Team("Giocatore")
        team_pc = Team("Computer")

        # --- Scelta del giocatore ---
        possibili_giocatore = list(pokedex.items())
        while len(team_player.pokemon) < 3:
            print(f"\n💰 Budget rimanente: {budget}")
            print("Pokémon disponibili:")
            for i, (nome, stats) in enumerate(possibili_giocatore, 1): # evita di mostrare i Pokémon già scelti
                print(f"{i}. {nome:11s} | Tipo: {stats['tipo']:<9s} | HP: {stats['hp']:>2d} | "
                    f"Att: {stats['attacco']:>2d} | Dif: {stats['difesa']:>2d} | Costo: {stats['costo']:>2d}")

            scelta = input_numero("Scegli un Pokémon (numero): ", 1, len(pokedex))
            nome_scelto = list(pokedex.keys())[scelta - 1]
            costo = pokedex[nome_scelto]["costo"]

            if costo > budget:
                print("❌ Non hai abbastanza crediti!")
                continue

            # Istanzia la classe corretta dal nome scelto
            cls = POKEMON_CLASSI.get(nome_scelto)
            if not cls:
                print("Errore interno: Pokémon non trovato.")
                continue
            # Aggiungi il Pokémon alla squadra
            team_player.aggiungi_pokemon(cls())
            possibili_giocatore = [p for p in possibili_giocatore if p[0] != nome_scelto]
            budget -= costo
            print(f"✅ {nome_scelto} aggiunto alla squadra!")

        # --- Squadra del PC (scelta casuale, 3 Pokémon diversi) ---
        budget_pc = 100
        possibili = list(POKEMON_CLASSI.keys())
        while len(team_pc.pokemon) < 3:
            cpu_choice = random.sample(possibili, 1)[0]
            
            #cancellare il pokemon scelto per evitare duplicati
            possibili.remove(cpu_choice)
            # controllare il budget del pc sulla base del costo del pokemon scelto
            costo = pokedex[cpu_choice]["costo"]
            if costo > budget_pc:
                continue
            budget_pc -= costo
            team_pc.aggiungi_pokemon(POKEMON_CLASSI[cpu_choice]())
            

        print("\nLa tua squadra :", [p.nome for p in team_player.pokemon])
        print("Squadra avversaria:", [p.nome for p in team_pc.pokemon])
        input("\nPremi INVIO per iniziare la battaglia...")

        # --- Avvio battaglia ---
        battle = Battle(team_player, team_pc)
        battle.start()
    
        # --- Rigioca? --- richiedere finchè non si ha un input valido
        while True:
            risposta = input("\nVuoi rigiocare? (s/n): ").strip().lower()
            if risposta in ['s', 'n']:
                rigioca = (risposta == 's')
                break
            print("⚠️  Risposta non valida. Inserisci 's' per sì o 'n' per no.")
        


if __name__ == "__main__":
    main()
