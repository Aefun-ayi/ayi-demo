import flask

api = flask.Flask(__name__)


@api.route('/version', methods=['get'])
# get方式访问
def version():
    ren = '1.1'
    return ren

if __name__ == '__main__':
    api.run(port=8008, debug=True, host='0.0.0.0')