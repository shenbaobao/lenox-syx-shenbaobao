# coding=utf8
from basicsql import connectdb,closedb
import MySQLdb
import requests
import json
# key = "7VC6OySlWg4ih8AerJQe20SeNUcsNKM3"
# secret = "RCIATF28mrBX-tG7yUoYB2NJxC8o-Q0W"
#api1
# key = "EPJoJtrfDDPB_qzkabXQwANd2w4cWnoH"
# secret = "Kghy_3gjVF7HrJynho5hdnvH0f-jIjab"
#api3
# key=7UZkZd4vgH1UeOPg3LiXEzRxJleJTHum
# secret=5aj9y0FkZa42_c1kmbkmRl9n8WptbFVT

# 'api_key': 'wRtmsh3Df9e6UnzKfoTQQl1YUwCrgIjG',
           # 'api_secret': '04wlI86pykQAssFEAeVS0QTZgMb5gEW',
print "输入要识别的学生学号"
student=raw_input()
db = connectdb()
cur=db.cursor()
cur.execute("select face_token from student where sno=%s" %student)
facetoken = cur.fetchone()[0]
# facetoken="e648e6aca10183458dd5a3aa1270db4e"
url = 'https://api-cn.faceplusplus.com/facepp/v3/compare'
files = {'image_file1': open('face/di1.jpg', 'rb')}
payload = {'api_key': '7UZkZd4vgH1UeOPg3LiXEzRxJleJTHum',
           'api_secret': '5aj9y0FkZa42_c1kmbkmRl9n8WptbFVT',
           'face_token2':facetoken}

r = requests.post(url, files=files, data=payload)
data = json.loads(r.text)
print r.text
# print data
if data['confidence']:
    data['confidence']>60
    print "the same"
elif data['confidence']<=60:
    print "different"
else:
    print 'error'
 '''   
运行结果：    
输入要识别的学生学号
4
{
"faces1": [{"face_rectangle": {"width": 198, "top": 273, "left": 241, "height": 198},
"face_token": "e60d78b8baded9229bf4b5dcfd7f3445"}], 
"confidence": 84.851, 
"image_id1": "PjF8RYWtkmVt8IZdbIs3IA==",
"request_id": "1512285689,7fd55f65-1af1-4ea5-a752-e0613ba767f2", 
"time_used": 459, 
"thresholds": {"1e-3": 62.327, "1e-5": 73.975, "1e-4": 69.101}
}
the same
