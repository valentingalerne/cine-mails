from flask import Flask
from flask import request
from flask_restplus import Resource, Api
from flask_cors import CORS

from bo.send_mail import *

app = Flask(__name__)
api = Api(app)

CORS(app, resources={r"/*": {"origins": "*"}})


@api.route('/mail')
class SendMail(Resource):
    def post(self):
        '''Route permettant d'envoyer un mail'''
        try:
            error = request.json['error']
            errorName = request.json['error_name']
            send(error, errorName)
            return {'message': 'Mail bien envoye'}
        except:
            self.api.abort(500, 'Error while trying to send mail')


if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=473)
