#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :do_mysql.py
# @Time      :2020/6/29 10:47
# @Author    :麻花

import mysql.connector
from tools import project_path
from tools.read_config import ReadConfig


class DoMysql():

    @staticmethod
    def do_mysql(query_sql,state='all'):

        #利用这个类从配置文件读取数据库连接
        db_config = eval(ReadConfig().get_config(project_path.case_config_path,'DB','db_config'))
        # 创建一个数据库连接
        cnn=mysql.connector.connect(**db_config)
        #创建游标
        cursor=cnn.cursor()
        #执行语句
        cursor.execute(query_sql)
        #获取结果 打印结果

        if state==1:
            res=cursor.fetchone()
        else:
            res=cursor.fetchall()

        #关闭游标  关闭连接
        cursor.close()
        cnn.close()

        return res


if __name__ == '__main__':
    from tools.get_data import GetData

    # load_member_id=getattr(GetData, 'load_member_id')
    # print(load_member_id)
    # print(type(load_member_id))

    query_sql = 'SELECT `id`  FROM `assurance32_hngy_test`.`pm_personal_plan_info` ' \
                'WHERE `plan_no` = {0}'.format(getattr(GetData, 'load_member_id'))
    # print(query_sql)
    res=DoMysql().do_mysql(query_sql)
    print(res[0][0])

