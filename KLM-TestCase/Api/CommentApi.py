#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/28 17:30
# @Author  : WangDonghe
# @Software: PyCharm

import unittest
import requests
import time

data = {'videoId': '859f3459bd06', 'content': '哈哈', 'replayId': '', 'videoTime': ''}
Cookie_str = {
    'kToken': 'MXwzMzMzNjE4MnwlRTYlQkIlQTIlRTUlQjAlOEYlRTUlQjAlOEZ8MTUyMDMwNDAwNDA5OHxNeUJRRHw4NjlmMGQ1YmIwZTg5YzdlMjJiNDE5'}
L = []
class Comment(unittest.TestCase):
    def test_addComment(self):
        url='http://t.api.klm123.com/comment/addComment/v2'
        r=requests.post(url=url,data=data,cookies=Cookie_str).json()
        print(r)
        commentId= r['data']['commentId']
        L.append(commentId)
        assert r['msg']=='成功'
        time.sleep(3)
    def test_deleteComment(self):
        url = 'http://t.api.klm123.com/comment/deleteComment'
        data = {'commentId':L[0]}
        print(data)
        r = requests.post(url=url,data=data,cookies=Cookie_str).json()
        print(r)
        assert r['msg'] == '成功'
