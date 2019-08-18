'''
author:jiushi
time:2019/7/6
file:port_scan.py
'''

from gevent import monkey;monkey.patch_all()
from gevent.lock import RLock
from multiprocessing import Process
import socket
import IPy
import gevent
import config


rlock=RLock()

class Scan(object):
    def __init__(self,*args,**kwargs):
        self.host=args[1]
        self.port=args[0]
        self.djc=[]
        self.calc=0
        self.xc_list=[]

    def port_scan(self,host,port):
        global banner
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(2)
        try:
            s.connect((str(host),int(port)))
            print('[+] host:{} port:{} status:open'.format(host, port))
            s.sendall(b'banner')
            banner=s.recv(1024)
            print('banner:{}'.format(bytes.decode(banner,encoding='utf-8')))
        except Exception as r:
            if 'UnicodeDecodeError' in str(r):
                print('banner:{}'.format(banner))
            else:
                pass

    def xc(self,rw):
        rlock.acquire()
        for r in rw:
            for g in range(self.port[0],self.port[1]):
                self.xc_list.append(gevent.spawn(self.port_scan,r,g))
        rlock.release()
        gevent.joinall(self.xc_list)

    def run_process(self):
        ip=IPy.IP(self.host)
        for c in ip:
            if self.calc==100:
                p=Process(target=self.xc,args=(self.djc,))
                p.start()
                self.djc.clear()
                self.calc=0
            self.djc.append(c)
            self.calc+=1
        if len(self.djc)>0:
            p = Process(target=self.xc, args=(self.djc,))
            p.start()

if __name__ == '__main__':
    obj=Scan(config.PORT_FAN,config.IP)
    obj.run_process()