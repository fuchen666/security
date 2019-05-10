#coding=utf-8

import datetime
import xlrd
import re
import sys
from pymongo import MongoClient
import json


sys.path.append(sys.path[0]+'/xunfeng/vulscan/vuldb')  # 将vuldb 加入到系统路径中

PASSWORD_DIC = []
TIMEOUT = 10               

conn = MongoClient('127.0.0.1', 65521)          # 链接巡风数据库
coll = conn['xunfeng']
coll.authenticate('scandb', 'emissuck')
members = coll.get_collection('Plugin')     # 获取巡风 Plugin 文件集
PASSWD = coll.get_collection('Config')


def get_config():
    config_info = PASSWD.find_one({"type": "vulscan"})
    pass_row = config_info['config']['Password_dic']
    password_dic = pass_row['value'].split('\n')
    return password_dic

if __name__ == '__main__':

    data = xlrd.open_workbook('/root/2018-01-03.xls')  # 提取xls文件
    table = data.sheets()[0]            
    nrows = table.nrows              # 行
    ncols = table.ncols              # 列

    for i in range(nrows):
        if i == 0:                  # 跳过第一行
            continue
        ip = table.row_values(i)[0]
        port = table.row_values(i)[1]
        plugin = table.row_values(i)[5]  # xls文件插件名称
        ps = table.row_values(i)[4]      # xls文件插件描述
#       print ip,port,plugin,ps
        if i >= 1:                         # 第二行开始

                for member in members.find():    # 循环遍历巡风 Plugin 文件

                        a = member['name']

#                       print a      # 输出巡风插件的文件名

#                       if a == plugin:  # 判断巡风插件名称是否等于xls里的插件名称

                        if a == plugin:

                             plugin = __import__  (member['filename'])  # _import_ 动态栽入否则找不到脚本       

                             if '.json' not in member['filename']:  # 标示符检测模式

                                 plugin_filename = member['filename']  # 赋值
                                 PASSWORD_DIC = get_config()              # 赋值
                                 setattr(plugin, "PASSWORD_DIC", PASSWORD_DIC) # 给插件声明密码字典
                                 plugin_info = plugin.check(str(ip),int(port),TIMEOUT) # 检查 ip ,端口，时间

                                 print ip,':',int(port),':',plugin_info     # 输 出

                             else:

                                  print ' '




