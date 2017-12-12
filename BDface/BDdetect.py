# coding=utf-8
###################
#勤深深语萌萌树莓派考勤机---百度人脸采集
#  @syx
###################
from aip import AipFace
'''
APP_ID='10269987'
API_KEY='ajqYXWPzZUVhIZxQcuWi1vA7'
SECRET_KEY='2aefa7bf10a7ca6b91127412c6446ffa'
'''
APP_ID='10522678'
API_KEY='V21FC4N90bTuMxk0qMixX5o1'
SECRET_KEY='OqMDdmsFIXcHpA7wN5I6aeej2wZq8PIF'
#初始化AipSpeech对象
aipface = AipFace(APP_ID,API_KEY,SECRET_KEY)

def get_file_content(filePath):
    with open(filePath,'rb') as fp:
        return fp.read()

def detectFace(filePath):
    options={'max_face_num':1,'face_fields':"age,beauty,expression",}
    result=aipface.detect(get_file_content(filePath),options)
    # if result['error_code']):
    #     print result['error_code'] + result['error_msg']
    # 这里想做一个错误处理，如果百度人脸返回错误码，存在错误码则先是错误信息，不存在参数'error_code'则返回正常脸部信息，
    # 如何判断返回值中是否有参数'error_code'
    # else:

    print result
    print len(result['result'][0])
    if len(result['result'])==0:
        print 'no face in picture!'
    else:
        faceinfo={'beauty':result['result'][0]['beauty'],
              "age":result['result'][0]['age'],
              "expression":result['result'][0]['expression']}

        print faceinfo

# detectFace("meilian.jpg")
detectFace('../face/di1.jpg')
