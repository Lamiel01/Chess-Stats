LICHESS_TOKEN = 'YOUR TOKEN'
import json
import berserk

session = berserk.TokenSession(LICHESS_TOKEN)
client = berserk.Client(session=session)


"""
with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
"""

name = 'Lamiel01'
#name = 'P4ssion'

def test(name) -> None:
    data = client.users.get_public_data(name)
    print(type(client.users.get_public_data(name)))
    print(client.users.get_puzzle_activity(name))
    return 1

def getBasicInfo(name) -> tuple:
    info = client.users.get_public_data(name)
    ID = info["id"]
    Username = info['username']
    Active = info['online']
    return ID, Username, Active

def getBasicsStats(name) -> tuple:
    info = client.users.get_public_data(name)
    BLITZ = info['perfs']['blitz']['rating']
    RAPID = info['perfs']['rapid']['rating']
    PUZZLE = info['perfs']['puzzle']['rating']
    return BLITZ, RAPID, PUZZLE

def blitz(name) -> tuple:
    info = client.users.get_public_data(name)
    RATING = info['perfs']['blitz']['rating']
    GAMES = info['perfs']['blitz']['games']
    return RATING, GAMES

def bullet(name) -> tuple:
    info = client.users.get_public_data(name)
    RATING = info['perfs']['bullet']['rating']
    GAMES = info['perfs']['bullet']['games']
    return RATING, GAMES

def rapid(name) -> tuple:
    info = client.users.get_public_data(name)
    RATING = info['perfs']['rapid']['rating']
    GAMES = info['perfs']['rapid']['games']
    return RATING, GAMES

print(test(name))
