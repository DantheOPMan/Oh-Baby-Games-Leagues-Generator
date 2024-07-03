import re
from collections import defaultdict

def parse_games(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    games = {}
    current_game = ""
    current_region = ""
    
    for line in lines:
        line = line.strip()
        if line.startswith("Game"):
            current_game = line
            games[current_game] = {"EU": [], "NA": []}
        elif line.startswith("EU Region:"):
            current_region = "EU"
            games[current_game][current_region] = re.split(r',\s*', line.split(": ")[1])
        elif line.startswith("NA Region:"):
            current_region = "NA"
            games[current_game][current_region] = re.split(r',\s*', line.split(": ")[1])

    return games

def check_repeats(games):
    repeats = defaultdict(int)
    for game, regions in games.items():
        players_in_game = set()
        for region, players in regions.items():
            for player in players:
                if player in players_in_game:
                    repeats[player] += 1
                players_in_game.add(player)
    return repeats

def count_player_participation(games):
    participation_count = defaultdict(lambda: {"EU": 0, "NA": 0})
    for game, regions in games.items():
        for region, players in regions.items():
            for player in players:
                participation_count[player][region] += 1
    return participation_count

def main():
    file_path = 'games.txt'
    games = parse_games(file_path)
    repeats = check_repeats(games)
    participation_count = count_player_participation(games)

    print("Repeats in games:")
    for player, count in repeats.items():
        print(f"{player}: {count} times")

    print("\nParticipation count:")
    for player, counts in participation_count.items():
        print(f"{player} - EU: {counts['EU']}, NA: {counts['NA']}")

if __name__ == "__main__":
    main()
