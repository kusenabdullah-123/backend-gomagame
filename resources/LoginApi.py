from flask_restful import Resource, reqparse
from model.loginModel import cekLogin


class LoginApi(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str,
                            help='nama must be in string')
        parser.add_argument('password', type=str,)
        args = parser.parse_args()
        print(args)
        result = cekLogin(args['username'], args['password'])

        if (result['status'] == "success"):
            return{"message": result['message'], "status": 200}, 200
        else:
            return{"message": result['message'], "status": 401}, 401
