from wechat_sdk import WechatBasic, WechatConf


def wechat_resp(token='', appid='', appsecret='', encoding_aes_key='', encrypt_mode='', signature='', timestamp='', nonce='', echostr=''):
    conf = WechatConf(token=token, appid=appid, appsecret=appsecret,
                      encoding_aes_key=encoding_aes_key, encrypt_mode=encrypt_mode)
    wechat = WechatBasic(conf=conf)
    wechat.get_access_token()
    body_text = """
<xml>
<ToUserName><![CDATA[touser]]></ToUserName>
<FromUserName><![CDATA[fromuser]]></FromUserName>
<CreateTime>1405994593</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[wechat]]></Content>
<MsgId>6038700799783131222</MsgId>
</xml>
"""
    if wechat.check_signature(signature=signature, timestamp=timestamp,
                              nonce=nonce):
        wechat.parse_data(body_text
        wechat.get_access_token()
        return 'echostr'
    else:
        return 'False'
