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
    elif ':task' in msg.text:
        with open('task.txt',mode='a',encoding='utf-8') as f:
            f.write(msg.text.replace(':task','')+'\n')
        return "Task saved"
    elif ':gettask' in msg.text:
        response = None
        with open('task.txt', mode='r+') as f:
            response = f.readlines()
        response_text = ''
        for i in range(len(response)):
            response_text = response_text + str(i) + '. '+response[i] + '\n'
        print(response_text)
        return response_text
    pass
itchat.auto_login(hotReload=True, enableCmdQR=2)
itchat.run()
