from project import get_username_from_user, get_puuid, get_matches, get_match_info, game_stats, win_rate_checker


def test_get_username_from_user():
    assert get_username_from_user() == ("Invalid server. Please try again.",)
    assert get_username_from_user("end") == ("end", None, None, None)
    assert get_username_from_user("yummy_tea", "owo", "PH2") == ("asia", "yummy_tea", "owo", "PH2")

def test_get_puuid():
    assert get_puuid("asia", "yummy_tea", "owo") == "l3wrf6KuxlXEhT5yZN_kJUDmUfrlfI7soEpuinkbyBn_tHnLb6vmywwTZxZM54J7BKMws1vWo01qVw"

def test_get_matches():
    server = "ph2"
    puuid = "l3wrf6KuxlXEhT5yZN_kJUDmUfrlfI7soEpuinkbyBn_tHnLb6vmywwTZxZM54J7BKMws1vWo01qVw"
    matches = get_matches(server, puuid)
    assert isinstance(matches, list)
    assert all(isinstance(match, str) for match in matches)

def test_get_match_info():
    match_id = "example_match_id"
    server = "example_server"
    returned_data = get_match_info(server, match_id)

    # Assert that the function returned a dictionary
    assert isinstance(returned_data, dict)


def test_game_stats():
    info = {"info": {"participants": [{"win": True, "puuid": "invalid_puuid"}]}}
    puuid = "valid_puuid"
    win_status = game_stats(info, puuid)
    assert win_status is None

def test_win_rate_checker():
    win, lose = win_rate_checker(True)
    assert win == 1
    assert lose == 0

