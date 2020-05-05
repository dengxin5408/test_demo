from tools.api import request_tool
from tools.data import random_tool
from tools.data import identity_tool
import json
import re


def test_shiming(pub_dic):

    url='http://www.guoyasoft.com:8084/cst/realname'
    headers = {
            'token': pub_dic,
            'charset': 'UTF-8'
        }

    email = random_tool.random_email()
    sex = random_tool.random_sex()  # 随机生成男(1)或女(0)
    cst_name=random_tool.random_name(sex)
    area=random_tool.random_area()
    area_id=area['code']
    area_name=area['name']
    province=area['province']
    city=area['city']
    birth_days=random_tool.random_birthday(18,35)
    cert_no=identity_tool.generate_id(sex=sex,area_id=area_id,birth_days=birth_days)
    cst_email = random_tool.random_email()
    req={
      "cstId": 	7,
       "birthday": birth_days,
       "certno": cert_no,
       "city": city,
       "cstName": cst_name,
       "email": cst_email,
       "province": province,
       "sex": sex
    }
    print(req)
    resp=request_tool.post_json(url,headers=headers,json=req)