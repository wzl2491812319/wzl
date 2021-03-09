#第一套衣服数据
id1 = 1
name1 = "牛仔裤"
price1 = 40
quality1 = "A+"
style1 = "裤子"
xiaoliang1 = 30

#第二套衣服数据
id2 = 2
name2 = "衬衫"
price2 = 50
quality2 = "A-"
style2 = "上衣"
xiaoliang2 = 10

#第三套衣服数据
id3 = 3
name3 = "风衣"
price3 = 20
quality3 = "B-"
style3 = "上衣"
xiaoliang3 = 15

#第四套衣服数据
id4 = 4
name4 = "卫衣"
price4 = 80
quality4 = "A+"
style4 = "上衣"
xiaoliang4 = 5

#第五套衣服数据
id5 = 5
name5 = "破洞裤"
price5 = 100
quality5 = "C-"
style5 = "上衣"
xiaoliang5 = 1

print("-----------------------------------")
print("------欢迎来到jason衣服商城系统-------")
print("-----------------------------------")
print("编号"," ","衣服名称"," ","价格"," ","品质"," ","类型"," ","销量")
print(id1,"   ",name1,"   ",price1,"   ",quality1,"  ",style1," ",xiaoliang1)
print(id2,"   ",name2,"     ",price2,"   ",quality2,"  ",style2," ",xiaoliang2)
print(id3,"   ",name3,"     ",price3,"   ",quality3,"  ",style3," ",xiaoliang3)
print(id4,"   ",name4,"     ",price4,"   ",quality4,"  ",style4," ",xiaoliang4)
print(id5,"   ",name5,"   ",price5,"  ",quality5,"  ",style5," ",xiaoliang5)
print("总金额：",(price1 * xiaoliang1 + price2 * xiaoliang2 + price3 * xiaoliang3 + price4 * xiaoliang4 + price5 * xiaoliang5),"元")
print("平均上衣价格：",(price2 + price3 + price4) / 3)
print("平均裤子价格：",(price1 + price5) / 2)
