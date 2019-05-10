#! coding = utf-8


from socket import *
import threading
import time
# 导入进程包
import multiprocessing


# 导入队列包


# 创建ip线程
class Ip:
    def __init__(self, ip):
        # 继承多线程父类
        # 接收传入的ip地址
        self.ip = ip


    def runs(self):
        # 创建对象并且进行扫描
        p = PortScan(self.ip)
        threading.Thread(target=p.run).start()


class PortScan(threading.Thread):
    def __init__(self, host):
        # 继承多线程父类
        super().__init__()
        self.host = host
        # 需要扫描的端口
        self.port = [21, 22, 23, 25, 53, 67, 80, 110, 139, 161, 389, 443, 445, 1080, 1433, 3306, 5432, 6379, 27017,
                     5000, 3389, 4848, 7001, 2601, 3389, 8080, 5900, 11211, 2181]

    def run(self):
        try:
            for i in self.port:
                # 多线程调用port扫描方法，一个端口一个线程
                threading.Thread(target=self.ports, args=(i,)).start()
                # 每0.1秒传入一个参数，进行扫描
                time.sleep(0.1)
                print("执行中")
        except:
            print("error")

    def ports(self, port_):
        try:
            print("正在扫描ip为:%s--端口是%s" % (self.host, port_))
            server = socket(AF_INET, SOCK_STREAM)
            server.connect((self.host, port_))

            # 创建文件进行写入
            with open("save.txt", "r") as f:
                # 写入文件
                f.write("host:%s----port:%s")
        except:
            print("ip为:%s端口%s未开启" % (self.host, port_))
        # 关闭套接字
        server.close()

    def __del__(self):
        print("ip为%s扫描结束" % self.host)


if __name__ == '__main__':
    
    for x in range(1, 256):
        # 传入进程，优化代码
        ip = Ip("192.168.15." + str(x))
        multiprocessing.Process(target=ip.runs).start()
        # 一秒创建一个进程
        time.sleep(0.2)
        print("进程已开启")
