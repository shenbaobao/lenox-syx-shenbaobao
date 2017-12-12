# coding=utf-8
###################
#勤深深语萌萌树莓派考勤机---百度人脸两两对比
#  @syx
###################
from aip import AipFace
APP_ID='10522678'
API_KEY='V21FC4N90bTuMxk0qMixX5o1'
SECRET_KEY='OqMDdmsFIXcHpA7wN5I6aeej2wZq8PIF'
#初始化AipSpeech对象
aipface = AipFace(APP_ID,API_KEY,SECRET_KEY)


dilireba='../face/di1.jpg'
wulei='../face/wulei1.jpg'
zhangyishan1="../face/zhangyishan1.jpg"
zhangyishan2="../face/zhangyishan2.jpg"
def get_file_content(filePath):
    with open(filePath,'rb') as fp:
        return fp.read()
match=aipface.match([get_file_content(zhangyishan1),
                     get_file_content(zhangyishan2),
                     get_file_content(wulei)])
print match