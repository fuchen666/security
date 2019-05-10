#coding=utf-8
#@Author: Ppbibo


from socket import gethostbyname
# import threading
import multiprocessing
import sys

class Batch_Demain_Conversion_IP(multiprocessing.Process):

    '''
        实现域名批量转换IP

    '''

    def __init__(self):

        super().__init__()

        self.demoList = []
        try:
            file = open('doamin.txt', 'r', encoding='utf-8')
        except:

            print("[-] 不存在 doamin.txt 文件")
            sys.exit()

        for e in file.readlines():
            a = "".join(e.split('\n'))

            if "http://" in a:
                a = a.strip('http://')

            if "https://" in a:
                a = a.strip('https://')

            if a.endswith('/'):
                a = a.strip('/')

            self.demoList.append(a)


    def run(self):

        for i in self.demoList:

            try:

                host = gethostbyname(i)

            except:

                print("[-] error: {}".format(i))

            print("[+] 域名：{} ====> IP：{}".format(i,host))

            with open("save.txt","a") as f:

                f.write(host+"\n")

        print('[Tips] Please open file `save.txt`')



if __name__ == '__main__':

    Batch_Demain_Conversion_IP().start()

