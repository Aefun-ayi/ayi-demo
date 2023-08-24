import flask, json

# 实例化api，把当前这个python文件当作一个服务，__name__代表当前这个python文件
api = flask.Flask(__name__)


# 'index'是接口路径，methods不写，默认get请求
@api.route('/test', methods=['get'])
def ad():
    body_data = {"code": 1,
                 "data": {"amount": "0.01",
                          "innerAgreementNo": "39063-2-20230706175553-7-36507",
                          "order5tr": "alipays://platformapi/startapp?appId-60000157GappclearTop-false6startMultApp-yE3asiq",
                          "outTradeNo": "39063-2-20230706175553-7585"},
                 "msg": "操作成功"}
    return json.dumps(body_data, ensure_ascii=False)




if __name__ == '__main__':
  api.run(port=8008,debug=True,host='0.0.0.0') # 启动服务