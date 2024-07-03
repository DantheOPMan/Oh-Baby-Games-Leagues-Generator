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
            file.write("  Repeated {} Region: {}\n".format(game['repeated_region'], ', '.join(game['repeated'])))
            file.write("\n")

def generate_games(names):
    games = []
    player_counts = {name: {'EU': 0, 'NA': 0} for name in names}
    max_games_per_region = 8

    for game_number in range(1, 13):
        available_names = names.copy()
        random.shuffle(available_names)  # Shuffle the names for randomization

        eu_players = []
        na_players = []
        repeated_players = []

        # Determine region configuration for this game
        if game_number % 2 == 1:
            primary_region, repeated_region = 'EU', 'NA'  # 1 EU, 2 NA
        else:
            primary_region, repeated_region = 'NA', 'EU'  # 2 EU, 1 NA

        # Prioritize players with 7 games in one region
        for name in available_names[:]:
            if player_counts[name]['EU'] >= 7 and len(na_players) < 12:
                na_players.append(name)
                player_counts[name]['NA'] += 1
                available_names.remove(name)
            elif player_counts[name]['NA'] >= 7 and len(eu_players) < 12:
                eu_players.append(name)
                player_counts[name]['EU'] += 1
                available_names.remove(name)

        # Prioritize players with 6 games in one region to play in the other region
        for name in available_names[:]:
            if player_counts[name]['EU'] == 6 and len(na_players) < 12:
                na_players.append(name)
                player_counts[name]['NA'] += 1
                available_names.remove(name)
            elif player_counts[name]['NA'] == 6 and len(eu_players) < 12:
                eu_players.append(name)
                player_counts[name]['EU'] += 1
                available_names.remove(name)

        # Fill remaining spots in primary and repeated regions
        for name in available_names[:]:
            if primary_region == 'EU' and len(eu_players) < 12:
                eu_players.append(name)
                player_counts[name]['EU'] += 1
                available_names.remove(name)
            elif primary_region == 'NA' and len(na_players) < 12:
                na_players.append(name)
                player_counts[name]['NA'] += 1
                available_names.remove(name)

        for name in available_names[:]:
            if repeated_region == 'EU' and len(repeated_players) < 12:
                repeated_players.append(name)
                player_counts[name]['EU'] += 1
                available_names.remove(name)
            elif repeated_region == 'NA' and len(repeated_players) < 12:
                repeated_players.append(name)
                player_counts[name]['NA'] += 1
                available_names.remove(name)

        # Fill remaining spots for any leftover players
        for name in available_names[:]:
            if len(eu_players) < 12:
                eu_players.append(name)
                player_counts[name]['EU'] += 1
                available_names.remove(name)
            elif len(na_players) < 12:
                na_players.append(name)
                player_counts[name]['NA'] += 1
                available_names.remove(name)
            elif len(repeated_players) < 12:
                repeated_players.append(name)
                if repeated_region == 'EU':
                    player_counts[name]['EU'] += 1
                else:
                    player_counts[name]['NA'] += 1
                available_names.remove(name)

        games.append({
            'number': game_number,
            'eu': eu_players,
            'na': na_players,
            'repeated': repeated_players,
            'repeated_region': repeated_region
        })

    return games

def main():
    names = read_names('names36.txt')
    games = generate_games(names)
    write_games('games.txt', games)
    player_counts = {name: {'EU': 0, 'NA': 0} for name in names}
    
    for game in games:
        for player in game['eu']:
            player_counts[player]['EU'] += 1
        for player in game['na']:
            player_counts[player]['NA'] += 1
        for player in game['repeated']:
            if game['repeated_region'] == 'EU':
                player_counts[player]['EU'] += 1
            else:
                player_counts[player]['NA'] += 1

    # Print player counts to check balance
    for player, counts in player_counts.items():
        print(f"{player} - EU: {counts['EU']}, NA: {counts['NA']}")

if __name__ == "__main__":
    main()
