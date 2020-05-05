# -*- coding:utf-8 -*-
# Author : 小吴老师
# Data ：2019/7/9 21:34

import random
import re
import string
from datetime import datetime

import pinyin
from dateutil.relativedelta import relativedelta

import tools.data.identity_constant as const


# 1. 定义“获取性别”函数，函数名：get_sex()
# 2. 随机0和1,0代表男，1代表女
# 3. 打印日志
#       性别：0-男
#       性别：1-女
# 4. 返回性别（数字）
def random_sex():
    sex = random.randint(0,1)
    # if sex == 0:
    #     print('性别：0-男')
    # else:
    #     print('性别：1-女')
    return sex

# 1. 定义函数，函数名：get_name()
# 2. 需要支持指定性别，参数名sex
# 3. 提供3个字符串：百家姓、适合男性的字、适合女性的字
# 4. 姓名由3个字组成：姓+名1+名2
#       姓：从百家姓字符串随机1个
#       名1：若为男生，从boys中选1个字
#           若为女生，从girls里选1个字
#       名2：先随机0或1,0不需要第3个字，1需要第3个字
#           若需要第3个字，男生从boys中选1个，女生从girls中选1个
# 5. 返回名字（第1个字+第2个字+第3个字）
def random_name(sex=-1):
    if sex == -1:
        sex = random.randint(0,1)

    first_name = "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华" \
                 "金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞" \
                 "任袁柳酆鲍史唐费廉岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅皮卞齐" \
                 "康伍余元卜顾孟平黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计伏成戴谈" \
                 "宋茅庞熊纪舒屈项祝董梁杜阮蓝闵席季麻强贾路娄危江童颜郭梅盛林" \
                 "刁钟徐邱骆高夏蔡田樊胡凌霍虞万支柯咎管卢莫经房裘缪干解应宗宣丁" \
                 "贲邓郁单杭洪包诸左石崔吉钮龚程嵇邢滑裴陆荣翁荀羊於惠甄魏加封芮" \
                 "羿储靳汲邴糜松井段富巫乌焦巴弓牧隗山谷车侯宓蓬全郗班仰秋仲伊宫宁" \
                 "仇栾暴甘钭厉戎祖武符刘姜詹束龙叶幸司韶郜黎蓟薄印宿白怀蒲台从鄂索" \
                 "咸籍赖卓蔺屠蒙池乔阴郁胥能苍双闻莘党翟谭贡劳逄姬申扶堵冉宰郦雍" \
                 "却璩桑桂濮牛寿通边扈燕冀郏浦尚农温别庄晏柴瞿阎充慕连茹习宦艾鱼" \
                 "容向古易慎戈廖庚终暨居衡步都耿满弘匡国文寇广禄阙东殴殳沃利蔚" \
                 "越夔隆师巩厍聂晁勾敖融冷訾辛阚那简饶空曾毋沙乜养鞠须丰巢关蒯相" \
                 "查后江红游竺权逯盖益桓公万俟司马上官欧阳夏侯诸葛闻人东方赫连皇" \
                 "甫尉迟公羊澹台公冶宗政濮阳淳于仲孙太叔申屠公孙乐正轩辕令狐钟离" \
                 "闾丘长孙慕容鲜于宇文司徒司空亓官司寇仉督子车颛孙端木巫马公西漆" \
                 "雕乐正壤驷公良拓拔夹谷宰父谷粱晋楚阎法汝鄢涂钦段干百里东郭南门" \
                 "呼延归海羊舌微生岳帅缑亢况后有琴梁丘左丘东门西门商牟佘佴伯赏南" \
                 "宫墨哈谯笪年爱阳佟第五言福百家姓续"
    girl = "秀娟英华慧巧美娜静淑惠珠翠雅芝玉萍红娥玲芬芳燕彩春菊兰凤洁梅琳素云莲" \
           "真环雪荣爱妹霞香月莺媛艳瑞凡佳嘉琼勤珍贞莉桂娣叶璧璐娅琦晶妍茜秋珊莎" \
           "锦黛青倩婷姣婉娴瑾颖露瑶怡婵雁蓓纨仪荷丹蓉眉君琴蕊薇菁梦岚苑婕馨瑗琰" \
           "韵融园艺咏卿聪澜纯毓悦昭冰爽琬茗羽希宁欣飘育滢馥筠柔竹霭凝晓欢霄枫芸" \
           "菲寒伊亚宜可姬舒影荔枝思丽";
    boy = "伟刚勇毅俊峰强军平保东文辉力明永健世广志义兴良海山仁波宁贵福生龙元全国" \
          "胜学祥才发武新利清飞彬富顺信子杰涛昌成康星光天达安岩中茂进林有坚和彪博" \
          "诚先敬震振壮会思群豪心邦承乐绍功松善厚庆磊民友裕河哲江超浩亮政谦亨奇固" \
          "之轮翰朗伯宏言若鸣朋斌梁栋维启克伦翔旭鹏泽晨辰士以建家致树炎德行时泰盛" \
          "雄琛钧冠策腾楠榕风航弘";

    first = random.choice(first_name)
    names = boy if sex == 0 else girl
    second = random.choice(names)
    has_third = random.randint(0,1)
    third = random.choice(names) if has_third == 1 else ''
    full_name = first+second+third
    # print('姓名：'+full_name)
    return full_name

# 1. 定义函数，函数名：get_pwd()
# 2. 密码长度8位，由大写字母、小写字母和数字组成
# 3. 至少包含1个大写字母、1个小写字母，1个数字
# 4. 其余5个字母随便取
# 5. 返回密码
def random_pwd():
    src = string.ascii_letters+string.digits
    pwd_list = random.sample(src,5)
    pwd_list.extend(random.sample(string.digits,1))
    pwd_list.extend(random.sample(string.ascii_uppercase,1))
    pwd_list.extend(random.sample(string.ascii_lowercase,1))
    random.shuffle(pwd_list)
    pwd = ''.join(pwd_list)
    # print('密码：'+pwd)
    return pwd


'''
# 1. 定义函数，函数名：get_tell()
# 2. 前三位为号段，如186/135，从有效号段列表取
# 3. 至少包含1个大写字母、1个小写字母，1个数字
# 4. 其余5个字母随便取
# 5. 返回密码
'''
def random_tell():
    tel_first = ['139', '138', '137', '136', '135', '134',
                 '159', '158', '157', '150', '151', '152', '147',
                 '188', '187','182', '183', '184', '178', '130', '131',
                 '132', '156', '155', '186', '185', '145', '176',
                 '133', '153', '189', '180', '181', '177', '173']
    first = random.choice(tel_first)
    second = str(random.randint(0, 9999) + 10000)[1:]
    third = str(random.randint(0, 9999) + 10000)[1:]

    tell_num = first + second + third
    # print('电话:'+tell_num)
    return tell_num


'''
# 1. 定义函数，函数名：get_addr()
# 2. 地址组成：省份+地区+路名+门牌号+房间号（楼层+号数）
#              eg：地址：上海市金山区河南广场33号1202室
# 3. 门牌号取值范围：11-150号
# 4. 房间号：
#       楼层高度范围：1-20层，不需前补0
#       房间号范围：1-20室，两位前补0（比如3，则改成03）
#       示例：12层第3个房间，房间号：1203室
# 5. 返回地址
'''
def random_addr():
    province ='上海市'
    districts = ['黄浦区','徐汇区','长宁区','静安区','普陀区','虹口区',
                 '闸北区','杨浦区','闵行区','宝山区','青浦区','松江区','嘉定区','奉贤区','金山区','浦东新区']
    road_list = '重庆大厦','黑龙江路','十梅庵街','遵义路','湘潭街',\
                '瑞金广场','仙山街','仙山东路','仙山西大厦','白沙河路',\
                '赵红广场','机场路','民航街','长城南路','流亭立交桥',\
                '虹桥广场','长城大厦','礼阳路','风岗街','中川路','白塔广场',\
                '兴阳路','文阳街','绣城路','河城大厦','锦城广场','崇阳街',\
                '华城路','康城街','正阳路','和阳广场','中城路','江城大厦',\
                '顺城路','安城街','山城广场','春城街','国城路','泰城街',\
                '德阳路','明阳大厦','春阳路','艳阳街','秋阳路','硕阳街',\
                '青威高速','瑞阳街','丰海路','双元大厦','惜福镇街道',\
                '夏庄街道','古庙工业园','中山街','太平路','广西街',\
                '潍县广场','博山大厦','湖南路','济宁街','芝罘路',\
                '易州广场','荷泽四路','荷泽二街','荷泽一路','荷泽三大厦',\
                '观海二广场','广西支街','观海一路','济宁支街','莒县路',\
                '平度广场','明水路','蒙阴大厦','青岛路','湖北街',\
                '江宁广场','郯城街','天津路','保定街','安徽路',\
                '河北大厦','黄岛路','北京街','莘县路','济南街',\
                '宁阳广场','日照街','德县路','新泰大厦','荷泽路',\
                '山西广场','沂水路','肥城街','兰山路','四方街','平原广场',\
                '泗水大厦','浙江路','曲阜街','寿康路','河南广场','泰安路',\
                '大沽街','红山峡支路','西陵峡一大厦','台西纬一广场',\
                '台西纬四街','台西纬二路','西陵峡二街','西陵峡三路',\
                '台西纬三广场','台西纬五路','明月峡大厦','青铜峡路',\
                '台西二街','观音峡广场','瞿塘峡街','团岛二路','团岛一街',\
                '台西三路','台西一大厦','郓城南路','团岛三街','刘家峡路',\
                '西藏二街','西藏一广场','台西四街','三门峡路','城武支大厦',\
                '红山峡路','郓城北广场','龙羊峡路','西陵峡街','台西五路',\
                '团岛四街','石村广场','巫峡大厦','四川路','寿张街',\
                '嘉祥路','南村广场','范县路','西康街','云南路','巨野大厦',\
                '西江广场','鱼台街','单县路','定陶街','滕县路','钜野广场',\
                '观城路','汶上大厦','朝城路','滋阳街','邹县广场','濮县街',\
                '磁山路','汶水街','西藏路','城武大厦','团岛路','南阳街',\
                '广州路','东平街','枣庄广场','贵州街','费县路','南海大厦',\
                '登州路','文登广场','信号山支路','延安一街','信号山路',\
                '兴安支街','福山支广场','红岛支大厦','莱芜二路','吴县一街',\
                '金口三路','金口一广场','伏龙山路','鱼山支街','观象二路',\
                '吴县二大厦','莱芜一广场','金口二街','海阳路','龙口街',\
                '恒山路','鱼山广场','掖县路','福山大厦','红岛路','常州街',\
                '大学广场','龙华街','齐河路','莱阳街','黄县路','张店大厦',\
                '祚山路','苏州街','华山路','伏龙街','江苏广场','龙江街',\
                '王村路','琴屿大厦','齐东路','京山广场','龙山路','牟平街',\
                '延安三路','延吉街','南京广场','东海东大厦','银川西路',\
                '海口街','山东路','绍兴广场','芝泉路','东海中街','宁夏路',\
                '香港西大厦','隆德广场','扬州街','郧阳路','太平角一街',\
                '宁国二支路','太平角二广场','天台东一路','太平角三大厦',\
                '漳州路一路','漳州街二街','宁国一支广场','太平角六街',\
                '太平角四路','天台东二街','太平角五路','宁国三大厦',\
                '澳门三路','江西支街','澳门二路','宁国四街','大尧一广场',\
                '咸阳支街','洪泽湖路','吴兴二大厦','澄海三路','天台一广场',\
                '新湛二路','三明北街','新湛支路','湛山五街','泰州三广场',\
                '湛山四大厦','闽江三路','澳门四街','南海支路','吴兴三广场',\
                '三明南路','湛山二街','二轻新村镇','江南大厦','吴兴一广场',\
                '珠海二街','嘉峪关路','高邮湖街','湛山三路','澳门六广场',\
                '泰州二路','东海一大厦','天台二路','微山湖街','洞庭湖广场',\
                '珠海支街','福州南路','澄海二街','泰州四路','香港中大厦',\
                '澳门五路','新湛三街','澳门一路','正阳关街','宁武关广场',\
                '闽江四街','新湛一路','宁国一大厦','王家麦岛','澳门七广场',\
                '泰州一路','泰州六街','大尧二路','青大一街','闽江二广场',\
                '闽江一大厦','屏东支路','湛山一街','东海西路',\
                '徐家麦岛函谷关广场','大尧三路','晓望支街','秀湛二路',\
                '逍遥三大厦','澳门九广场','泰州五街','澄海一路','澳门八街',\
                '福州北路','珠海一广场','宁国二路','临淮关大厦','燕儿岛路',\
                '紫荆关街','武胜关广场','逍遥一街','秀湛四路','居庸关街',\
                '山海关路','鄱阳湖大厦','新湛路','漳州街','仙游路','花莲街'
    district = random.choice(districts)
    road = random.choice(road_list)
    no = str(random.randint(11,150))+'号'
    room = str(random.randint(1,20))+str(random.randint(100,120))[1:]+'室'
    addr = province+district+road+no+room
    # print('地址：'+addr)
    return addr

'''
# 1. 定义函数，函数名：get_email()
# 2. 邮箱组成：
#       首字符：只能是字母（大写或小写）
#       其余字符：大写字母、小写字母、数字、下划线
#       邮箱后缀：主流邮箱服务商，如@126.com、@gmail.com、@qq.com等
# 3. 邮箱名长度：6-18位
# 4. 返回邮箱
'''
def random_email():
    email_suffix = ['@gmail.com','@yahoo.com','@msn.com','@hotmail.com',
                    '@aol.com','@ask.com','@live.com','@qq.com',
                    '@0355.net','@163.com','@163.net','@263.net',
                    '@3721.net','@yeah.net','@googlemail.com','@126.com',
                    '@sina.com','@sohu.com','@yahoo.com.cn']
    first = random.choice(string.ascii_letters)
    num = string.ascii_letters+string.digits+"_"
    length = random.randint(5,17)
    second = ''.join(map(str,random.sample(num,length)))
    third = random.choice(email_suffix)
    email = first+second+third
    # print('邮箱：'+email)
    return email

def random_name_pinyin(name=''):
    if name == '':
        name = random_name()
    if len(name) == 2:
        name_pinyin = pinyin.get(name, format='strip')
    else:
        name_pinyin = pinyin.get(name[0],format='strip')+pinyin.get_initial(name[1:],delimiter="")
    # print('姓名（拼音）：'+name_pinyin)
    return name_pinyin

def random_number(min=0,max=1,step=1):
    num = random.randrange(min,max,step)
    # print('随机数：'+str(num))
    return num

# 随机字母
def random_str_abc(num):
    str =''
    for i in range(num):
        str=str+random.choice(string.ascii_letters)
    return str


# 中文
def random_chinese():
    val = random.randint(0x4e00, 0x9fbf)
    return chr(val)

# 常用汉字
def random_gbk_chines():
    head = random.randint(0xb0, 0xf7)
    body = random.randint(0xa1, 0xf9)
    val = f'{head:x}{body:x}'
    str = bytes.fromhex(val).decode('gb2312')
    return str

def random_birthday(min=0,max=100):
    age=random.randint(min,max)
    print(str(age)+'岁')
    today=datetime.now()
    birth_days = datetime.strftime(today - relativedelta(years=age), "%Y%m%d")
    print(birth_days)
    return birth_days

def random_area():
    flag=False
    rlt={}
    while not flag:
        area = eval(str(random.choice(list(const.AREA_INFO.items()))))
        addr=area[1]
        if re.findall(r'(^[上北天重][海京津庆]市.{1,}[县|州|区])',addr)!=[]:
            rlt['province']=re.findall(r'(.+市)',addr)[0].replace('市市','市')
            rlt['city']=re.findall(r'(.+市)',addr)[0].replace('市市','市')
            rlt['county']=re.findall(r'市(.+[县|州|区])',addr)[0]
            flag=True
        if re.findall(r'(.+[省].+市.+[县|州|区])', addr) != []:
            rlt['province']=re.findall(r'(.+省)',addr)[0]
            rlt['city']=re.findall(r'省(.+市)',addr)[0].replace('市市','市')
            rlt['county']=re.findall(r'市(.+[县|州|区])',area[1])[0]
            flag = True
        if re.findall(r'(.+自治区.+市.+[县|州|区])', addr) != []:
            rlt['province']=re.findall(r'(.+自治区)',addr)[0]
            rlt['city']=re.findall(r'自治区(.+市)',addr)[0].replace('市市','市')
            rlt['county']=re.findall(r'市(.+[县|州|区])',addr)[0]
            flag = True
        rlt['code'] = str(area[0])
        rlt['name'] = area[1]

    return rlt

