from tools.api import request_tool
from tools.report.assert_tool import assert_in


def sign_up(phone,pwd,rePwd,userName,expect):

     r = {
  "phone": phone,
  "pwd": pwd,
  "rePwd": rePwd,
  "userName": userName
}

     rq = request_tool.post_json(url="http://api.yansl.com:8084/signup",json=r)

     code = rq["code"]
     assert_in(rq.text,expect)


