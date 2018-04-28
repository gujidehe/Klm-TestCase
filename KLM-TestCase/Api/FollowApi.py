#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/16 14:43
# @Author  : WangDonghe
# @Site    : 
# @File    : FollowApi.py
# @Software: PyCharm

import unittest
import requests
import json
class Follow(unittest.TestCase):
    Cookie_str = {
        'kToken': 'MXwzMzMzNjE4MnwlRTYlQkIlQTIlRTUlQjAlOEYlRTUlQjAlOEZ8MTUyMDMwNDAwNDA5OHxNeUJRRHw4NjlmMGQ1YmIwZTg5YzdlMjJiNDE5'}
    data = {'followId': 110604}
    def cc(self,Cookie_str,data):
        self.Cookie_str=Cookie_str
        self.data=data
    def test_addFollow(self):
        url='http://t.api.klm123.com/fans/addFollow'
        r=requests.post(url=url,data=self.data,cookies=self.Cookie_str).json()
        print(r)
        assert r['msg']=='OK'


    def test_cancelFollow(self):
        url='http://t.api.klm123.com/fans/cancelFollow'
        i=requests.post(url=url,data=self.data,cookies=self.Cookie_str).json()
        print(i)
        assert i['msg'] == 'OK'


