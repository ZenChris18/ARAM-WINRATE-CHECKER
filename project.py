import requests
from dotenv import load_dotenv
import os

load_dotenv()
riot_api_key = os.environ.get("riot_api_key")

def main():
    server, game_name, tag_line = get_username_from_user()
    puuid = get_puuid(server, game_name, tag_line)
    matches = get_matches(server, puuid)
    print(matches)

def get_username_from_user():
    game_name = input("Enter your username: ").replace(" ", "_")
    tag_line = input("Enter your tagline: ")
    server = input("Enter Server: ")
    return server, game_name, tag_line

def get_puuid(server, game_name, tag_line):
    url = f"https://{server}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}?api_key={riot_api_key}"
    response = requests.get(url)
    response.raise_for_status()  # Raise exception for HTTP errors
    return response.json()["puuid"]

def get_matches(server, puuid):
    url = f"https://sea.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?queue=450&start=0&count=100&api_key={riot_api_key}"
    response = requests.get(url)
    response.raise_for_status()  # Raise exception for HTTP errors
    return response.json()

if __name__ == "__main__":
    main()
