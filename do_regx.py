#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :do_regx.py
# @Time      :2020/7/14 17:23
# @Author    :麻花

import re

# s='www.Lemfix.com' #目标字符串
# res=re.match('(w)(ww)',s)  #全匹配 头部匹配
# print(res.group(0)) #group()==group(0) 拿到匹配的全字符分组根据你正则表之
#
# s= 'hellelemonfislemon'
# res=re.findall('(le)(mon)',s)#列表在字符串里面找匹配的内容存在列表里面
# #如果有分组就是以元组的形式表现出来 列表嵌套元组
# print (res)


# s='{"relationNo":"${normal_tel}","userPassword":"e10adc3949ba59abbe56e057f20f883e"}'
# res=re.search('\$\{(.*?)\}',s)
# print(res.group())
# print(res.group(1))
from tools.get_data import GetData

class DoRegx:

    @staticmethod
    def do_regx(s):

        while re.search('\$\{(.*?)\}',s) :

            key=re.search('\$\{(.*?)\}',s).group (0)
            value=re.search('\$\{(.*?)\}',s).group(1)
            s=s.replace(key,str(getattr(GetData,value)))
        return s

if __name__ == '__main__':
    s='{"relationNo":"${normal_tel}","userPassword":"${pwd}"}'
    res=DoRegx.do_regx(s)
    print(res)

