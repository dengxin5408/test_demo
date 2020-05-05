from tools.api import request_tool
import pytest



id1 = ['正确数据',
           '长度小于11位',
           '不存在此用户',
           '非法字母',
           '非法字符串'
           ]
     # id1内为case的标题,参数存入ids中
     # cases为具体测试参数值
case1 = [('15123274197', 2000),
             ('2354668', '没有此手机号'),
             ('15235359977', '没有此手机号'),
             ('dsjdk','没有此手机号'),
             ('@#%$.*','没有此手机号')
            ]
@pytest.mark.parametrize('phone,assertion',case1,ids=id1)#ids变量不可更改
def test_chaxun(pub_dic,phone,assertion): # get请求query数据
    headers = {
        'token': pub_dic
    }
    # 将公共方法上传,保持已登录
    d = {"phone":'phone'}
    # 将params存入变量d中
    r = request_tool.get(url="http://api.yansl.com:8084/cst/getCustomer",params=d,headers=headers)
    # 请求方法为get,将传入URL,参数,token,存入变量R中
    rs = r.json()
    # 只有转JSON过后才能取下标,不然一定会报错
    code = rs['code']
    #取出rs中cood下标存入变量COOD
    data = rs['data']
    message = rs['message']
    assert code == assertion or message == assertion# 根据实际接口返回的响应进行断言


