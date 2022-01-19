from flask_restful import Resource
from model.GameModel import getAllGame


class GameApi(Resource):
    def get(self):
        games = getAllGame()
        return {'games': games}
