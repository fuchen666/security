#!coding=utf-8

import string

s = ["s", "y", "s", "t", "e", "m"]  # 定义一个序列

s = "".join(s)  # 将序列中的元素连接

# print(s)

cmd = "cat /etc/passwd"

code = "__import__('os')." + s + "('" + cmd + "')"    # 动态加载 # "os.system(cmd)"

eval(code)  # 函数用来执行一个字符串表达式，并返回表达式的值。

print('running ok！')