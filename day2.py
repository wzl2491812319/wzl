
# import random
# num = random.randint(1,500)
# print(num)


# a = input("请输入数字：")
# print(type(a))
# a = int(a)
# print(type(a))
# print("您输入的数字为：",a)


# score = input("请输入您的成绩：")
# score = int(score)
# if score >= 90 and score <= 100:
#     print("优秀")
# elif score >= 80 and score < 90:
#     print("良好")
# elif score >= 70 and score < 80:
#     print("还可以")
# elif score >= 60 and score < 70:
#     print("及格")
# elif score >0 and score < 60:
#     print("不合格")
# else:
#     print("非法输入！")


# number = 1
# while  True:
#     if number > 5:
#         break
#     print(number)
#     number = number + 1


# day2任务开始

#实现输入10个数字，并打印10个数的求和结果
#方法一
# a = input("请输入多个数字，会进行相加操作:")
# a = a.replace("","")
# lst = a.split("+")
# num = 0
# for lst1 in lst:
#     num = num + int(lst1)
# print(num)

# 方法二
# a = input("请输入多个数字，用，隔开:")
# b = [int(i) for i in a.split(",")]
# print(sum(b))

#从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。

# a = input("请输入多个数字：")
# temp = []
# for i in a.split(","):
#     temp.append(int(i))
# temp = sorted(temp)
# print("您输入的数组中，最大的数为：%g" %temp[-1])

#使用random模块，如何产生 50~150之间的数？

# import random
# num = random.randint(50,150)
# print(num)

#从键盘输入任意三边，判断是否能形成三角形，若可以，
#则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）

# a = int(input('请输入第 1 边:'))
# b = int(input('请输入第 2 边:'))
# c = int(input('请输入第 3 边:'))
# if a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a:
#     print('能组成三角形')
#     if a==b==c:
#         print('等边三角形')
#     elif a==b or a==c or b==c:
#         print('等腰三角形')
#     elif (a**2+b**2==c**2) or (b**2+c**2==a**2) or (a**2+c**2==b**2):
#         print('直角三角形')
#     else:
#         print('普通三角形')
# else:
#         print('不能组成三角形')

#有以下两个数，使用+，-号实现两个数的调换。

# a = 56
# b = 71
# print("改变前a为:",a,"改变前b为:",b)
# c = a + b
# a = c - a
# b = c - b
# print("改变后a为:",a,"改变后b为:",b)

#实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）

# user = "root"
# password = "admin"
# cs = 0
# while cs < 3:
#     a = input("请输入用户名：")
#     b = input("请输入密码：")
#     if a == "root" and b == "admin":
#         print("登录成功")
#         break
#     else:
#         if cs == 2:
#             print("您已输入错误三次，锁定中！")
#         else:
#             print("输入用户名和密码错误，请重新输入")
#         cs += 1

#编程实现下列图形的打印

# for i in range(8):
#     for j in range(0, 10 - i):
#         print(end=" ")
#     for k in range(10 - i, 10):
#         print("*", end=" ")
#     print()

#使用while循环实现99乘法表的打印。

#方法一：
# i = 1
# while i <= 9:
#     j = 1
#     while(j <= i):    # j的大小是由i来控制的
#         print('%d*%d=%-3d' % (i, j, i*j), end='\t')
#         j += 1
#     print('')
#     i += 1

#方法二：
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('{}x{}={}\t'.format(j, i, i*j), end='')
#     print()

#编程实现99乘法表的倒叙打印
# for i in range(9,0,-1):
#     for j in range(1, i+1):
#         print('{}x{}={}\t'.format(j, i, i*j), end='')
#     print()

#一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，
# 问第几天能出来？请编程求出。

# a = 20
# b = 3
# c = 2
# day = 0
# while 1:
#     a -= b
#     if a == 0:
#         break
#     a += c
#     day += 1
# print(day)

#判断下列变量命名是否合法

#help("keywords")
# char=1      合法     Cy%ty=2      不合法
# Oax_li=3    合法     $123=4       不合法
# fLul=5      合法      3_3=6       不合法
# BYTE=7      合法      T_T=8       合法

# 继续完成上午的猜数字游戏的需求功能。
# 1.添加计数打印功能
# 2.添加次数金币功能和锁定系统功能。

#（有错误）
# import random,time
# cont = 0
# qian = 0
# rannum = random.randint(1,100)
# print("您的资产为：",qian)
#while True:
    # print("这是您的第%s次尝试" %(cont+1))
    # if(cont ==50):
    #     print("系统锁定")
    #     break
    # if(cont == 20):
    #     time.sleep(1)
    #     print("您还需要等待29秒")
    #     time.sleep(1)
    #     print("您还需要等待28秒")
    #     time.sleep(1)
    #     print("您还需要等待27秒")
    #     time.sleep(1)
    #     print("您还需要等待26秒")
    #     time.sleep(1)
    #     print("您还需要等待25秒")
    #     time.sleep(1)
    #     print("您还需要等待24秒")
    #     time.sleep(1)
    #     print("您还需要等待23秒")
    #     time.sleep(1)
    #     print("您还需要等待22秒")
    #     time.sleep(1)
    #     print("您还需要等待21秒")
    #     time.sleep(1)
    #     print("您还需要等待20秒")
    #     time.sleep(1)
    #     print("您还需要等待19秒")
    #     time.sleep(1)
    #     print("您还需要等待18秒")
    #     time.sleep(1)
    #     print("您还需要等待17秒")
    #     time.sleep(1)
    #     print("您还需要等待16秒")
    #     time.sleep(1)
    #     print("您还需要等待15秒")
    #     time.sleep(1)
    #     print("您还需要等待14秒")
    #     time.sleep(1)
    #     print("您还需要等待13秒")
    #     time.sleep(1)
    #     print("您还需要等待12秒")
    #     time.sleep(1)
    #     print("您还需要等待11秒")
    #     time.sleep(1)
    #     print("您还需要等待10秒")
    #     time.sleep(1)
    #     print("您还需要等待9秒")
    #     time.sleep(1)
    #     print("您还需要等待8秒")
    #     time.sleep(1)
    #     print("您还需要等待7秒")
    #     time.sleep(1)
    #     print("您还需要等待6秒")
    #     time.sleep(1)
    #     print("您还需要等待5秒")
    #     time.sleep(1)
    #     print("您还需要等待4秒")
    #     time.sleep(1)
    #     print("您还需要等待3秒")
    #     time.sleep(1)
    #     print("您还需要等待2秒")
    #     time.sleep(1)
    #     print("您还需要等待1秒")
    #     time.sleep(1)
    #     print("您还需要等待0秒")
    #     break
    # else:
    #     x = input("你输入的数字是")
    #     cont += 1
    #     num = int(x)
    #     if num > rannum:
    #         print("大了！")
    #     elif num < rannum:
    #         print("小了！")
    #     elif num == rannum:
    #         print("您的资产为：",qian+2000)
    #         print("恭喜，猜对了！数字为：", rannum)
    #         break



#用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
# a=1
# b=1
# c=0
# while a<20:
#     while b<=a:
#         print(a," ",b)
#         c=c+(a*b)
#         b+=1
#     b=1
#     a+=1
# print(c)


# 继续完成上午的猜数字游戏的需求功能。
# 1.添加计数打印功能
# 2.添加次数金币功能和锁定系统功能。

# import random
# import time
# num = random.randint(0, 10)
# gold=0
# n=0
# asd=20
# print("您的初始资金为0")
# while 1:
#     n+=1
#     a = int(input("请输入一个数字："))
#     if num > a:
#         print("小了")
#     elif num < a:
#         print("大了")
#     elif num==a:
#         print("你成功了")
#         print("你猜了",n,"次")
#         if n<3:
#             gold+=200
#             print("游戏结束，您的资金为",gold)
#         else:
#             print("资金不加不减")
#         break
#     if n==20:
#         print("您已经猜了20次了即将冷却30秒")
#         while 1:
#             time.sleep(1)
#             print("还有",asd,"秒")
#             asd-=1
#             if asd==0:
#                 break
#     elif n==50:
#         print("您已经猜了50次了系统锁定")
#         while 1:
#             time.sleep(1)