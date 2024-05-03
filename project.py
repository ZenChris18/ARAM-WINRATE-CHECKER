import requests

riot_api_key = "RGAPI-a55047de-6c63-410c-ac09-952cbc3b8c18"

def main():
    username = get_username()
    response = get_puuid(username)
    print(response)

def get_username():
    game_name = input("Enter your username: ").replace(" ", "_")
    tag_line = input("Enter your tagline: ")
    return (f"https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}?api_key={riot_api_key}")


def get_puuid(a):
    code = requests.get(a)
    puuid = code.json()["puuid"]
    return puuid
    

if __name__ == "__main__":
    main()