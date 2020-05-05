from tools.api import request_tool
from tools.data import excel_tool
import xlrd
from tools.os import os_tool
from xlutils.copy import copy
import xlwt

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
    # 只有转JSON过后才能取下标,不然会报错
    code = rs['code']
    #取出rs中cood下标存入变量COOD
    data = rs['data']
    assert code == 2000
    # 断言 响应cood是否等于2000
    phone = rs['data'][0]['phone']
    cstId = rs['data'][0]['cstId']

    print(phone)
    print(cstId)


    d = {'accountName': 'dengxin12'}
    headers = { "content-type": "application/json;charset=UTF-8"}
    re = request_tool.get(url='http://api.yansl.com:8084/acc/getAccInfo',params=d,headers=headers)
    re_json = re.json()
    cstId1 = re_json['cstId']
    phone1 = re_json['accoutId']
    print(cstId1)
    print(phone1)

    # 调用函数,设置单元格背景颜色

    Pattern = xlwt.Pattern()
    Pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    Pattern.pattern_fore_colour = 2
    orig = xlrd.open_workbook(
        'E:\\测试文件\\test.xls'.format(os_tool.get_root_path()),
        formatting_info=True)# formatting_info还没有对新版本的xlsx的格式完成兼容。
    style = xlwt.XFStyle()
    style.pattern = Pattern

    # cpoy函数用于复制该变量的值,也就是复制一份新的excel数据给wb变量
    wb = copy(orig)
    # 根据索引获取第一页的sheet数据 赋值给s变量
    s = wb.get_sheet(0)
    f = 0

    if phone != phone1:
        f = 1
        s.write(5, 9, '手机号查询:' + str(phone) + '用户名查询:' + str(phone), style)
      # 如果phone != phone1,f=1,s在表格5行9列写入()里的值
    if cstId != cstId1:
        f = 1
        s.write(6, 9, '手机号查询-cst:' + str(cstId) + '用户名查询-cst:' + str(cstId1), style)
        # 如果f变量= 1的时候执行里面的代码
    if (f == 1):
        # f = 1 将处理之后的excel数据存入指定的本地路径下
        time = excel_tool.datat_time()
        wb.save(
            os_tool.get_root_path() +
            'E:\\测试文件\\测试数据1.xls' % ())

        print("failed")
        # 反之执行里面的代码
    else:
        print("pass")
