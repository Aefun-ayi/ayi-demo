import pymysql
from Mysqlconfig import MysqlConfig


class MysqlConnection:
    def __init__(self, host=MysqlConfig.HOST,
                 port=MysqlConfig.PORT,
                 user=MysqlConfig.USER,
                 pwd=MysqlConfig.PASSWORD,
                 db=MysqlConfig.DB):
        self.db = pymysql.connect(host=host,
                                  port=port,
                                  user=user,
                                  password=pwd,
                                  database=db,
                                  charset=MysqlConfig.CHARSET)  # 创建连接
        self.cursor = self.db.cursor()  # 创建游标

    # 查询方法
    def select(self, sql, many=True):
        try:
            self.cursor.execute(sql)  # 执行SQL语句
            if many:
                res = self.cursor.fetchall()
            else:
                res = self.cursor.fetchone()
            return res
        except Exception as e:
            raise e  # 打印日志

    # 增删改方法
    def __do(self, sql):
        try:
            self.cursor.execute(sql)  # 执行SQL语句
        except Exception as e:
            self.db.rollback()  # 如果执行失败要回滚
            # 打日志
            raise e
        else:
            self.db.commit()  # 提交

    def update(self, sql):
        self.__do(sql)

    def insert(self, sql):
        self.__do(sql)

    def delete(self, sql):
        self.__do(sql)

    def exit(self):
        self.cursor.close()  # 关闭游标
        self.db.close()  # 关闭数据库


if __name__ == '__main__':
    db = MysqlConnection()
    # res = db.query('select phone_name from Device_Info where phone_mobile = "21091116UC";')
    res = db.select('select ad_name from adinfotable where package_info = "中台_天气_V1.1.8【1466插件版1.0.12】";')
    db.exit()
    print(res)
    print(type(res[0][0]))
    print(res[0][0])

    li = list(res[0][0].split(","))
    print(li)
    # print(li[1])

