import json


def getAllGallery():
    with open('../database/gallery.json') as galleryJson:
        galleryObj = json.load(galleryJson)
        galleryJson.close()
    return galleryObj
