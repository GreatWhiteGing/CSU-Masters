import random
import os

modes = ["Clash", "Control", "Elimination", "Mayhem", "Momentum Control", "Rift", "Showdown", "Survival",
         "Team Scorched", "Zone Control", "Supremacy"]
maps = ["Altar of Flame", "Bannerfall", "Cathedral of Dusk", "Cauldron", "Convergence", "Disjunction", "Distant Shore",
        "Endless Vale", "Eternity", "Exodus Blue", "Fragment", "Javelin-4",
        "Midtown", "Pacifica", "Radiant Cliffs", "Rusted Lands", "The Anomaly", "The Burnout", "The Dead Cliffs",
        "The Fortress", "Twilight Gap", "Vostok", "Widows Court", "Wormhaven"]
primary_weapon = ["Auto Rifles", "Scout Rifles", "Pulse Rifles", "Hand Canons", "SMGs", "Sidearms", "Bows"]
special_weapon = ["Shotguns", "GLs", "Fusion Rifles", "Sniper Rifles", "Trace Rifles", "Glaives"]


def choose_mode(modes, player_count):
    if player_count % 2 != 0:
        game_mode = "Rumble"
    else:
        game_mode = random.choice(modes)
    print(f"You are playing {game_mode}")
    return game_mode


def choose_map(maps):
    game_map = random.choice(maps)
    print(f"You are playing on {game_map}")


def choose_weapon(game_mode):
    if game_mode == "Team Scorched":
        print("Scorch that ass!")
    else:
        weapon1 = random.choice(primary_weapon)
        weapon2 = random.choice(special_weapon)
        print(f"You will be using {weapon1} and {weapon2}")
        use_exotics()


def use_exotics():
    yes_or_no = ["YESSSSS", "Nah"]
    choice = random.choice(yes_or_no)
    print(f"Exotics?: {choice}")


def choose_teams():
    players = []
    player_count = input("How many players?: ")
    x = int(player_count)
    for i in range(0, x):
        y = input("Player name: ")
        players.append(y)
    os.system('cls')
    if x % 2 == 0:
        team1 = random.sample(players, int(x / 2))
        print('\n----------------------------------------------------')
        print("Team 1: ")
        print(*team1, sep=', ')
    else:
        print('\n----------------------------------------------------')
        print("FREE FOR ALL!!")
    return x


def do_the_dew():
    teams = choose_teams()
    print('\n----------------------------------------------------')
    game_mode = choose_mode(modes, teams)
    print('\n----------------------------------------------------')
    choose_map(maps)
    print('\n----------------------------------------------------')
    choose_weapon(game_mode)


do_the_dew()
