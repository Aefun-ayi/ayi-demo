from mainmain import Api
import flask

api = flask.Flask(__name__)

@api.route('/ad', methods=['GET'])
def ad():
    a = Api()
    return a

if __name__ == '__main__':
  api.run(port=8100,debug=True,host='0.0.0.0')