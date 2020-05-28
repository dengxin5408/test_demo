from tools.api import request_tool
from tools.data import random_tool
import openpyxl



def test_sign():

    url='http://api.yansl.com:8084/signup'

    phone=random_tool.random_tell()
    pwd=random_tool.random_pwd()
    re_pwd=pwd
    user_name=random_tool.random_name_pinyin()
    num=random_tool.random_number(10,99)

    req={
          "phone": phone,
          "pwd": pwd,
          "rePwd": re_pwd,
          "userName": user_name+str(num)
        }
    resp=request_tool.post_json(url,json=req)
    resp_json = resp.json()
    code= resp_json['code']
    print(code)
    data= resp_json['data']
    assert code== 2000

    if code==2000:
     print("测试成功")

    else:
     print("测试失败")






