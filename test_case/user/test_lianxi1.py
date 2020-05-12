import pytest
from tools.api import request_tool
import requests





def test_chaxun(pub_dic): # get请求query数据
    headers = {
        'token': pub_dic
    }
    # 将公共方法上传,保持已登录
    d = {"phone":'15123274197'}
    # 将params存入变量d中
    r = request_tool.get(url="http://api.yansl.com:8084/cst/getCustomer",params=d,headers=headers)
    # 请求方法为get,将传入URL,参数,token,存入变量R中
    rs = r.json()
    # 只有转JSON过后才能取下标,不然一定会报错
    code = rs['code']
    #取出rs中cood下标存入变量COOD
    data = rs['data']
    assert code == 2000
    # 断言 响应cood是否等于2000

def test_path(test_login2):


    headers ={'token':test_login2}
    r = request_tool.get(url="http://api.yansl.com:8084/cst/getAll/1/4",headers=headers)
    rs = r.json()
    code = rs["code"]
    data = rs["data"]
    if code == 2000 and data != "":
    # 多个断言结果校验
        print("测试成功")

    else:
        print("测试失败")


def test_xiazai(pub_dic):

    f = open("C:\softwoer\dev\test_api\test_file\demo\excel_test.xls",'rb')
    files = {'file':f}


    r = request_tool.post(url="http://api.yansl.com:8084/product/downRepertoryTemplate",files=files)

    r_json = r.json()
    code = r_json['code']
    data = r_json['data']
    assert code == 2000

    print(r.status_code)
    print(r.text)
    f.close()




def test_DJ(pub_dic):
    headers = {"token":'pub_dic'}

    data = {
        "userName":'jinqian78'
    }
    r = request_tool.post(url="http://api.yansl.com:8084/user/lock",data=data,headers=headers)
    r_json = r.json()
    print(r.status_code,r.text,r.request.body)
    r_json = r.json()
    code = r_json['code']
    data = r_json['data']
    assert code == 2000


def test_cz(pub_dic):

     req = {
         "accountName": "jinqian78",
         "changeMoney": 1000
     }
     r = request_tool.post_json(url="http://api.yansl.com:8084/acc/recharge",json=req)
     req_json = r.json()
     code = req_json["code"]
     data = req_json["data"]
     assert code == 2000








