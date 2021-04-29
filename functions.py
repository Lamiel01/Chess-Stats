import berserk

session = berserk.TokenSession(LICHESS_TOKEN)
client = berserk.Client(session=session)

name = 'test'

def getBasicInfo(name):
    info = client.users.get_public_data(name)
    ID = info["id"]
    Username = info['username']
    Active = info['online']
    return ID, Username, Active
