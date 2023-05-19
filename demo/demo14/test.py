from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.header import Header

app = Flask(__name__)

# 配置邮箱服务器
mail_host = "smtp.163.com"
mail_user = "email@163.com"  # 发件人邮箱
mail_pass = "email_password"  # 发件人邮箱密码
sender = mail_user

# 收件人邮箱
receiver = "manchengkj6@163.com"

# 定义邮件内容模板
email_template = '''
收到一条新的信息：
姓名：{}
邮箱：{}
内容：{}
'''

@app.route('/submit', methods=['POST'])
def submit_form():
    # 获取POST请求参数
    name = request.json.get('name')
    email = request.json.get('email')
    content = request.json.get('content')

    # 构造邮件内容
    email_content = email_template.format(name, email, content)

    # 发送邮件
    message = MIMEText(email_content, 'plain', 'utf-8')
    message['From'] = Header("Sender Name", 'utf-8')
    message['To'] = Header("Receiver Name", 'utf-8')
    message['Subject'] = Header("New Message", 'utf-8')
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receiver, message.as_string())
        smtpObj.quit()
        return jsonify({'message': 'success'})
    except Exception as e:
        return jsonify({'message': str(e)}), 500

if __name__ == '__main__':
    app.run()