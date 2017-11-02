#encoding:utf-8
#发现网上都是用的sqlite3，或者就是mysql+Flask-SQLAlchemy之类的，感觉SQLAlchemy看上去很复杂
#这里我用基础的MySQLdb完成
#__author__ lenox-syx

from flask import Flask,render_template,request
import MySQLdb
import json
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method=="POST":

        username= request.form.get('username')
        password= request.form.get('password')
        # m=15002100000
        number1=str(username)
        # print type(number)
        conn = MySQLdb.connect(host='localhost',port=3306,user='root',passwd='Qq123456789',db='qinshenshen', )
        cur = conn.cursor()
        judge=cur.execute('select * from teacher where ttel= "%s"'%number1)
        print judge
        if judge:
            info=cur.fetchone()
            if str(password)==info[4] :
                # name1=info[1]
                return render_template("user.html", name=info[1])
        else:
            return "<h1> 用户不存在</h1>"
    return "<h1>密码错误 !<h1>"


@app.route("/user/<name>")
def user(namex):
    return render_template("user.html",name=username)



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
