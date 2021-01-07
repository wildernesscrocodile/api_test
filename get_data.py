#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :get_cookie.py
# @Time      :2020/6/9 16:37
# @Author    :麻花
from tools import project_path
import pandas as pd
from tools.read_config import ReadConfig

class GetData:
    Cookie = None
    loan_id = None
    check_list=eval(ReadConfig().get_config(project_path.case_config_path,'CHECKLEAVEAMOUNT','check_list'))
    NoRegTel = pd.read_excel(project_path.test_case_path,sheet_name='init').iloc[0,0]
    normal_tel = pd.read_excel(project_path.test_case_path,sheet_name='init').iloc[1,0]
    admin_tel = pd.read_excel(project_path.test_case_path,sheet_name='init').iloc[2,0]
    load_member_id = pd.read_excel(project_path.test_case_path,sheet_name='init').iloc[3,0]
    memberID = pd.read_excel(project_path.test_case_path,sheet_name='init').iloc[4,0]
    pwd=pd.read_excel(project_path.test_case_path,sheet_name='init').iloc[5,0]

if __name__ == '__main__':
    df=pd.read_excel(project_path.test_case_path,sheet_name='init')
    # print(df.iloc[0,0])
    print(GetData.normal_tel)