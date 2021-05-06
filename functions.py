LICHESS_TOKEN = 'YOUR TOKEN'
import berserk

session = berserk.TokenSession(LICHESS_TOKEN)
client = berserk.Client(session=session)

name = 'Lamiel01'
#name = 'P4ssion'

def test(name) -> None:
    print(client.users.get_public_data(name))

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

#print(f'The basic info of {name} is: BLITZ  RAPID PUZZLE')
#print(getBasicInfo(name))
print(f'El jugador {name} tiene en blitz: (rating, partidas jugadas) ' ,blitz(name))
print(f'El jugador {name} tiene en rapid: (rating, partidas jugadas) ' ,rapid(name))
print(f'El jugador {name} tiene en bullet: (rating, partidas jugadas) ' ,bullet(name))
#print(getBasicsStats(name))
