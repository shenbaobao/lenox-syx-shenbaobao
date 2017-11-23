import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)
import urllib2
import basicsql
import json

url="https://api-cn.faceplusplus.com/facepp/v3/compare"
key = "7VC6OySlWg4ih8AerJQe20SeNUcsNKM3"
secret = "RCIATF28mrBX-tG7yUoYB2NJxC8o-Q0W"
filepath = r"E:\pythonprogram\shumeipai\face\di2.jpg"
data=[]
data.append('Content-Disposition: form-data; name="%s"\n' % "api_key")
data.append(key)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
data.append(secret)
no=4

def getfacetoken(no):
    db = basicsql.connectdb()
    cur = db.cursor()
    cur.execute("select face_token from student where sno=%s" %no)
    face_token=cur.fetchone()[0]
    # print face_token
    basicsql.closedb(db)
    return face_token

def getdata(adding,filepath):
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'face_token2')
    data.append(adding)
    # fr = open(filepath, 'rb')
    data.append('Content-Disposition: form-data; name="%s"; filename=" "' % 'image_file1')
    data.append('E:\pythonprogram\shumeipai\\face\di2.jpg')

    http_body = '\r\n'.join(data)
    print http_body
    return http_body


def compareface(http_body):
    try:
        data=urllib2.urlopen(url,data=http_body).read()
        print data

    except urllib2.HTTPError as e:
        print e.read()
if __name__ == '__main__':
    add=getfacetoken(no)
    http_body=getdata(add,filepath)
    compareface(http_body)

    print "Have Done!"



