from flask_restful import Resource
from model.ArticleModel import getAllArticle


class ArticleApi(Resource):
    def get(self):
        articles = getAllArticle()
        return {'articles': articles}
