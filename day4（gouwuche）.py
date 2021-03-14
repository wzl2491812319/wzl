print("----欢迎来到我们电子世界商城系统----")
username = "wzl"
password = "123"
i = 1
while i < 4:
    print("这是您的第",i,"次登录")
    username =input("请输入用户名：")
    password = input("请输入密码：")
    if username == "wzl" and password == "123":
        print("登录成功,欢迎您的到来！")
        break
    else:
        if i == 3:
            print("对不起，您的用户名和密码输入错误，无法登陆")
            import sys
            sys.exit()
        else:
            i += 1
        if i < 3:
            print("您的用户名或密码输入错误，请重新输入！")
shop = [
    ["HUAWEI",5000],
    ["Iphone",8000],
    ["xiaomi",3000],
    ["oppo",4000],
    ["vivo",2500],
]
salary = int(input("请输入您的初始资金:"))
mycat = []
while 1:
    for index,value in enumerate(shop):
        print(index,value)
    num = input("请输入您要的商品ID：")
    if num.isdigit():
        num = int(num)
        if num in range(len(shop)):
            if salary >= shop[num][1]:
                mycat.append(shop[num])
                salary = salary - shop[num][1]
                print("\033[32;20;1m购买成功！您的余额为：",salary,"元 \033[0m")
            else:
                print("\033[31;20;1m对不起，您的资金不足！\033[0m")
        else:
            print("没有该商品，抱歉！")
    elif num == "Q" or num == "q":
        print("欢迎下次光临！再见")
        break
    else:
        print("输入非法，请重新输入！")
print("你的购物车内容为：")
for index,value in enumerate(mycat):
    print(index,":",value)
print("-----您的余额：------",salary,"元")


#     姓名  年龄  性别  编号 任职公司  薪资  部门编号
# names = [
#     ["曹操","56","男","106","IBM",500 ,"50"],
#     ["大乔","19","女","230","微软",501 ,"60"],
#     ["小乔", "19", "女", "210", "Oracle",600, "60"],
#     ["许褚", "45", "男", "230", "Tencent",700 , "10"]
# ]
# avg = 0
# sum = 0
# avg2 = 0
# sum2 = 0
# #1.统计每个人的平均薪资
# for i in range(len(names)):
#     a = names[i][5]
#     b = int(names[i][1])
#     sum = a + sum
#     sum2 = b + sum2
# avg = sum / len(names)
# avg2 = sum2 / len(names)
# print("平均薪资为：",avg)
# print("平均年龄：",avg2)
#
# #公司新来一个员工，刘备，45，男，220，alibaba，500,30，添加到列表中
# print("原表",names)
# names.insert(4,["刘备","45","男","220","alibaba",500,"30"])
# print("新表",names)
#
# #统计公司男女人数
# nan = 0
# nv = 0
# for i in range(len(names)):
#     if names[i][2] == "男":
#         nan += 1
#     else:
#         nv += 1
# print("男生人数：",nan)
# print("女生人数：",nv)
#
# #每个部门的人数
# for i in range(len(names)):
#     print(names[i][6],names.count(i))


# 现在魔法学院有赫敏、哈利、罗恩、马尔福四个人的几次魔法作业的成绩。但是呢，因为有些魔法作业有一定难度，教授不强制同学们必须上交，所以大家上交作业的次数并不一致。
# [罗恩, 23 ,35 ,44]
# [哈利 ,60, 77 ,68 ,88, 90]
# [赫敏, 97 ,99 ,89 ,91, 95, 90]
# [马尔福 ,100, 85 ,90]
# 求每个人的总成绩？

# a = ["罗恩",23,35,44]
# b = ["哈利",60,77,68,88,90]
# c = ["赫敏",97,99,89,91,95,90]
# d = ["马尔福",100,85,90]
# suma =int(a[1]+a[2]+a[3])
# print(a[0],"总成绩为：",suma)

# a = [ ["罗恩", 23, 35, 44],
#       ["哈利", 60, 77, 68, 88, 90],
#       ["赫敏", 97, 99, 89, 91, 95, 90],
#       ["马尔福", 100, 85, 90]]
# for x in range(len(a)):
#     num = 0
#     for y in range(1, len(a[x])):
#         num += a[x][y]
#     print(a[x][0], "的成绩为", num)


# num = int(input("数字:"))  #54321
# while num != 0:
#     print(num % 10)  #1 2 3 4 5
#     num = num // 10

# def bubbleSort(a):
#     n = len(a)
#     # 遍历所有数组元素
#     for i in range(n):
#         # Last i elements are already in place
#         for j in range(0, n - i - 1):
#             if a[j] > a[j + 1]:
#                 a[j], a[j + 1] = a[j + 1], a[j]
# a = [5,2,4,7,9,1,3,5,4,0,6,1,3]
# bubbleSort(a)
# print("排序后的数组:")
# for i in range(len(a)):
#     print("%d" % a[i])