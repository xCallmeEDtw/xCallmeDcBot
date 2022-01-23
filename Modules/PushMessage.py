import requests
import json
import os
def PushMessage(messages):
    #請使用自己的token
    accessToken = os.environ.get('ACCESS_TOKEN', None)  
    
    headers ={
        'Content-Type':'application/json',
        'Authorization': 'Bearer '+accessToken
    }
    data ={
        'to':'Uaecc02e8daa06d7ca2d504e30736fa26',
        'messages':messages
    }
    url = 'https://api.line.me/v2/bot/message/push'
    r = requests.post(url,headers=headers,data=json.dumps(data))
    return r