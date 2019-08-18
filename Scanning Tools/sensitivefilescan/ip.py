import requests

url = "http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=708c958bcbfc48a5980bed32dab9241c&orderno=YZ20189122795ZTgI8J&returnType=2&count=1"

re = requests.get(url)

print(re.text)


