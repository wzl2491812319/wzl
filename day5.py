# def sum(a,b,c):
#     s = a + b +c
#     return  s
# a = 3
# b = 4
# c = 5
# z = sum(a,b,c)
# print(z)
#
# def NXN(m):
#     for i in range(1,m+1):
#         for j in range(1,i+1):
#             print(j,"X",i,"=",(j*i),"\t",end="")
#         print()
# n = input("请输入一个数字：")
# n = int(n)
# NXN(n)

# prov = {
#     "010":"北京",
#     "020":"上海"
# }
# print(type(prov))
# print(prov)
# #插入数据
# prov["030"] = "广州"
# prov["040"] = "深圳"
# print(prov)
# #取出数据
# value = prov["010"]
# print(value)
# #如何去遍历数据
# #1、获取所有键
# keys = prov.keys()
# #遍历每一个键，通过键来获取字典每个值
# for key in keys:
#     value = prov[key]
#     print(key,value)


#1、请循环遍历出所有的key
#2、请循环遍历出所有的value
# 3、请在字典中增加一个键值对,"k4":"v4"

# dict = {
#     "k1":"v1",
#     "k2":"v2",
#     "k3":"v3"
# }
# keys = dict.keys()
# for key in keys:
#     print("所有的key为：",key)
# for key in keys:
#     value = dict[key]
#     print("所有的value为：", value)
# dict["K4"] = "v4"
# print(dict)


#请将上面的数据存储到字典里，可以根据水果名称查询购买这个水果的费用
#用水果名称做key，金额做value，创建一个字典

# info = {
#     "苹果":32.8,
#     "香蕉":22,
#     "葡萄":15.5
# }
#
# while 1:
#     a = input("请输入你要购买的水果名称：")
#     if a == "q":
#         break
#     b = info[a]
#     print(b)

#小明，小刚去超市里购买水果
#小明购买了苹果，草莓，香蕉，小刚购买了葡萄，橘子，樱桃，请从下面的描述的字典中，计算每个人花费的金额，并写入到money字段里。
#以姓名做key，value仍然是字典

# Friuts = {
# 	"苹果":12.3,  # 水果和单价
# 	"草莓":4.5,
#     "香蕉":6.3,
#     "葡萄":5.8,
#     "橘子":6.4,
#     "樱桃":15.8
# }
# info = {
#     "小明": {
#         "fruits": {"苹果":4, "草莓":13, "香蕉":10},
#         "money":0
#     },
#     "小刚": {
#         "fruits": {"葡萄":19, "橘子":12, "樱桃":30},
#         "money":0
#     }
# }
# for a in info:
#     w = 0
#     for i in info[a]["fruits"]:
#         for y in info[a]["fruits"].keys() :
#             if i == y :
#                 if y in Friuts:
#                     x = (Friuts[y])*(info[a]["fruits"][i])
#                     w += x
#                     info[a]["money"] = w
#             else:
#                 continue
#     print(a,"的金钱为",info[a]["money"])

#编写一个函数，传入一个列表，并统计每个数字出现的次数。返回字典数据：{21:3,56:9,10:3}

# def abc(li):
#     a= {}
#     for i in range(len(li)-1):
#         flag = 0
#         for j in range(i):
#             if li[j] == li[i]:
#                 flag = 1
#                 break
#         if flag == 1:
#             continue
#         if li[i].isdigit():
#             counter = li.count(li[i])
#             a[li[i]] = counter
#         else:
#             continue
#     return a
# x = input("请输入一个列表：")
# a = x.split(",")
# print(abc(a))

#有以下公司员工信息，将数据转换为字典方式（姓名作为键，其他作为值,张三:{xxx:xxx,xx:xxx}）

## 姓名  年龄  性别  编号   任职公司   薪资   部门编号
# names = [
#     ["刘备","56","男","106","IBM", 500 ,"50"],
#     ["大乔","19","女","230","微软", 501 ,"60"],
#     ["小乔", "19", "女", "210", "Oracle", 600, "60"],
#     ["张飞", "45", "男", "230", "Tencent", 700 , "10"]
# ]
# name = []
# for i in range(len(names)):
#     a = names[i][0]
#     b = name.append(a)
# print(name)
# d = dict(zip(name,names))
# print(d)





