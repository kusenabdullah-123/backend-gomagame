from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS
from model.galleryModel import getGalleryById
from model.ArticleModel import getArticleById
from resources.GallerysApi import GallerysApi
from resources.GameApi import GameApi
from resources.images import Image
from resources.LoginApi import LoginApi
from resources.ArticleApi import ArticleApi


app = Flask(__name__)
api = Api(app)
CORS(app)
version = "v1"


class GalleryApi(Resource):

    def get(self, idGallery):
        gallery = getGalleryById(idGallery)
        return {'gallery': gallery}


class Article(Resource):

    def get(self, idArticle):
        article = getArticleById(idArticle)
        return {'article': article}


api.add_resource(GallerysApi, f'/{version}/gallery/')
api.add_resource(GameApi, f'/{version}/game/')
api.add_resource(LoginApi, f'/{version}/login/')
api.add_resource(ArticleApi, f'/{version}/article/')
api.add_resource(Article, f'/{version}/article/<int:idArticle>')
api.add_resource(GalleryApi, f'/{version}/gallery/<int:idGallery>')
api.add_resource(Image, f'/{version}/images/', endpoint="images")

if __name__ == '__main__':
    app.run()
