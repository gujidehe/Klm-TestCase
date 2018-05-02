#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/2 15:18
# @Author  : WangDonghe
# @Software: PyCharm

import unittest
import requests
class Accusation(unittest.TestCase):
    data = [{'type':1,'reason':'','videoId':'9b7f7d007807'},
            {'type':2,'reason':'','videoId':'9b7f7d007807'},
            {'type':3,'reason':'haldd','videoId':'9b7f7d007807'}]
    def cc(self,data):
        self.data=data
    def test_addAccusation(self):
        url = 'http://t.api.klm123.com/accusation/addAccusation'
        for i in range(0,3):
            r = requests.post(url=url,data=self.data[i]).json()
            print(self.data[i])
            assert r['msg']=='成功'
