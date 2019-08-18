## 网段端口快速扫描 ##
- [x] 支持IP段扫描
- [x] 支持获取banner

要安装的第三方模块：
```
multiprocessing
gevent
IPy
```

使用方法：
配置config.py执行port_scan.py即可
```python
'''
用于配置端口扫描
'''

PORT_FAN=[1,1000] #扫描端口的范围，第一个是开始端口号，第二是结束端口号
IP='39.96.0/24' #要扫描的IP范围，不懂请搜子网掩码划分IP

```

扫描结果：
```python
[+] host:39.96.0.211 port:22 status:open
banner:SSH-2.0-OpenSSH_7.2p2 Ubuntu-4ubuntu2.4

[+] host:39.96.0.217 port:21 status:open
[+] host:39.96.0.217 port:22 status:open
[+] host:39.96.0.218 port:22 status:open
banner:220 Welcome to blah FTP service.

banner:SSH-2.0-OpenSSH_7.4

banner:SSH-2.0-OpenSSH_7.4

[+] host:39.96.0.226 port:80 status:open
[+] host:39.96.0.227 port:80 status:open
[+] host:39.96.0.238 port:443 status:open

```