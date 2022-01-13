from flask_restful import Resource
from model.galleryModel import getAllGallery


class Gallery(Resource):
    def get(self):
        gallery = getAllGallery()
        return {'gallery': gallery}
