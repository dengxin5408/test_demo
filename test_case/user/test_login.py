from tools.api import request_tool
import pytest

id2=['正确数据',
     '用户名错误',
     '密码错误']
# case的标题,参数存入ids中
cases=[('xiewu1','qYFn2Y4a',2000),
       ('xiewu','qYFn2Y4a',9999),
       ('xiewu1','qYFn2Y4',9999)]
# []里为请求参数,()里为一个完整的case,和预期结果
@pytest.mark.parametrize('name,pwd,assertion',cases,ids=id2)
def test_login(name,pwd,assertion):
    url='http://www.guoyasoft.com:8084/login'
    req={
      "pwd": pwd,
      "userName": name
    }
    resp=request_tool.post_json(url,json=req)
    print(resp)
    resp_json = resp.json()
    code=resp_json['code']
    print(code)
    data=resp_json['data']
    assert code == assertion




