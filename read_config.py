#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :read_config.py
# @Time      :2020/6/10 14:55
# @Author    :麻花

import configparser

class ReadConfig:

    @staticmethod
    def get_config(file_path,section,option):
        cf = configparser.ConfigParser()
        cf.read(file_path)
        return cf[section][option]

if __name__ == '__main__':
    from tools.project_path import *
    print(ReadConfig.get_config(case_config_path,'MODE','mode'))