#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/28 10:39
# @Author  : WangDonghe
# @Site    : 
# @File    : LikeApi.py
# @Software: PyCharm
import unittest
import requests
class Like(unittest.TestCase):
    data = {'videoId':'0a015f48bff7'}
    def cc(self,data):
        self.data=data
    def test_addLike(self):
        url = 'http://t.api.klm123.com/like/addLike'
        r = requests.post(url=url,data=self.data).json()
        print(r)
        assert r['msg']== u'点赞成功'
    def test_cancelLike(self):
        url = 'http://t.api.klm123.com/like/cancelLike'
        r = requests.post(url=url, data=self.data).json()
        print(r)
        assert r['msg']== u'取消点赞成功'