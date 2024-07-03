import random

players = [
    "zCxtalyst", "Khushas", "Melli", "nickwark", "codsy", "fluxray", "mahotei", "Bartic",
    "SHIBA-DOG-MILLIONAIRE", "Axelmeow", "jorgatan", "Drift", "johnnyeth", "RiskETH",
    "chinchilla", "elbow", "Cody", "Invi", "LarlLad", ".archer.", "kelty", "Shapes",
    "shadow", "Morph"
]

num_players = len(players)
num_games = 12
players_per_region = 12

# Ensure players participate equally in EU and NA regions
eu_count = {player: 0 for player in players}
na_count = {player: 0 for player in players}

games = {}

for game_num in range(1, num_games + 1):
    random.shuffle(players)
    games[f"Game {game_num}"] = {"EU": [], "NA": []}
    
    # Temporary list to track which players have been picked for this game
    picked_players = set()
    
    eu_players = []
    na_players = []
    
    # Distribute players to regions ensuring balance
    for player in players:
        if len(eu_players) < players_per_region and eu_count[player] < 6 and player not in picked_players:
            eu_players.append(player)
            eu_count[player] += 1
            picked_players.add(player)
        elif len(na_players) < players_per_region and na_count[player] < 6 and player not in picked_players:
            na_players.append(player)
            na_count[player] += 1
            picked_players.add(player)
    
    # Ensure all spots are filled
    while len(eu_players) < players_per_region:
        eligible_players = [player for player in players if player not in picked_players and eu_count[player] < 6]
        if not eligible_players:
            eligible_players = [player for player in players if player not in picked_players]
        player = random.choice(eligible_players)
        eu_players.append(player)
        eu_count[player] += 1
        picked_players.add(player)

    while len(na_players) < players_per_region:
        eligible_players = [player for player in players if player not in picked_players and na_count[player] < 6]
        if not eligible_players:
            eligible_players = [player for player in players if player not in picked_players]
        player = random.choice(eligible_players)
        na_players.append(player)
        na_count[player] += 1
        picked_players.add(player)

    games[f"Game {game_num}"]["EU"] = eu_players
    games[f"Game {game_num}"]["NA"] = na_players

# Output the games
for game, regions in games.items():
    print(f"{game}:")
    for region, players in regions.items():
        print(f"  {region} Region: {', '.join(players)}")

# Verify the distribution
print("\nPlayer Participation Count:")
for player in players:
    print(f"{player} - EU: {eu_count[player]}, NA: {na_count[player]}")
