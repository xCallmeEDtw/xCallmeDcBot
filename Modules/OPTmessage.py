import json
def MessageAdd(m_add,m_type):

    if m_type == 'sticker':
         
        addtion = {
                "type":"sticker",
                "packageId": m_add[0],
                "stickerId": m_add[1]
                
                }
    elif m_type =='image':
        
        addtion={
                "type":"image",
                "originalContentUrl": m_add,
                "previewImageUrl": m_add
                }
    elif m_type =='text':
        
        addtion={
                "type":"text",
                "text": m_add
                }
    elif m_type == 'flex':
        addtion = {
            "type": "flex",
            "altText": m_add[0],
            "contents": m_add[1]
        }
    return addtion
