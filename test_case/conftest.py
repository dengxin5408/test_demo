import pytest
from tools.api import request_tool
import json
                                                            
@pytest.fixture(scope='session')  #fixture打下标签作为公共登录拿到token
def pub_dic():

    url='http://api.yansl.com:8084/login'
    req={
      "pwd": "123456dx",
      "userName": "dxhd123456"
    }
    resp=request_tool.post_json(url,json=req)
    resp_json=json.loads(resp.text)
    token=resp_json['data']['token']
    # 取出登录后token,存入变量
    return token


