import unittest
import requests
import json
from selenium import webdriver
class LogInApi(unittest.TestCase):
    def test_LogIn(slef):
        url = "http://t.passport.klm123.com//login/loginByMobile/v2"
        with open('E:\PycharmProjects\\untitled\data\\test.txt','r') as f:
            for data1 in f:
                data=eval(data1)######str转dict############
                #print(data)
                a=str(data['mobile'])
                if len(a)!=11:
                    print('您输入的手机号有误,错误手机号为',a)
                r = requests.post(url=url,data=data).text
                print(type(r))
                i=json.loads(r)
                # print(i)
                assert i["msg"]=='成功'
