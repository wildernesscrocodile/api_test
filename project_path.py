#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :project_path.py
# @Time      :2020/6/10 11:15
# @Author    :麻花

import os

project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
# print(project_path)
#测试用例的路径
test_case_path = os.path.join(project_path,'test_data','test_data.xlsx')
#测试报告路径
test_report_path = os.path.join(project_path,'test_result','html_report','test_api.html')
#配置文件的路径
case_config_path = os.path.join(project_path,'conf','case.config')

#存储日志文件路径
log_path = os.path.join(project_path,'test_result','log','test_api.txt')

if __name__ == '__main__':
    print(case_config_path)