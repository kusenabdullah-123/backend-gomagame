from flask import Flask, send_file
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from os import path
# from resources.GallerysApi import GallerysApi


app = Flask(__name__)
api = Api(app)

version = "v1"


# class GalleryApi(Resource):

#     def get(self, idGallery):
#         gallery = getGalleryById(idGallery)
#         return {'gallery': gallery}

class Image(Resource):
    @api.representation("text/html")
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str,
                            help='name must be in string')
        args = parser.parse_args()
        image = path.join(path.realpath(""), f"images/{args['name']}.webp")
        return send_file(image, mimetype="image/webp")

# api.add_resource(GallerysApi, f'/{version}/gallery/')
# api.add_resource(GalleryApi, f'/{version}/gallery/<int:idGallery>')


api.add_resource(Image, f'/{version}/images/', endpoint="images")

if __name__ == '__main__':
    app.run()
