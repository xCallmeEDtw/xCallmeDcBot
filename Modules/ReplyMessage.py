import requests
import json

def ReplyMessage(replyToken,messages):
    #請使用自己的token
    accessToken = 'LTaTHoeYkfTYpyCtqRwQX2wlaQniteHxFQsrK6tRIGhtn+SLOA9Wef6oDEGtlBIrxFbQPNI3aNfdHLSgGELZRl2iCIwE1zYB2i0QA6K2CxoutgsNsHZr097uFTAfIA1Bdv/Dg83ud3qUpDa92w6FCQdB04t89/1O/w1cDnyilFU='

    headers ={
        'Content-Type':'application/json',
        'Authorization': 'Bearer '+accessToken
    }
    data ={
        "replyToken":replyToken,
        'messages':messages
    }
    url = 'https://api.line.me/v2/bot/message/reply'
    r = requests.post(url,headers=headers,data=json.dumps(data))
    return r
