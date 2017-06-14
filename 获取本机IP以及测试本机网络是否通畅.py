#获取本机ip地址
import socket

hostname=socket.gethostname
local_ip=socket.gethostbyname(socket.gethostname())
ip_lists=socket.gethostbyname_ex(socket.gethostname())

print(hostname)
print(local_ip)
print(ip_lists)

# 判断当前是否可以联网
import os
import subprocess

def canConnect():
    fnull = open(os.devnull, 'w')
    result = subprocess.call('ping www.baidu.com', shell = True, stdout = fnull, stderr = fnull)
    fnull.close()
    if result:
        print("False")
    else:
        print("True")

canConnect()