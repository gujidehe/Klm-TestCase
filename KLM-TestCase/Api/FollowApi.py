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

Cookie_str = {
    'kToken': 'MXwzMzMzNjE4MnwlRTYlQkIlQTIlRTUlQjAlOEYlRTUlQjAlOEZ8MTUyMDMwNDAwNDA5OHxNeUJRRHw4NjlmMGQ1YmIwZTg5YzdlMjJiNDE5'}
data = {'followId': 110604}
data1={'pageSize':1,'pageNo':1}
class Follow(unittest.TestCase):
    def test_addFollow(self):
        url='http://t.api.klm123.com/fans/addFollow'
        r=requests.post(url=url,data=data,cookies=Cookie_str).json()
        print(r)
        assert r['msg']=='OK'
    def test_cancelFollow(self):
        url='http://t.api.klm123.com/fans/cancelFollow'
        i=requests.post(url=url,data=data,cookies=Cookie_str).json()
        print(i)
        assert i['msg'] == 'OK'
    def test_getFollowList(self):
        url = 'http://t.api.klm123.com/fans/getFollowList'
        r= requests.get(url=url,data=data1,cookies=Cookie_str).json()
        print(r)
        assert r['msg'] == '成功'


