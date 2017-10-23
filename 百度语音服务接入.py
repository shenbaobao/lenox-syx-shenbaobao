#encoding:utf-8
from aip import AipSpeech
import json
# 定义常量，此处替换为你自己的应用信息
APP_ID='10269987'
API_KEY='ajqYXWPzZUVhIZxQcuWi1vA7'
SECRET_KEY='2aefa7bf10a7ca6b91127412c6446ffa'
#初始化AipSpeech对象
aipSpeech = AipSpeech(APP_ID,API_KEY,SECRET_KEY)
# 读取文件
def get_file_content(filePath):
    with open(filePath,'rb') as fp:
        return fp.read()
# 识别本地文件
result = aipSpeech.asr(get_file_content('test.pcm'),'pcm',8000)
#目前支持式较少，原始 PCM 的录音参数必须符合 8k/16k 采样率、16bit 位深、单声道，支持的格式有：pcm（不压缩）、wav（不压缩，pcm编码）、amr（压缩格式）。
print result
print (json.dumps(result).decode('unicode-escape'))
print (json.dumps(result['result']).decode('unicode-escape'))


运行结果
================= RESTART: E:\大三上\pythonfile\百度语音.py =================
{u'err_no': 0, u'corpus_no': u'6480132887577771721', u'err_msg': u'success.', u'result': [u'\u767e\u5ea6\u8bed\u97f3\u63d0\u4f9b\u6280\u672f\u652f\u6301\uff0c'], u'sn': u'274616879581508773510'}
{"err_no": 0, "corpus_no": "6480132887577771721", "err_msg": "success.", "result": ["百度语音提供技术支持，"], "sn": "274616879581508773510"}
["百度语音提供技术支持，"]
>>> 
