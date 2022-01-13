from os import path
import json


def getPath(nameFile):
    return path.join(path.realpath(""), f"database/{nameFile}.json")


def openFile(namaFile):
    with open(getPath(namaFile)) as dataJson:
        Obj = json.load(dataJson)
        dataJson.close()
    return Obj
