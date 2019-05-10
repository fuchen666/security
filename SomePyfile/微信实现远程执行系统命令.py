# ！coding = utf-8

import itchat
import os
import time

now_time = (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))  # 定义一个时间撮

info = 'Accept success :' + str(now_time) + '\ndelay 1.5s\nmessage:'  # 定义要发送的内容


@itchat.msg_register(itchat.content.TEXT, itchat.content.PICTURE, itchat.content.RECORDING)  # 接受消息的类型
def main(msg):

    try:

        text = (msg['Text'])  # 接受所有的message

        print(text)

        if "::" in text:

            code = str(text)[2:]

            print(str(now_time) + '\n' + code)

            with open("./message_log.txt", 'a') as r:

                r.write(code + '\n')

                if True:

                    try:

                        status = os.system(code)  # print(s)  # 输入0则执行成功其他值则失败

                        if status == 0:

                            time.sleep(1.5)

                            # 发送给文件助手
                            itchat.send(info + code + '\nstatus:ok', 'filehelper')

                            print('send message ok:1 \n')

                        else:

                            time.sleep(1.5)

                            # 发送给文件助手
                            itchat.send(info + code + '\nstatus:error', 'filehelper')  # 发送给文件助手

                            print('error:0')

                    except:

                        print('a Error！')

    except:

        pass


if __name__ == '__main__':

    itchat.auto_login(hotReload=True)

    itchat.run()
