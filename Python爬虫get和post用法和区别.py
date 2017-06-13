POST和GET数据传送

数据传送分为POST和GET两种方式，两种方式有什么区别呢？
最重要的区别是GET方式是直接以链接形式访问，链接中包含了所有的参数，当然如果包含了密码的话是一种不安全的选择，
不过你可以直观地看到自己提交了什么内容。POST则不会在网址上显示所有的参数，不过如果你想直接查看提交了什么就不太方便了，
大家可以酌情选择。


POST方式：
上面我们说了data参数是干嘛的？对了，它就是用在这里的，我们传送的数据就是这个参数data，下面演示一下POST方式。
import urllib.request
import urllib.parse


values = {}
values['username'] = "username"
values['password'] = "password"
data = urllib.parse.urlencode(values).encode(encoding='UTF8')  #需要加上编码格式，否则是str形式，而data不能是str模式
print(type(data)) 
url = "http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib.request.Request(url,data)
response = urllib.request.urlopen(request)
print (response.read().decode('utf-8'))  #编码后可以打印出正常格式的文本


GET方式：
至于GET方式我们可以直接把参数写到网址上面，直接构建一个带参数的URL出来即可。


import urllib.request
import urllib.parse

values={}
values['username'] = "username"
values['password']="password"
data = urllib.parse.urlencode(values)  #这个get方式的不需要编码，因为需要跟字符串形式的url相加
url = "http://passport.csdn.net/account/login"
geturl = url + "?"+data
print(geturl)
request = urllib.request.Request(geturl)
response = urllib.request.urlopen(request)
print (response.read().decode('utf-8'))

你可以print geturl，打印输出一下url，发现其实就是原来的url加？然后加编码后的参数
http://passport.csdn.net/account/login?username=1016903103%40qq.com&password=XXXX

和我们平常GET访问方式一模一样，这样就实现了数据的GET方式传送。