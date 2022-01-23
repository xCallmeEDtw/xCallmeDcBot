import requests
import json
import os

def Notify(token):
    #請使用自己的token
    # token = 'XS8TqlR25XtCraBFyk1Ud4a2KOizLIX051P6q4euTyx'
    accessToken = token

    headers ={
        'Content-Type':	'application/x-www-form-urlencoded',
        'Authorization': 'Bearer '+accessToken
    }
    data ={
        'message':'恭喜你註冊成功，請勿封鎖此帳號，會收不到通知哦!! '
    }
    url = 'https://notify-api.line.me/api/notify'
    r = requests.post(url,headers=headers,data=data)

    print(r.text)