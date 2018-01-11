import urllib
import urllib2
import re
import thread
import time
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
url = 'http://www.szrc.cn/HrMarket/WLZP/ZP/0/%E4%BC%9A%E8%AE%A1'
headers = {'User-Agent':user_agent}
result= urllib2.Request( url,headers = headers )
response = urllib2.urlopen( result )
pageCode = response.read().decode( 'utf-8' )
pattern = re.compile(r'<a class="pub" href="/HrMarket/Common/PositionInfo/.*?>(.*?)</a>.*?<td class=".*?">(.*?)</td>.*?<td class=".*?">(.*?)</td>.*?<td class=".*?">(.*?)</td>',re.S)
items = re.findall( pattern,pageCode )
for i in items:
    input = raw_input()
    for g in i:
        print g
