#!coding=utf-8


import requests,multiprocessing
from bs4 import BeautifulSoup



class Monscan(multiprocessing.Process):


    def __init__(self):

        multiprocessing.Process.__init__(self)

        self.domainList = []

        #User-Agent
        self.header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
         Chrome/44.0.2403.125 Safari/537.36','Connection':'close'}


        file = open('url.txt','r')
        for item in file.readlines():
            url="".join(item.split('\n'))
            self.domainList.append("http://"+url)

    def run(self):


            for url in self.domainList:

                try:

                    re = requests.get(url,headers=self.header,timeout=10)

                    if re.status_code == 200:

                        # print(url+"=======>"+re.encoding)

                        print(url)

                        if re.encoding == "ISO-8859-1":

                            re.encoding = 'utf-8'

                        if re.encoding == 'GB2312':

                            re.encoding = 'gbk'

                        html = BeautifulSoup(re.text, 'lxml')
                        print(html.title.text)

                    else:

                        print(url)

                        continue

                except:

                    print(url)

                    continue



if __name__ == '__main__':

    a = Monscan()

    a.start()
