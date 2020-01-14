from flask import Flask
from flask_restplus import Resource, Api
from flask import request
from flask_cors import CORS

from bo.send_mail import *

app = Flask(__name__)
api = Api(app)

CORS(app, resources={r"/*": {"origins": "*"}})


# @api.param('message')
@api.route('/mail')
class SendMail(Resource):
    def get(self):
        try:
            # message = request.args.get('message')
            send()
            return {'message': 'Mail bien envoye'}
        except:
            self.api.abort(500, 'Error while trying to send mail')


if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=473)
