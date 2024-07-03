import random

def read_names(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

def write_games(filename, games):
    with open(filename, 'w') as file:
        for game in games:
            file.write("Game {}:\n".format(game['number']))
            file.write("  EU Region: {}\n".format(', '.join(game['eu'])))
            file.write("  NA Region: {}\n".format(', '.join(game['na'])))
            file.write("\n")

def generate_games(names):
    games = []
    player_counts = {name: {'EU': 0, 'NA': 0} for name in names}
    max_games_per_region = 6

    for game_number in range(1, 13):
        random.shuffle(names)  # Shuffle the names for randomization
        eu_players = []
        na_players = []

        # First, allocate players with 7 games in one region
        for name in names:
            eu_count = player_counts[name]['EU']
            na_count = player_counts[name]['NA']
            if eu_count == 7 and len(na_players) < 12:
                na_players.append(name)
                player_counts[name]['NA'] += 1
            elif na_count == 7 and len(eu_players) < 12:
                eu_players.append(name)
                player_counts[name]['EU'] += 1

        # Then, allocate the rest
        for name in names:
            if name in eu_players or name in na_players:
                continue
            eu_count = player_counts[name]['EU']
            na_count = player_counts[name]['NA']
            if eu_count < max_games_per_region and len(eu_players) < 12:
                eu_players.append(name)
                player_counts[name]['EU'] += 1
            elif na_count < max_games_per_region and len(na_players) < 12:
                na_players.append(name)
                player_counts[name]['NA'] += 1

        # Ensure all players are assigned
        remaining_players = [name for name in names if name not in eu_players and name not in na_players]
        for name in remaining_players:
            if len(eu_players) < 12:
                eu_players.append(name)
                player_counts[name]['EU'] += 1
            else:
                na_players.append(name)
                player_counts[name]['NA'] += 1

        games.append({
            'number': game_number,
            'eu': eu_players,
            'na': na_players
        })

    return games

def main():
    names = read_names('names.txt')
    games = generate_games(names)
    write_games('games.txt', games)
    player_counts = {name: {'EU': 0, 'NA': 0} for name in names}
    
    for game in games:
        for player in game['eu']:
            player_counts[player]['EU'] += 1
        for player in game['na']:
            player_counts[player]['NA'] += 1

    # Print player counts to check balance
    for player, counts in player_counts.items():
        print(f"{player} - EU: {counts['EU']}, NA: {counts['NA']}")

if __name__ == "__main__":
    main()
