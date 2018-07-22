import itchat
from itchat.content import TEXT
import datetime
import locale


@itchat.msg_register(TEXT, isFriendChat=True, isGroupChat=False, isMpChat=True)
def simple_reply(msg):
#    locale.setlocale(locale.LC_ALL, '')
    if "几点了" in msg.text:
        # print(time.strftime('%H'))
        return_text = datetime.timedelta(hours=14)+datetime.datetime.now()
        return 'The time is {}'.format(return_text)
    elif "爱你" in msg.text:
        return '爱你too'
    elif '哈哈哈哈哈' in msg.text:
        return '哈'*130
    pass
itchat.auto_login(hotReload=True, enableCmdQR=2)
itchat.run()
