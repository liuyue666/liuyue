Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import urllib2
>>> httpHandler = urllib2.HTTPHandler(debuglevel=1)
>>> httpsHandler = urllib2.HTTPHabdler(debuglevel=1)

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    httpsHandler = urllib2.HTTPHabdler(debuglevel=1)
AttributeError: 'module' object has no attribute 'HTTPHabdler'
>>> httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
>>> opener = urllib2.build_opener(httpHandler, httpsHandler)
>>> urllib2.install_opener(opener)
>>> response = urllib2.urlopen('http://www.baidu.com')
send: 'GET / HTTP/1.1\r\nAccept-Encoding: identity\r\nHost: www.baidu.com\r\nConnection: close\r\nUser-Agent: Python-urllib/2.7\r\n\r\n'
reply: 'HTTP/1.1 200 OK\r\n'
header: Date: Thu, 16 Nov 2017 06:14:48 GMT
header: Content-Type: text/html; charset=utf-8
header: Transfer-Encoding: chunked
header: Connection: Close
header: Vary: Accept-Encoding
header: Set-Cookie: BAIDUID=51BACE56A8BD6705D830831F46580FEE:FG=1; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
header: Set-Cookie: BIDUPSID=51BACE56A8BD6705D830831F46580FEE; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
header: Set-Cookie: PSTM=1510812888; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
header: Set-Cookie: BDSVRTM=0; path=/
header: Set-Cookie: BD_HOME=0; path=/
header: Set-Cookie: H_PS_PSSID=24792_1439_21099_24879_20928; path=/; domain=.baidu.com
header: P3P: CP=" OTI DSP COR IVA OUR IND COM "
header: Cache-Control: private
header: Cxy_all: baidu+4c51507b4de0344dd906c2cd96c1591f
header: Expires: Thu, 16 Nov 2017 06:14:45 GMT
header: X-Powered-By: HPHP
header: Server: BWS/1.1
header: X-UA-Compatible: IE=Edge,chrome=1
header: BDPAGETYPE: 1
header: BDQID: 0xc4af76a0000459e7
header: BDUSERID: 0
>>> 
