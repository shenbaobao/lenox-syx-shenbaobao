# coding=utf-8
###################
#勤深深语萌萌树莓派考勤机---百度人脸识别
#  @syx
###################
from aip import AipFace
APP_ID='10522678'
API_KEY='V21FC4N90bTuMxk0qMixX5o1'
SECRET_KEY='OqMDdmsFIXcHpA7wN5I6aeej2wZq8PIF'
#初始化AipSpeech对象
aipface = AipFace(APP_ID,API_KEY,SECRET_KEY)

dilireba='../face/di1.jpg'
dilireba2='../face/di2.jpg'
wulei='../face/wulei1.jpg'
zhangyishan1="../face/zhangyishan1.jpg"
zhangyishan2="../face/zhangyishan2.jpg"
def get_file_content(filePath):
    with open(filePath,'rb') as fp:
        return fp.read()

def identyfyuser(filePath):
    identify=aipface.identifyUser(image=get_file_content(filePath),groupId='group1')
    # print identify
    # print identify.has_key('result')
    '''
    # 判断key 'result'是否在dict中的方法(1,dict.has_key())(2如下)
    if 'result' in identify.keys():
        print 1
    else:
        print 0
    '''
    if identify.has_key('result'):
        if len(identify["result"])!=0:
            score=identify["result"][0]['scores']
            userinfo=identify["result"][0]['user_info']
            if score>80:
                end=userinfo
            else:
                end=userinfo
        else:
            end='no face'
    elif identify.has_key('error_code'):
       end=result['error_code'] + result['error_msg']
    return end

# identyfyuser(dilireba2)