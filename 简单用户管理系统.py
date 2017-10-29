'''
程序中用到的模块解释如下：
(1) re：正则表达式引擎，Python中调用正则表达式的方法
(2) pickle：对象持久化，将数据写入到磁盘中
(3) datetime：时间处理，用于记录用户登陆时间戳
(4) base64：base64加密模块
(5) hashlib：hash加密模块
'''

#-*- coding:utf-8 -*-
#2015-04-05

import re
import pickle
import base64,hashlib
from datetime import datetime   

def Initialization(file_name):
    '''程序初始化，创建user.ini和time.ini文件'''
    dict_test={'admin':'db69fc039dcbd2962cb4d28f5891aae1'}  #创建超级管理员，默认密码为admin
    f = file(file_name,'a+')   #以追加的方式打开文件，避免文件被修改
    if len(f.readlines()) ==0:  #判断程序是否为空，只在第一次运行的时候初始化
        if file_name=='user.ini':
            pickle.dump(dict_test, f, True)
        else:
            pickle.dump({},f, True)
    f.close()

def encodepass(passwd):
    '''采用base64和md5双层加密，破解可能几乎为0'''
    m = hashlib.md5()
    pwd = base64.b64encode(passwd)
    m.update(pwd)
    return m.hexdigest()

def time_order(user):
    '''记录用户登陆时间，结果保存在time.ini文件中'''
    ft = file('time.ini','r')
    dbt = pickle.load(ft)
    if user not in dbt:
        dbt.setdefault(user,datetime.today())
    else:
        time_value = dbt[user]
        t = datetime.today()-time_value
        try:
            if t.hour<=4:
                print 'You already logged in at:<last_login_timestamp>'
        except:
            print 'You already logged in at:<last_login_timestamp>'
        dbt[user] = datetime.today()
    ft = file('time.ini','w')
    pickle.dump(dbt, ft, True)
    ft.close()
        

def newuser(db):
    '''用户创建程序，由olduser调用'''
    while True:
        name = raw_input('Please input the username:')
        if re.match(r'\w', name):   #采用正则表达式检测用户名是否合法
            pass
        else:
            print 'Username should be made of A~Z、a~z、0~9、_'
            continue
        for valuename in db.keys():
            if name.lower() == valuename.lower():
                break
        else:
            break
    passwd = raw_input('Please input the password:')
    db[name] = encodepass(passwd)
    
def olduser(db):
    '''用户登陆程序'''
    name = raw_input('Login:')
    if name in db:
        pwd = raw_input('passwd:')
        passwd = db.get(name)
        if passwd == encodepass(pwd):
            print 'Welcome back!',name
            time_order(name)
        else:
            print 'Login incorrent!'
    else:
        YN = raw_input('Do you want to instead a new user? Yes or No:')
        if YN.lower()=='yes':
            newuser(db)
    print '\n',
        
def deluser(db):
    '''删除一个用户，但必须以管理员的身份'''
    print 'Please login as admin'  #管理员的身份才能删除用户
    name = raw_input('Login:')
    pwd = raw_input('passwd:')
    passwd = db.get(name)
    if passwd == encodepass(pwd) and name=='admin':
        user = raw_input('Please input a user name:')
        if user != 'admin':
            if db.pop(user):
                print 'Delete Current!'
        else:
            print 'Con not delete admin!'
    else:
        print 'Wrong passwprd'
    
def checkuser(db):
    '''查看所有用户，但必须以管理员的身份'''
    print 'Please login as admin'  #管理员的身份才能查看所有用户
    name = raw_input('Login:')
    pwd = raw_input('passwd:')
    passwd = db.get(name)
    if passwd == encodepass(pwd) and name == 'admin':
        for key in db:
            print 'username: %10s ====> password: %10s' % (key,db[key])
    else:
        print 'You can not check all users!'

def resetuser(db):
    '''修改密码，但必须正确的输入老密码'''
    name = raw_input('Please input the username：')
    passwd  = raw_input('Please input old password：')
    if db[name] == encodepass(passwd):
        passwd = raw_input('Please input new password：')
        db[name] = encodepass(passwd)
    else:
        print 'Wrong password!'

def showmenu():
    '''程序运行的主函数'''
    fu = file('user.ini','r')
    db = pickle.load(fu)
    prompt = '''(L)ogin Now
(Q)uit
(D)elet User
(C)heck All User
(R)eset Password
Enter choice:'''
    
    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).split()[0].lower()
            except (EOFError,KeyboardInterrupt):
                choice = 'q'
            print '\nYou picked:[%s]' % choice
            if choice not in 'lqdcr':
                print 'invalid option,try again'
            else:
                chosen = True
                    
        if choice == 'q':done = True
        if choice == 'l':olduser(db)
        if choice == 'd':deluser(db)
        if choice == 'c':checkuser(db)
        if choice == 'r':resetuser(db)
        
    fu = file('user.ini','w')
    pickle.dump(db,fu,True)
    fu.close()
        
        
if __name__ == '__main__':
    '''系统有一个用户名为admin 密码为admin的超级用户,请立即修改密码！'''
    print 'Welcome to User Information Management System!'
    Initialization('user.ini')
    Initialization('time.ini')
    showmenu()

