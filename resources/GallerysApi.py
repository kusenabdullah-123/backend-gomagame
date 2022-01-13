from flask_restful import Resource
from model.galleryModel import getAllGallery


class GallerysApi(Resource):
    def get(self):
        gallerys = getAllGallery()
        return {'gallerys': gallerys}
