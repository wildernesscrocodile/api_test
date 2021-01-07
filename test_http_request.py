#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test_http_request.py
# @Time      :2020/6/9 16:28
# @Author    :麻花

import unittest
from tools.http_request import HttpRequest
from ddt import ddt,data
from tools.do_excel import DoExcel
from tools.project_path import *
from tools.my_log import MyLog
from tools.get_data import GetData
from tools.do_mysql import DoMysql

my_logger=MyLog()

test_data = DoExcel().get_data(test_case_path)

@ddt
class TestHttpRequest(unittest.TestCase):

    def setUp(self):
        pass

    @data(*test_data)
    def test_api(self,item):

        my_logger.info('开始执行用例{0}:{1}'.format(item['case_id'],item['title']))
        if item['data'].find('$loan_id')!=-1:
            if getattr(GetData,'load_member_id')==None:
                query_sql='SELECT `id`  FROM `assurance32_hngy_test`.`pm_personal_plan_info` ' \
                          'WHERE `plan_no` = {0}'.format(getattr(GetData,'load_member_id'))
                loan_id=DoMysql().do_mysql(query_sql)[0][0]
                item['data']=item['data'].repalce('${load_id}',loan_id)
                setattr(GetData,'load_id',loan_id)
                my_logger.info(loan_id)

            else:
                my_logger.info(getattr(GetData,'load_id'))
                item['data']=item['data'].repalce('${load_id}',str(getattr(GetData,'load_id')))


        my_logger.info('获取到的请求数据是:{0}'.format(item['data']))
        if item['check_sql']!=None:
            my_logger.info('此条用例需要做数据库校验:{0}'.format(item['title']))
            query_sql = eval(item['check_sql'])['sql']  # 拿到了sql语句注意是存在字典里面的(E
            # 开始查询
            Before_Amount = DoMysql.do_mysql(query_sql,1)[0]
            my_logger.info('用例:{0}请求之前的余额是:{1}'.format(item['title'],Before_Amount))

            my_logger.info('-----------开始http接口请求----------')
            res = HttpRequest.http_request(item['url'], eval(item['data']), item['http_method'],
                                           getattr(GetData, 'Cookie'))
            my_logger.info('-----------完成http接口请求----------')

            After_Amount = DoMysql.do_mysql(query_sql,1)[0]
            my_logger.info('用例:{0}请求之后的余额是:{1}'.format(item['title'],After_Amount))

            #检查结果
            if abs(Before_Amount-After_Amount)==0:
                my_logger.info('数据库余额检查通过')
                check_sql_result='数据库检查通过'
            else:
                my_logger.info('数据库余额未检查通过')
                check_sql_result = '数据库未检查通过'
            DoExcel.write_back(test_case_path,item['sheet_name'],item['case_id']+1,10,check_sql_result)

        else:
            my_logger.info('此条用例不需要做数据库校验')
            my_logger.info(' ----------开始http接口请求----------')
            res = HttpRequest.http_request(item['url'], eval(item['data']), item['http_method'],
                                           getattr(GetData, 'Cookie'))
            my_logger.info('-----------完成http接口请求----------')

        # else:
        #     res = HttpRequest.http_request(item['url'], eval(item['data']), item['http_method'],
        #                                    getattr(GetData, 'Cookie'))

        if res.cookies:
            setattr(GetData,'Cookie',res.cookies)
        try:
            self.assertEqual(str(item['expected']),res.json()['code'])
            Testresult = 'PASS'
        except AssertionError as e:
            Testresult = 'FAILED'
            my_logger.info("执行用例出错：{0}".format(e))
            raise e
        finally:
            print(item['title'])
            DoExcel.write_back(test_case_path,item['sheet_name'],item['case_id']+1,8,str(res.json()))
            DoExcel.write_back(test_case_path,item['sheet_name'],item['case_id']+1,9,str(Testresult))

            my_logger.error("获取到的结果是：{0}".format(res.json()))

    def tearDown(self):
        pass

if __name__ == '__main__':
    TestHttpRequest().test_api()
