from tools.api import request_tool
from tools.data import random_tool
import json

def test_xiugai_pwd(pub_dic):


    url='http://api.yansl.com:8084/user/changepwd'
    headers = {
            'token': pub_dic
        }

    pwd = random_tool.random_pwd()
    req={
      "newPwd": pwd,
      "oldPwd": "123456d",
      "reNewPwd": pwd,
      "userName": "xx123456d"
    }
    resp=request_tool.post_json(url,headers=headers,json=req)