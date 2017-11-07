#encoding:utf-8
#发现网上都是用的sqlite3，或者就是mysql+Flask-SQLAlchemy之类的，感觉SQLAlchemy看上去很复杂
#这里我用基础的MySQLdb完成
#__author__ lenox-syx

#11.7，今天找到了数据表格的操作结合table.html实现把数据库里的表格显示在网页上
#这里基础的连接数据库的操作可以写在一个a.py文件，然后通过a.func（）调用里面的函数，我写了一个把basicsql.py，
# 就是在注释里两个函数，也可以直接写在这里。有两种尝试。

from flask import Flask,render_template,request
# import MySQLdb
import basicsql

app = Flask(__name__)
'''
def connectdb():
	db = MySQLdb.connect(host='localhost', user="root", passwd='Qq123456789', db='qinshenshen', port=3306, charset='utf8')
	db.autocommit(True)
	cursor = db.cursor()
	return (db,cursor)

# 关闭数据库
def closedb(db,cursor):
	db.close()
	cursor.close()
'''
@app.route("/")
def index():
    return render_template("login1.0.html")

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method=="POST":

        username= request.form.get('username')
        password= request.form.get('password')
        # m=15002100000
        number1=str(username)
        # print type(number)
        (db, cursor) = basicsql.connectdb()
        judge=cursor.execute('select * from teacher where ttel= "%s"'%number1)
        print judge  #控制端获得数据，是否登录成功
        if judge:
            info=cursor.fetchone()
            if str(password)==info[4] :
                # name1=info[1]
                return render_template("user.html", name=info[1])
        else:
            return "<h1> 用户不存在</h1>"
        basicsql.closedb()
    return "<h1>密码错误 !<h1>"

@app.route("/table")
def table():
        # 连接数据库
        (db, cursor) = basicsql.connectdb()
        # 获取数据
        cursor.execute("select tno,tname,ttel from teacher")
        posts = cursor.fetchall()
        # 关闭数据库
        basicsql.closedb(db, cursor）
        # 后端向前端传递数据
        return render_template('table.html', posts=posts)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0
