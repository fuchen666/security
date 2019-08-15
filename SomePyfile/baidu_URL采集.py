import re
import requests
import time
import sys
import random
from urllib.parse import quote,unquote
import threading
from bs4 import BeautifulSoup

result = []

threads = []

def collect(word,pn):

    page = pn // 10
    word = quote(word, "utf-8")
    url = "http://m.baidu.com/ssid=0/from=0/bd_page_type=1/uid=0/baiduid=F0A715FCC08EDFEF3EF12FEDDC2EC810/pu=sz%40224_220%2Cta%40middle____/pu=sz%40224_220%2Cta%40middle___24_74.0/baiduid=31235B9FF0F7A756A7940620CAF109E1/s?ref=www_colorful&lid=12985577237012163036&word=" + word + "&pn=" + str(
        pn) + "&rn=10&tn=middle&prest=111081&st=111091&usm=0&sa=pp"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
    }

    request = requests.get(url, headers=headers)
    soup = BeautifulSoup(request.text, 'html.parser')

    res = soup.find_all('div', class_="resitem")

    for i in res:
        try:
            absClass = i.find('div', class_="abs")
            siteurl = absClass.find('span', class_='site').get_text()
            siteurl = "http://" + siteurl
            title = i.find('a').get_text()
            result.append(siteurl)
            # print(title + " - " + siteurl)
        except:
            pass
        
def save(result,word):
    filename = word + ".txt"

    for i in result:
        with open(filename,"a",encoding="utf-8") as fw:
            url = i.strip()
            fw.write(url+"\n")
            fw.close()

def main(word,pn):
    for i in range(1,pn):
        pn = i * 10
        t = threading.Thread(target=collect,args=(word,pn))
        threads.append(t)
        t.setDaemon(True)
        t.daemon = True
        t.start()

    for t in threads:
        t.join()

    urlList = list(set(result))

    remove = ['http://baike.baidu.com','http://http://zhidao.baidu.com','http://baijiahao.baidu.com','http://wk.baidu.com']

    try:
        for i in remove:
            if i in urlList:
                urlList.remove(i)
    except:
        pass

    total = len(urlList)

    save(urlList,word)

    return total

if __name__ == "__main__":
    word = sys.argv[1]
    pn = int(sys.argv[2])
    print("正在采集...")
    total = main(word,pn)
    print("本次共采集 " + str(total) + " 个域名")
    print("采集结束")