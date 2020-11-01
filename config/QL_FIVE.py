import os, datetime
xml_path='C:/softwoer/dev/test_api/reports/xml'
html_path='C:/softwoer/dev/test_api/reports/html/data/test-cases'

dirToBeEmptied = 'C:/softwoer/dev/test_api/reports/xml' #需要清空的文件夹
ds = list(os.walk(dirToBeEmptied)) #获得所有文件夹的信息列表
delta = datetime.timedelta(days=7) #设定365天前的文件为过期
now = datetime.datetime.now() #获取当前时间
for d in ds: #遍历该列表
 os.chdir(d[0]) #进入本级路径，防止找不到文件而报错
 if d[2] != []: #如果该路径下有文件
  for x in d[2]: #遍历这些文件
   ctime = datetime.datetime.fromtimestamp(os.path.getctime(x)) #获取文件创建时间
   if ctime < (now-delta): #若创建于delta天前
    os.remove(x) #则删掉

dirToBeEmptied_html =html_path
ds = list(os.walk(dirToBeEmptied_html)) #获得所有文件夹的信息列表
dsr = ds[::-1] #反转该列表，从最底层的文件夹开始清算
for d in dsr: #遍历该列表
 print(d) #打印出列表项，观察规律
 if d[2] != []: #如果该路径下有文件
  for x in d[2]: #先将文件清理干净
   os.remove(os.path.join(d[0], x))
for d in dsr: #再次遍历该列表
 if d[1] != []: #如果该路径下有子文件夹
  for y in d[1]: #将子文件夹清理干净
   os.rmdir(os.path.join(d[0], y))
