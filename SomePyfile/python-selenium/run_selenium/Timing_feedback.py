#! coding = utf-8


import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import requests


def main(User,Passwd):

    try:

        driver = webdriver.Firefox()

        # driver.implicityly_wait(3)  # 使用30秒隐式等待时间来定义Selenium执行步骤的超时时间

        if driver:

            driver.get("http://tlias-stu.boxuegu.com/#/login ")

            time.sleep(1)

            userName = driver.find_element_by_xpath('/html/body/div/div/div[3]/div/div/div[2]/form/div[1]/div/div/div[1]/input')

            userName.send_keys(User)

            time.sleep(1)

            passWord = driver.find_element_by_xpath('/html/body/div/div/div[3]/div/div/div[2]/form/div[2]/div/div/div[1]/input')

            passWord.send_keys(Passwd)

            time.sleep(1)

            driver.find_element_by_xpath('/html/body/div/div/div[3]/div/div/div[2]/form/button').click()

            if True:

                print('[*] login ok:1')

                time.sleep(3)

                driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/span').click()

                time.sleep(3)

                driver.find_element_by_xpath('/html/body/div/div/div[2]/ul/li[1]/div/label[1]/span[1]/span')

                time.sleep(2)

                driver.get("/html/body/div/div/div[2]/ul/li[2]/div/label[1]/span[1]/span")

                time.sleep(2)

                driver.get("/html/body/div/div/div[2]/ul/li[3]/div/label[1]/span[1]/span")

                time.sleep(2)

                driver.get("/html/body/div/div/div[2]/ul/li[4]/div/label[1]/span[1]/span")

                time.sleep(3)

                fankui = driver.find_element_by_xpath('//html/body/div/div/div[2]/div/div[2]/textarea')

                fankui.send_keys('test')

                driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[3]/label/span[1]/span').click()

                time.sleep(3)

                driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[4]/span/a').click()

                if True:


                    print('[*] message print right :status:ok')

                    time.sleep(5)

                    driver.close()

                    driver.quit()

                    print('[*] quit status:ok')

                else:

                    print('[!] status error.')

            else:

                print('[!] login error:0')


    except:

        pass


def GetNowTime():

    while True:

        time.sleep(1)

        nowTime = time.strftime("%H:%M:%S", time.localtime(time.time()))  # 获取当前系统时间

        print(nowTime)

        if nowTime == '14:00:00':

            # main()

            print('time ok :1')

            break

if __name__ == '__main__':

    main(User='cxxxxxxx',Passwd='xxxxxxxx')

    # GetNowTime()
