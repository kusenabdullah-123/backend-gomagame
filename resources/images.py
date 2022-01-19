from flask import send_file, make_response
from flask_restful import Resource, reqparse
from os import path


class Image(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str,
                            help='name must be in string')
        args = parser.parse_args()
        image = path.join(path.realpath(""), f"images/{args['name']}.webp")
        response = make_response(send_file(image, mimetype="image/webp"))
        response.headers["Content-Type"] = "text/html"
        return send_file(image, mimetype="image/webp")
