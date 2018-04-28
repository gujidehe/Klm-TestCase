#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/28 17:30
# @Author  : WangDonghe
# @Software: PyCharm

import unittest
import requests
import time
class Comment(unittest.TestCase):
    data = {'videoId':'859f3459bd06','content':'哈哈','replayId':'','videoTime':''}
    Cookie_str = {
        'kToken': 'MXwzMzMzNjE4MnwlRTYlQkIlQTIlRTUlQjAlOEYlRTUlQjAlOEZ8MTUyMDMwNDAwNDA5OHxNeUJRRHw4NjlmMGQ1YmIwZTg5YzdlMjJiNDE5'}
    L=[]
    def cc(self,data,Cookie_str,commentId,L):
        self.data=data
        self.Cookie_str=Cookie_str
        self.commentId=commentId
        self.L=L
    def test_addComment(self):
        url='http://t.api.klm123.com/comment/addComment/v2'
        r=requests.post(url=url,data=self.data,cookies=self.Cookie_str).json()
        print(r)
        commentId= r['data']['commentId']
        self.L.append(commentId)
        assert r['msg']=='成功'
        time.sleep(5)
    def test_deleteComment(self):
        url = 'http://t.api.klm123.com/comment/deleteComment'
        data = {'commentId':self.L[0]}
        print(data)
        r = requests.post(url=url,data=data,cookies=self.Cookie_str).json()
        print(r)
        assert r['msg'] == '成功'
