#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :http_request.py
# @Time      :2020/6/7 21:29
# @Author    :麻花

import requests
from tools.my_log import MyLog

my_logger=MyLog()
class HttpRequest:

    @staticmethod
    def http_request(url,data,http_method,cookie=None):
        try:
            if http_method.upper() == "GET":
                res = requests.get(url,data,cookies=cookie)
            elif http_method.upper() == "POST":
                res = requests.post(url,data,cookies=cookie)
            else:
                my_logger.info("输入的请求方法不对")
        except Exception as e:
            my_logger.error("请求报错了",e)
            raise e
        return res



if __name__ == '__main__':

    # login_url = 'http://14.23.47.110:9203/centralized/login/login'
    # login_data = {"relationNo":"2001030169","userPassword":"1bbd886460827015e5d605ed44252251"}
    #
    # queryTeacherInfo_url = 'http://14.23.47.110:9203/assurance/public/queryTeacherInfo'
    # queryTeacherInfo_data = {"teacherNo":"2001030169","token":"9f12fdef2c984c21a05f11d842fd7188"}

    # login_url = 'http://14.23.47.109:8180/ybt/auth/login'
    # login_data = {"username": "Z8880001", "password": "123", "rememberMe": "0"}
    #
    # formlist_url = 'http://14.23.47.109:8180/ybt/form/list?pageNum=1&pageSize=10'
    # formlist_data = {"formName":"","taskStatus":"","status":"","formFolderId":""}

    login_url = 'http://175.6.27.63:19394/centralized/login/login'
    login_data = {"relationNo":"102030","userPassword":"e10adc3949ba59abbe56e057f20f883e"}

    queryTeacherInfo_url = 'http://175.6.27.63:19394/assurance/personalPlanInfo/updatePmPersonalPlanInfo'
    queryTeacherInfo_data = {"planName":"test","planLayer":"GRFZGH","relationPlanNo":"",
                             "startDate":"2020-06-24","endDate":"2020-06-24","planDesc":"","createrNo":"102030",
                             "createrName":"钟慧林","planNo":"P202006240953201753158716",
                             "token":"6adc0dbbbf394a0d8c01eb7a62909bde"}

# res=requests.post(createSysUser_url,createSysUser_data)

# createSysUser_url = 'http://14.23.47.109:8180/ybt/system/setting/user/createSysUser'
# createSysUser_data = {"name":"张三","userCode":"Z0000003","userName":"Z0000003",
#         "departId":"b7744acfcbd511e98152005056b227b6","departName":"教学评估办公室"}
# # res=requests.post(createSysUser_url,createSysUser_data)
# print(res.json())
#     header = {"Content-Type": "application/json","User-Agent": "Mozilla/5.0 "}
#     header = {"Content-Type": "application/json"}
    login_res = HttpRequest().http_request(login_url,login_data,"post")
    queryTeacherInfo_res= HttpRequest().http_request(queryTeacherInfo_url,queryTeacherInfo_data,"post",cookie=login_res.cookies)
    # formlist1_res= requests.post(formlist_url,formlist_data,cookies=login_res.cookies)

    print("表单列表有：{0}".format(login_res.json()))
    print("表单列表有：{0}".format(queryTeacherInfo_res.json()))
    # print("表单列表有：{0}".format(formlist1_res.json()))


