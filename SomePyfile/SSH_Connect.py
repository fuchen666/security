# coding = utf-8

import paramiko
import time

# 创建 ssh 连接
sshc = paramiko.SSHClient()

# 第一次连接提示是否继续远程连接，默认选择YES
sshc.set_missing_host_key_policy(paramiko.AutoAddPolicy)

ip = "149.129.94."
# ip = "192.168.1.1"


try:


    for i in range(160, 225):

        host = ip + str(i)

        print(host)

        try:

            con = sshc.connect(host,22,'root','*********',timeout=3)

            username = sshc.exec_command("whoami")[1].readlines()

            time.sleep(1)

            print("\33[1m[+] HOST: {} 连接成功\33[1m".format(host))

        except Exception as e:

            # print("[-] SSH 连接失败，请检查端口用户名密码是否正确")
            print("[-] HOST: {} 连接错误".format(host))

            continue

except:

    print("[-] Time out")