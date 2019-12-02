# encoding:utf-8
import requests
import json
import base64
import os
from tkinter import filedialog


# client_id 为官网获取的AK， client_secret 为官网获取的SK
# host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&' \
#        'client_id=FhRmh20HRsQW00Dq4S8SfK5f&client_secret=QMB5buaw9ZEVmuU6qgOwKjcqEbDREfZG'
# response = requests.get(host)
# if response:
#     access_token = response.json()
#     # print(access_token)
#     print(response.json())

# 获取access_token的函数, access_token会一一个月更新一次, 注意过期
def get_token():
    url = 'https://aip.baidubce.com/oauth/2.0/token'
    data = {}
    data['grant_type'] = 'client_credentials'
    data['client_id'] = 'FhRmh20HRsQW00Dq4S8SfK5f'
    data['client_secret'] = 'QMB5buaw9ZEVmuU6qgOwKjcqEbDREfZG'

    response = requests.post(url, data)
    content = response.content.decode('utf-8')
    content = json.loads(content)
    # print('获取到的access_token为:\r',content['access_token'])
    return content['access_token']


def picture_encode(image):
    f1 = open(image, 'rb')
    f1_64 = base64.b64decode(f1.read())
    f1.close()
    f1_64 = f1_64.decode()
    return f1_64


def add_face(face1, face2, image):
    requesu_url = 'https://aip.baidubce.com/rest/2.0/face/v1/merge' + "?access_token=" + get_token()
    params = {
        "image_template": {"image": picture_encode(face1), "image_type": 'BASE64'},
        "image_target": {"image": picture_encode(face2), "image_type": 'BASE64'}
    }
    params = json.dumps(params)
    this_headers = {'content-type': 'application/json'}
    response = requests.post(requesu_url, params, headers=this_headers)
    req_con1 = response.content.decode('utf-8')

    content = eval(req_con1)
    result = content['result']['merge_']
