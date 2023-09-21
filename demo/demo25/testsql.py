from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@192.168.7.43:2023/my_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  #设置sqlalchemy自动更新跟踪数据库（数据被修改时，修改模型类）
app.config['SQLALCHEMY_ECHO'] = True  # 查询时会显示原始SQL语句

# 创建组件对象
db = SQLAlchemy(app)


# 构建模型类  类->表  类属性->字段  实例对象->记录
class User(db.Model):
    __tablename__ = 'AdInfoTable'  # 设置表名, 表名默认为类名小写
    # id = db.Column(db.Integer, primary_key=True)  # 设置主键, 默认自增
    phone_mobile = db.Column('package_info', db.String(512), unique=True, primary_key=True)  # 设置字段名 和 唯一约束
    phone_name = db.Column('ad_name', db.String(1024), index=True)  # 设置默认值约束 和 索引


if __name__ == '__main__':
    with app.app_context():
        # 删除所有继承自db.Model的表
        db.drop_all()
        # 创建所有继承自db.Model的表
        db.create_all()
    app.run(debug=True)
