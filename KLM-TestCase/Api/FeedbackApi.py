#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/28 11:21
# @Author  : WangDonghe
# @Software: PyCharm

import unittest
import requests
import json
class Feedback(unittest.TestCase):
    headers = {
        'User-Agent':'DeviceId:KLM_WZ6hMPbjeYADAPzxC44vnwGm;Device:MHA-TL00;IMEI:862001031575132;MAC:54:25:EA:54:91:5A;Channel:zhuoyi;VersionCode:33;SensorId:3667c9b4c9a9a4a2'
    }
    data ={'videoId':'0a015f48bff7','data':'[{"reason":"","type":3}]'}
    print(data)
    def cc(self,data,headers):
        self.data=data
        self.headers=headers
    def test_addFeedback(self):
        url= 'http://t.api.klm123.com/feedback/addFeedback'
        r=requests.post(url=url,data=self.data,headers=self.headers).json()
        print(r)
        assert r['msg']==u'成功'