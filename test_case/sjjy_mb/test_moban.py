import xlrd
from tools import request_tool
from tools import assert_tool
from tools import excel_tool
from config import conf
from tools import os_tool
from xlutils.copy import copy


# 校验展厅漏斗场景的意向和订单卡片 与 渠道漏斗页面的数据对比
def test_kapian_qudaoloudou_yixiang_dingdan(test_login):
    # 获取2张卡片数据
    url = conf.BUICK_API_URL + "/api/dashboard/funnel/intro"
    payload = "{}"
    headers = {
        'Content-Type': "application/json;charset=UTF-8"
    }
    # 发送post请求,获取响应数据
    response = request_tool.post_request(
        url, data=payload, headers=headers, cookies=test_login['cookie'])
    # 遍历获取响应数据inv_quantity的数值
    data1 = response.json()
    # 判断响应码
    assert_tool.assert_equal(response.status_code, 200)
    # 获取response的具体的数据
    yixiang = data1['data'][1]['count']
    dingdan = data1['data'][2]['count']
    print(yixiang)
    print(dingdan)

    # 获取渠道漏斗_全渠道合计的意向和订单数据
    url = conf.BUICK_API_URL + "/api/dashboard/funnel/channel_funnel"
    json = {
        "date_select": "2019-10"
    }
    headers = {
        'Content-Type': "application/json;charset=UTF-8"
    }
    # 发送post请求,获取响应数据
    response = request_tool.post_request(
        url, json=json, headers=headers, cookies=test_login['cookie'])
    # 遍历获取响应数据inv_quantity的数值
    data = response.json()
    # 判断响应码
    assert_tool.assert_equal(response.status_code, 200)
    # 获取response的具体的数据
    yixiang1 = data['data'][5]['new_intention']
    dingdan1 = data['data'][5]['new_order']
    print(yixiang1)
    print(dingdan1)

    # 调用函数,设置单元格背景颜色
    # D:\softwaredata\pycharm\buik-ai-autotest2\download\source_file\关键数据核对.xls
    style = excel_tool.set_cell_style_font_size(10)
    # 读取本地excel download/source_file/别克新逻辑明细数据(LISA使用)20180608.xls
    orig = xlrd.open_workbook(
        r'{0}download/source_file/别克新逻辑明细数据(LISA使用)20180608.xls'.format(os_tool.get_root_path()),
        formatting_info=True)  # formatting_info还没有对新版本的xlsx的格式完成兼容。

    # cpoy函数用于复制该变量的值,也就是复制一份新的excel数据给wb变量
    wb = copy(orig)
    # 根据索引获取第一页的sheet数据 赋值给s变量
    s = wb.get_sheet(0)
    f = 0
    if yixiang != yixiang1:
        f = 1
        s.write(5, 9, '展厅月度整体情况_意向:' + str(yixiang) + '渠道漏斗_到店意向合计:' + str(yixiang1), style)

    if dingdan != dingdan1:
        f = 1
        s.write(6, 9, '展厅月度整体情况_订单:' + str(dingdan) + '渠道漏斗_订单合计:' + str(dingdan1), style)

    # 如果f变量= 1的时候执行里面的代码
    if (f == 1):
        # f = 1 将处理之后的excel数据存入指定的本地路径下
        time = excel_tool.data_time()
        wb.save(
            os_tool.get_root_path() +
            'download/target_file/failed_别克新逻辑明细数据(LISA使用)20180608_%s.xls'%(time))
        print("failed")
    # 反之执行里面的代码
    else:
        print("pass")


# 校验展厅漏斗场景的线索和交车卡片 与 渠道漏斗页面的数据对比
def test_qudaoloudou_xiansuo_jiaoche(test_login):
    # 获取2张卡片数据
    url = conf.BUICK_API_URL + "/api/dashboard/funnel/intro"
    payload = "{}"
    headers = {
        'Content-Type': "application/json;charset=UTF-8"
    }
    # 发送post请求,获取响应数据
    response = request_tool.post_request(
        url, data=payload, headers=headers, cookies=test_login['cookie'])
    # 遍历获取响应数据inv_quantity的数值
    data1 = response.json()
    # 判断响应码
    assert_tool.assert_equal(response.status_code, 200)
    # 获取response的具体的数据
    xiansuo = data1['data'][0]['count']
    jiaoche = data1['data'][3]['count']
    print(xiansuo)
    print(jiaoche)

    # 获取渠道漏斗_全渠道合计的意向和订单数据
    url = conf.BUICK_API_URL + "/api/dashboard/funnel/channel_funnel"
    json = {
        "date_select": "2019-10"
    }
    headers = {
        'Content-Type': "application/json;charset=UTF-8"
    }
    # 发送post请求,获取响应数据
    response = request_tool.post_request(
        url, json=json, headers=headers, cookies=test_login['cookie'])
    # 遍历获取响应数据inv_quantity的数值
    data = response.json()
    # 判断响应码
    assert_tool.assert_equal(response.status_code, 200)
    # 获取response的具体的数据
    xiansuo1 = data['data'][5]['new_leads']
    jiaoche1 = data['data'][5]['new_retail']
    print(xiansuo1)
    print(jiaoche1)

    # 调用函数,设置单元格背景颜色
    # D:\softwaredata\pycharm\buik-ai-autotest2\download\source_file\关键数据核对.xls
    style = excel_tool.set_cell_style_font_size(10)
    # 读取本地excel download/source_file/别克新逻辑明细数据(LISA使用)20180608.xls
    # download/source_file/销售漏斗-gl6.xls
    orig = xlrd.open_workbook(
        r'{0}download/source_file/销售漏斗-gl6.xls'.format(os_tool.get_root_path()),
        formatting_info=True)  # formatting_info还没有对新版本的xlsx的格式完成兼容。
    # cpoy函数用于复制该变量的值,也就是复制一份新的excel数据给wb变量
    wb = copy(orig)
    # 根据索引获取第一页的sheet数据 赋值给s变量
    s = wb.get_sheet(0)
    f = 0
    if xiansuo != xiansuo1+1:
        f = 1
        s.write(0, 10, '展厅月度整体情况_线索:' + str(xiansuo) + '渠道漏斗_线索合计:' + str(xiansuo1), style)

    if jiaoche != jiaoche1+1:
        f = 1
        s.write(1, 10, '展厅月度整体情况_交车:' + str(jiaoche) + '渠道漏斗_交车合计:' + str(jiaoche1), style)

    # 如果f变量= 1的时候执行里面的代码
    if (f == 1):
        # f = 1 将处理之后的excel数据存入指定的本地路径下
        time = excel_tool.data_time()
        wb.save(
            os_tool.get_root_path() +
            'download/target_file/failed_别克新逻辑明细数据(LISA使用)20180608_%s.xls'%(time))
        print("failed")
    # 反之执行里面的代码
    else:
        print("pass")
