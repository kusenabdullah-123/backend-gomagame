from model.utilitys import openFile

file = "game"


def getAllGame():
    game = openFile(file)
    return game["game"]


def filtered(idGame, data):
    for item in data:
        if item["idGame"] == idGame:
            obj = item
    return obj


def getGameById(idGame):
    game = openFile(file)
    return filtered(idGame, game['game'])
