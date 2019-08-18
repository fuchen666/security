#!-*-encoding:utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select


def alert():
	
	''' 
	Xpath 定位更准确 

	使用chrome浏览器需下载chromedriver（同一目录）

	'''
    try:

        driver = webdriver.Chrome()  # 调用chrome浏览器
        driver.implicityly_wait(30)  # 使用30秒隐式等待时间来定义Selenium执行步骤的超时时间
        driver.get('https://wj.qq.com/s/1***/url')
        time.sleep(1)

        # 模拟键盘回车键
        driver.find_element_by_xpath('/html/body/div[7]/div/table/tbody/tr[3]/td/div[2]/button').send_keys(Keys.ENTER)  
	# send_keys()  发送方法

        department = Select(driver.find_element_by_class_name("survey_form_input"))
        department.select_by_visible_text("XX部门")
        time.sleep(1)

        rname = driver.find_element_by_xpath("//*[@id=\"text_q-2-MQwR\"]")
        # rname.clear()   # 清除指定框中的信息
        rname.send_keys(u"姓名")
        time.sleep(1)

        phone = driver.find_element_by_xpath("//*[@id=\"text_q-3-EVyX\"]")
        phone.send_keys("13888888***")

        driver.find_element_by_xpath('//*[@id="question_q-4-rMPg"]/div/div[3]/div[2]/label/div[1]/p').click() # 点击事件
        time.sleep(1)

        # driver.find_element_by_xpath("//*[@id=\"container\"]/div[2]/div/div/div/div[5]/div/a[2]").send_keys(Keys.ENTER) #回车提交键
        time.sleep(3)	
	driver.close()
	driver.quit()
	
    except Exception as e:
        print str(e)
        driver.close()
        driver.quit()


def GetNowTime():
    
    while True:
        time.sleep(1)

        nowtime = time.strftime("%H:%M:%S", time.localtime(time.time()))  # 获取当前系统时间
        print nowtime
        
        if nowtime == '14:00:00' #
            alert()
            break        

# alert()
GetNowTime()


