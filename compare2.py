#_*_coding:utf-8_*_
import urllib2
import basicsql
import time
import json
# db=basicsql.connectdb()
# cur=db.cursor()

http_url='https://api-cn.faceplusplus.com/facepp/v3/detect'
# key = "EPJoJtrfDDPB_qzkabXQwANd2w4cWnoH"
# secret = "Kghy_3gjVF7HrJynho5hdnvH0f-jIjab"
#
key = "7VC6OySlWg4ih8AerJQe20SeNUcsNKM3"
secret = "RCIATF28mrBX-tG7yUoYB2NJxC8o-Q0W"
filepath = r"E:\pythonprogram\shumeipai\face\di1.jpg"
boundary = '----------%s' % hex(int(time.time() * 1000))
data = []
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
data.append(key)
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
data.append(secret)
data2=data

def getfacetoken():
    data.append('--%s' % boundary)
    fr=open(filepath,'rb')
    data.append('Content-Disposition: form-data; name="%s"; filename=" "' % 'image_file')
    data.append('Content-Type: %s\r\n' % 'application/octet-stream')
    data.append(fr.read())
    fr.close()
    data.append('--%s--\r\n' % boundary)
# print data

    http_body='\r\n'.join(data)
#buld http request
    req=urllib2.Request(http_url)
#header
    req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
    req.add_data(http_body)
    try:
    #req.add_header('Referer','http://remotserver.com/')
	#post data to server
	    resp = urllib2.urlopen(req, timeout=5).read()
	#get response
	    print resp
        dictinfo = json.loads(resp)

	    result=dictinfo['faces'][0]['face_token']
	# print 'getfacetoken='getfacetoken
    except urllib2.HTTPError as e:
        print e.read()
return result


def compare(getfacetoken):
    data2.append('Content-Disposition: form-data; name="face_token1" ')
    data2.append(getfacetoken)
    data2.append('Content-Disposition: form-data; name="%s" % ''face_token2')
    #数据库获取的人脸比对值
    db = basicsql.connectdb()
    cur = db.cursor()
    cur.execute("select face_token from student where sno=%s" % 4)
    face_token = cur.fetchone()[0]
    print face_token
    basicsql.closedb(db)
    data2.append(face_token)
    http_body='\r\n'.join(data)
#buld http request
    req=urllib2.Request(http_url)
#header
    req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)

    req.add_data(http_body)
    try:
        resp = urllib2.urlopen(req, timeout=5).read()
        print resp
    except urllib2.HTTPError as e:
        print e.read()

if __name__ == '__main__':
    a=getfacetoken()
    compare(a)

    print "Have Done!"
