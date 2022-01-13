from flask import Flask
from flask_restful import Api
from flask_cors import CORS
import controller.gallery as Gallery

app = Flask(__name__)
api = Api(app)

version = "v1"

api.add_resource(Gallery, f'/{version}/gallery')


if __name__ == '__main__':
    app.run()
