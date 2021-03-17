# 确定用户库
bank = {}
# 确定银行的开户名称
bank_name = "中国工商银行昌平区回龙观支行"

info ="""
********************************
*    中国工商银行账户管理系统       *
*             V1.0             *
********************************
*       1.开户                  *
*       2.存钱                  *
*       3.取钱                  *
*       4.转账                  *
*       5.查询                  *
*       6.Bye!                 *
********************************
"""
import random
#存款逻辑
def savemoney():
    while 1:
        if chose == "2":
            account = input("请输入账号:")
            if account == "q":
                break
            elif account in bank.keys():
                password = input("请输入密码:")
                if account == "q":
                    break
                elif password == bank[account]["password"]:
                    print("欢迎使用",account)
                    print("账户余额为：",bank[account]["money"])
                    savenum = int(input("请输入存款金额"))
                    bank[account]["money"] = savenum+bank[account]["money"]
                    print("存款后余额为：",bank[account]["money"])
                else:
                    print("密码错误请重试")
            else:
                print("账号错误请重试")
#银行的取款逻辑
def bank_take(take_account, take_user, take_password, take_money):
    keys = bank.keys()
    if take_account not in keys:
        return 1
    elif take_password != bank[take_account]["password"] and take_user != bank[take_account]["username"]:
        return 2
    elif take_money > bank[take_account]["money"]:
        return 3
#取款逻辑
def take():
    take_account = input("请输入账号：")
    take_user = input("请输入用户名：")
    take_password = int(input("请输入密码："))
    take_money = int(input("请输入取款金额："))

    s = bank_take(take_account, take_user, take_password, take_money)

    if s == 1:
        print("账户不存在")
    elif s == 2:
        print("用户名密码输入错误：")
    elif s == 3:
        print("您的余额不足")
    else:
        bank[take_account]["money"] = bank[take_account]["money"] - take_money
        print("您的余额为：",bank[take_account]["money"])
#银行转账逻辑
def bank_zhuanzhang(outuser,outpasswd,enteruser,outmoney):
    if outuser in bank.keys():
        if outpasswd in bank[outuser]["password"]:
            if enteruser in bank.keys():
                outmoney = int(outmoney)
                if outmoney <= bank[outuser]["money"]:
                    bank[enteruser]["money"] = bank[enteruser]["money"] + outmoney
                    bank[outuser]["money"] = bank[outuser]["money"] - outmoney
                    print("转账成功，转入者资金为",bank[enteruser]["money"])
                    print("转账成功，转出者资金为", bank[outuser]["money"])
                    return 0
                else:
                    return 3
            else:
                return 1
        else:
            return 2
    else:
        print("不存在")
        return 1
#转账逻辑
def zhuanzhang():
    outuser = input("请输入转出账号：")  # 转出账号
    outpasswd = input("请输入转出密码：")  # 转出密码
    enteruser = input("请输入转入账号：")  # 转入账号
    outmoney = input("请输入转出金额：")  # 转出金额
    zz = bank_zhuanzhang(outuser,outpasswd,enteruser,outmoney)
    if zz == 0:
        print("正常")
    elif zz == 1:
        print("账号不对")
    elif zz == 2:
        print("密码不对")
    elif zz == 3:
        print("钱不够")
#查询逻辑
def bank_search():
    while True:
        accounts = input("请输入要查询的账户:")
        passwords = input("请输入密码：")
        if accounts in bank.keys():
            if passwords == bank[accounts]["password"]:
                print("当前账号:", accounts, "\n",
                      "密码：", "******", "\n",
                      "余额:", bank[accounts]["money"], "￥", "\n",
                      "用户居住地址为：", bank[accounts]["country"],
                      "-", bank[accounts]["province"], "-",
                      bank[accounts]["street"],
                      "-", bank[accounts]["door"], "\n",
                      "当前账户的开户行为：", bank_name)
            else:
                print("---账户或密码错误!---")
        else:
            print("---账户或密码错误!---")
        # if accounts and passwords == "q":
        #     print("退出查询")
        #     break
        aaa = input("退出查询请输入 q ,不退出请随意输入: ")
        if aaa == "q":
            print("退出成功！")
            break
        else:
            print("请再次输入要查询的账户!")
            continue
# 银行的开户逻辑
def bank_addUser(account,username,password,country,province,street,door,money):
    # 判断用户库是否已满
    if len(bank) >= 100:
        return 3
    # 判断是否存在
    # 获取所有键，然后在判断是否有
    keys = bank.keys()
    if account in keys:
        return 2
    # 正常开户
    bank[account] = {
        "username":username,
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "money":money,
        "bank_name":bank_name
    }
    return 1

# 开户逻辑
def addUser():
    # 生成账号：  8位随机
    string = ""  # 随机数缓冲
    for i in range(8):  # 循环8次取字符
        string = string + "1234567890"[random.randint(0,9)]  # 拼接
    account = string
    print("账号为：",account)
    username = input("请输入姓名：")
    password  = input("请输入密码：")
    print("接下来输入地址信息：")
    country = input("\t输入国家：")
    province = input("\t输入省份：")
    street = input("\t输入街道：")
    door = input("\t输入门牌号：")
    money = int(input("请初始化您的余额："))
    # 调用银行的开户方法
    s = bank_addUser(account,username,password,country,province,street,door,money)

    if s == 1:
        print("开户成功！")
        print("以下是您的开户个人信息：")
        print("***********************")
        print("账号：",account)
        print("用户名：", username)
        print("密码：******")
        print("国家：", country)
        print("省份：", province)
        print("街道：", street)
        print("门牌号：", door)
        print("账户余额：", money)
        print("开户行地址：", bank_name)
        print("***********************")
    elif s == 2:
        print("该用户已存在！")
    elif s == 3:
        print("对不起，该银行已满！请携带证件到其他银行办理！")
while True:
    print(info)
    chose = input("请输入您的选择：")
    if chose == "1":  # 判断是否是1
        addUser()
    elif chose == "2":
        savemoney()
    elif chose == "3":
        take()
    elif chose == "4":
        zhuanzhang()
    elif chose == "5":
        bank_search()
    elif chose == "6":
        print("拜拜了您！")
        break
    else:
        print("输入非法，请重新输入!")