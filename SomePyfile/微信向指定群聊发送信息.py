# ！coding = utf-8

import itchat


context = "系统自动发送的message"

def SentChatRoomsMsg(name, context):

    '''
    指定群聊发送message
    '''

    try:

        itchat.get_chatrooms(update=True)  # 获取群组所有的相关信息（注意最好群聊保存到通讯录）

        iRoom = itchat.search_chatrooms(name)  # 传入指定群名进行搜索

        # print(iRoom)  # 输出一个群聊信息列表

        for room in iRoom:

            print(room["NickName"])  #

            print(room['UserName'])  #  得到群名的唯一标识，进行信息发送

            #  遍历所有NickName为键值的信息进行匹配群名
            if room["NickName"] == name:

                userName = room['UserName']  # 得到群名的唯一标识，进行信息发送

                itchat.send_msg(context, userName)

                print("发送message ：ok")

            else:

                print('No groups found!')

    except:

        pass

if __name__ == '__main__':

    itchat.auto_login(hotReload=True)

    SentChatRoomsMsg("🙌🙌🙌🙌", context)  # 群名

    itchat.run()

