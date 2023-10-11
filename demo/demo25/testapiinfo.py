# coding:utf-8

import pymysql
def mysql_db():
    con = pymysql.connect(
        host='192.168.7.130',
        port=3306,
        database='aefun_databese',
        charset='utf8mb4',
        user='root',
        password='admin')
    with con.cursor() as cursor:
        sql = "select * from ad_info_table;"
        cursor.execute(sql)
        datas = cursor.fetchall()
        print(datas)
        con.commit()
        con.close()

if __name__ == '__main__':
    mysql_db()