import requests
from dotenv import load_dotenv
import os
# import json

load_dotenv()
riot_api_key = os.environ.get("riot_api_key")

def main():
    region_server, game_name, tag_line, server = get_username_from_user()
    puuid = get_puuid(region_server, game_name, tag_line)
    matches = get_matches(server, puuid)
    
    # Initialize win and lose counts
    win_count = 0
    lose_count = 0
    
    for match_id in matches:
        info = get_match_info(server, match_id)
        if info is not None:
            stats = game_stats(info, puuid)
            win, lose = win_rate_checker(stats)
            win_count += win  # Update win count
            lose_count += lose  # Update lose count
            if win_count + lose_count == 50:  # Check if we check 50 matches
                break  # exit the loop

    #calculate the winrate
    total_matches = win_count + lose_count
    win_rate = (win_count / total_matches) * 100 if total_matches > 0 else 0
    
    print()
    print(f"WINRATE: {win_rate:.2f}%")
    print()


def get_username_from_user():
    game_name = input("Enter your username: ").replace(" ", "_")
    tag_line = input("Enter your tagline: ")
    print("Servers are NA, BR, LAN, LAS, KR, JP, EUNE, EUW, TR, RU, OCE, PH2, SG2, TH2, TW2, VN2")
    server = input("Enter Server: ").upper()
    if server in ("NA", "BR", "LAN", "LAS"):
        region_server = "americas"
    elif server in ("KR", "JP", "PH2", "OCE", "SG2", "TH2", "TW2", "VN2"):
        region_server = "asia"
    elif server in ("EUNE", "EUW", "TR", "RU"):
        region_server = "europe"
        
    return region_server, game_name, tag_line, server

def get_puuid(server, game_name, tag_line):
    url = f"https://{server}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}?api_key={riot_api_key}"
    response = requests.get(url)
    response.raise_for_status()  # Raise exception for HTTP errors
    return response.json()["puuid"]

def get_matches(server, puuid):
    if server in ("NA", "BR", "LAN", "LAS"):
        new_server = "americas"
    elif server in ("KR", "JP"):
        new_server = "asia"
    elif server in ("EUNE", "EUW", "TR", "RU"):
        new_server = "europe"
    elif server in ("PH2", "OCE", "SG2", "TH2", "TW2", "VN2"):
        new_server = "sea"

    url = f"https://{new_server}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?queue=450&start=0&count=100&api_key={riot_api_key}"
    response = requests.get(url)
    response.raise_for_status()  # Raise exception for HTTP errors
    return response.json()

def get_match_info(server, match_id):
    if server in ("NA", "BR", "LAN", "LAS"):
        new_server = "americas"
    elif server in ("KR", "JP"):
        new_server = "asia"
    elif server in ("EUNE", "EUW", "TR", "RU"):
        new_server = "europe"
    elif server in ("PH2", "OCE", "SG2", "TH2", "TW2", "VN2"):
        new_server = "sea"

    url = f"https://{new_server}.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={riot_api_key}"
    response = requests.get(url)
    response.raise_for_status()  # Raise exception for HTTP errors
    match_data = response.json()
    return match_data # json.dumps(match_data, indent = 4)

def game_stats(info, puuid):
    match_info = info["info"]["participants"]

    # Search for the player with the puuid
    player_index = None
    for i, participant in enumerate(match_info):
        if participant["puuid"] == puuid:
            player_index = i
            break

    if player_index is None:
        return None  # Player not found in the match

    # Get the win status
    win = match_info[player_index]["win"]

    return win

def win_rate_checker(stats):
    win = 0
    lose = 0
    if stats == True:
        win += 1
    else:
        lose += 1
    return win, lose
if __name__ == "__main__":
    main()
