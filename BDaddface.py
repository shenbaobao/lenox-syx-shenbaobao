# coding=utf-8
from aip import AipFace
APP_ID='10522678'
API_KEY='V21FC4N90bTuMxk0qMixX5o1'
SECRET_KEY='OqMDdmsFIXcHpA7wN5I6aeej2wZq8PIF'
#初始化AipSpeech对象
aipface = AipFace(APP_ID,API_KEY,SECRET_KEY)
def get_file_content(filePath):
    with open(filePath,'rb') as fp:
        return fp.read()
dilireba='../face/di1.jpg'
wulei='../face/wulei1.jpg'
zhangyishan="../face/zhangyishan1.jpg"
# aipface.addUser(uid='uid1',groupId='group1',image=get_file_content(dilireba),userInfo='迪丽热巴')
# aipface.updateUser(uid='uid1',groupId='group1',image=get_file_content(dilireba),userInfo='dilireba')
# print aipface.addUser(uid='uid2',groupId='group1',image=get_file_content(wulei),userInfo='吴磊')
print aipface.addUser(uid='uid3',groupId='group1',image=get_file_content(zhangyishan),userInfo='张一山')

print aipface.getGroupUsers('group1')['result'][2]['user_info']

