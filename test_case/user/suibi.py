import xlrd
from xlutils.copy import copy
import xlwt

# 第一步  把原表格中的数据拷贝一份
path = 'E:\\测试文件\\test.xls'
book = xlrd.open_workbook(path)
#  book = xlrd.open_workbook(path, formatting_info=True)
#  设置 formatting_info=True ，当打开表格是保存表格原有的样式，进行保存时，
#  原来的样式不会丢失
sheet = book.sheets()[0]
wb = copy(book)
ws = wb.get_sheet(0)

# 第二步  设置样式
pattern = xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
pattern.pattern_fore_colour = 2 		 # 5 背景颜色为黄色
#1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7 = Cyan, 16 = Maroon,
# 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown), 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray

style = xlwt.XFStyle()
style.pattern = pattern

# 第三步  写入数据并保存
ws.write(1, 1, '苹果', style)	 #  顺序为 row, column, value, style
ws.write(1, 2, '南瓜', style)
ws.write(1, 3, '猫头鹰', style)
     # 单元格数据为空，背景为黄色
# value会覆盖原单元格的数据，如果不想被覆盖了，需提前把原单元格的数据获取到再写入
wb.save(path)

