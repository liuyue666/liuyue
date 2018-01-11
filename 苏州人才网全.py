import urllib
import urllib2
import re
url = 'http://www.szrc.cn/HrMarket/WLZP/ZP/0/%E4%BC%9A%E8%AE%A1'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
request= urllib2.Request(url,headers = headers)
response = urllib2.urlopen(request)
html = response.read().decode( 'utf-8' )
content_pattern = re.compile(r'class="td_positionName">.*?<a class="pub" href="/HrMarket/Common/PositionInfo/.*?>(.*?)</a>.*?<td class=".*?">(.*?)</td>.*?<td class=".*?">(.*?)</td>.*?<td class=".*?">(.*?)</td>',re.S)
content_items = re.findall(content_pattern,html)
for item in content_items:
    print item[0],item[1],item[2],item[3]

