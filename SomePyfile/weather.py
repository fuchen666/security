# coding:utf-8

import time
import requests
import json
import itchat


time_n = (time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time())))  # 获取当前系统时间（精确到分钟）

def weather():

    '''陈婷婷

    天气接口调用

    参考文章：

    https://www.sojson.com/blog/305.html

    http://t.weather.sojson.com/api/weather/city/101130801'''

    try:

        url = "http://t.weather.sojson.com/api/weather/city/101130801"  # 阿克苏地

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}

        r = requests.get(url,headers=headers,timeout=3)

    except:

        print('出现了一点故障：请求失败啦')

    try:
        '''获取当天的天气'''

        time = (json.loads(r.text)['time'])  # 系统更新时间

        city = (json.loads(r.text)['cityInfo']['city'])  # 请求城市

        updateTime = (json.loads(r.text)['cityInfo']['updateTime'])  # 天气更新时间

        message = (json.loads(r.text)['message'])  # 返回状态

        forecast = (json.loads(r.text)['data']['forecast'][0]['week'])  # 日期（周几）

        sunrise = (json.loads(r.text)['data']['forecast'][0]['sunrise'])  # 日出

        high = (json.loads(r.text)['data']['forecast'][0]['high'])  # 当天最高温

        low = (json.loads(r.text)['data']['forecast'][0]['low'])  # 当天最低温

        sunset = (json.loads(r.text)['data']['forecast'][0]['sunset'])  # 日落

        aqi = (json.loads(r.text)['data']['forecast'][0]['aqi'])  # 空气指数

        fx = (json.loads(r.text)['data']['forecast'][0]['fx'])  # 风向

        fl = (json.loads(r.text)['data']['forecast'][0]['fl'])  # 风力

        type = (json.loads(r.text)['data']['forecast'][0]['type'])  # 天气

        notice = (json.loads(r.text)['data']['forecast'][0]['notice'])  # 天气描述

    except:

        pass

    if 0 <= aqi <= 50:

        zhidu = (str(aqi) + ' (优)\n' + '[Tips]大口的呼吸新鲜空气吧😌')

    elif 51 <= aqi <= 100:

        zhidu = (str(aqi) + ' (良)\n' + '[Tips]空气不错出去走走哦😌')

    elif 101 <= aqi <= 150:

        zhidu = (str(aqi) + ' (轻度污染)\n' + '[Tips]适量减少户外运动😯')

    elif 151 <= aqi <= 200:

        zhidu = (str(aqi) + ' (中度污染)\n' + '[Tips]适量减少户外运动😯')

    elif 201 <= aqi <= 300:

        zhidu = (str(aqi) + ' (重度污染)\n' + '[Tips]适量减少户外运动，外出带口罩安😢')

    elif aqi > 300:

        zhidu = (str(aqi) + ' (严重污染)\n' + '[Tips]尽量不要户外运动，外出带口罩安😢')

    else:

        pass

    data = ("城市: %s🏠\n" \
           "今天是: %s🌟\n" \
           "最%s \n"
            "最%s \n"
            "空气指数: %s\n"
            "风向: %s \n"
            "风力: %s \n"
            "天气: %s \n"
            "天气更新时间: %s \n"
            "爱你❤%s") % (city,forecast,high,low,zhidu,fx,fl,type,updateTime,notice)

    return data


@itchat.msg_register(itchat.content.TEXT,itchat.content.PICTURE,itchat.content.RECORDING)   # 接受消息的类型
def send(msg):

    ''' 微信发送信息 '''

    try:

        text = (msg['Text'])  # 接受所有的message

        with open("./all_log.txt", 'a') as r:

            r.write(str(time_n) + '\n' + text + '\n')

        print(str(time_n) + '\n' + str(text))

        count = '*'

        

        if "老公早安" in text or "老婆早安" in text:

            itchat.send(u'陈婷婷的天气预报❤️\n' + weather(), 'filehelper')  # 发送给文件传输助手

            user = itchat.search_friends(name=u'Pamper the little girl❤️')[0]  # 发送给指定朋友
                
            user.send(u'陈婷婷的天气预报❤️\n'+ weather())

            weather_log = ('message:weather send ok!!!')

            print(weather_log)

            with open("./weather_log.txt", 'a') as r:

                r.write('[' + str(count) + ']' + str(time_n)+'\n'+weather_log + '\n')

          

    except Exception as e:

        print("Error",e)

if __name__ == '__main__':

    try:
        # print(weather())
        itchat.auto_login(hotReload=True)
        itchat.run()

    except:

        print('[!]Error => itchat not running！！！')

