#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/27 17:04
# @Author  : WangDonghe
# @Site    : 
# @File    : all_case.py
# @Software: PyCharm

import unittest
import os
import time
import HTMLTestRunner
case_path = os.path.join(os.getcwd(),'Api')
def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,pattern='*Api.py',top_level_dir=None)
    print(discover)
    return discover
def report():
    now = time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(time.time()))
    print(now)
    fp = open('E:\PycharmProjects\\untitled\\report\\' + now + ' 测试报告.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'接口自动化测试报告',
        description=u'用例执行情况：')
    runner.run(all_case())
    fp.close()
