from flask import Flask, request

app = Flask(__name__)

@app.route('/api/post', methods=['POST'])
def post_api():
    # 获取 POST 请求中的数据
    data = request.json
    # 对数据进行处理
    # ...
    # 返回处理后的结果
    return {'result': 'success'}



if __name__ == '__main__':
    app.run(port=8008, debug=True, host='0.0.0.0')