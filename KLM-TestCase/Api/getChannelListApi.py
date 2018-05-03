#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/3 15:41
# @Author  : WangDonghe
# @Software: PyCharm
import unittest
import requests
class ChannelList(unittest.TestCase):
    def test_getChannelList(self):
        url = 'http://t.api.klm123.com/channel/getChannelList/v4'
        r=requests.get(url=url).json()
        assert r['msg']=='成功'
        for i in range(0, len(r['data']['channels']) - 1):
            print(r['data']['channels'][i]['id'])