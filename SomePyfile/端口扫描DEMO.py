#! coding = utf-8


from socket import *
import threading
import time

portList = [21, 22, 23, 25, 53, 67, 80, 110, 139, 161, 389, 443, 445, \
            1080, 1433, 3306, 5432, 6379,27017, 5000, 3389, 4848, 7001, 2601, 3389, 8080, 5900, 11211, 2181]

thread = []

def portScan(host,port):

    try:

        s = socket(AF_INET,SOCK_STREAM)

        s.connect((host,port))

        print('[+] {} open'.format(port))

        print('[+] {} open'.format(port),file=open('save.txt','a'))

        s.close()

    except:

        print('[-] {} close'.format(port))


if __name__ == '__main__':

    for port in portList:

        t = threading.Thread(target=portScan,args=('127.0.0.1',port),)

        thread.append(t)

        t.start()

        time.sleep(0.1)

    try:

        t.daemon()

        t.join()

    except:

        pass

    print('扫描结束')