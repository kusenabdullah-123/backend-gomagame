from model.utilitys import openFile

file = "article"


def getAllArticle():
    articles = openFile(file)
    return articles["article"]


def filtered(idArticle, data):
    for item in data:
        if item["idArticle"] == idArticle:
            obj = item
    return obj


def getArticleById(idArticle):
    article = openFile(file)
    return filtered(idArticle, article['article'])
