
from model.utilitys import openFile

file = "gallery"


def getAllGallery():
    gallerys = openFile(file)
    return gallerys["gallery"]


def filtered(idGallery, data):
    for item in data:
        if item["idGallery"] == idGallery:
            obj = item
    return obj


def getGalleryById(idGallery):
    gallery = openFile(file)
    return filtered(idGallery, gallery['gallery'])
