#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/2 11:42
# @Author  : WangDonghe
# @Software: PyCharm

import unittest
import requests
class CommentLike(unittest.TestCase):
    data = {'videoId':'d288b526d3f1','commentId':69845}
    def cc(self,data):
        self.data=data
    def test_CommentLike(self):
        url = 'http://t.api.klm123.com/comment/addLike'
        r = requests.post(url=url,data=self.data).json()
        print(r)
        assert r['msg']=='成功'