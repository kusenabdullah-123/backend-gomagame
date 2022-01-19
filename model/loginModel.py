from email import message
from telnetlib import STATUS
from model.utilitys import openFile

file = "login"


def getAllUser():
    users = openFile(file)
    return users["users"]


def cekLogin(username, password):
    users = getAllUser()
    for user in users:
        if(user['username'] == username and user['password'] == password):
            return {
                "status": "success",
                "message": "Success Login"
            }
        else:
            return {
                "status": "failed",
                "message": "Fail Login"
            }
