#!/usr/bin/env python
def login(username, password):
    f = open("db", 'r')  # 读文件
    for line in f:
        l1 = line.split("|")
        if l1[0] == username and l1[1] == password:
            return True
    return False


def regedit(username, password):
    f = open("db", 'a')  # a表示添加
    temp = "\n" + username + "|" + password
    f.write(temp)
    f.close()

def main():
    a = input("1:登陆，2：注册")
    if a == "1":
        username = input("请输入用户名：")
        password = input("请输入密码：")
        r = login(username, password)
        if r == True:
            print("登陆成功")
        else:
            print("登陆失败")
    elif a == "2":
        print("注册")
        user = input("请输入用户名：")
        passwd = input("请输入密码：")
        regedit(user, passwd)

main()
