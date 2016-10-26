# -*- coding:utf-8 -*-


import re
import urllib2


reponse=urllib2.urlopen('http://time.tianqi.com/')
the_page=reponse.read()
#print(the_page)

m=r'(20\d{2}-\d+\d+.*\d+:\d+:\d+)'
m=re.compile(m)

mm=m.findall(the_page)

my_line='*'*50

print my_line,'\n',my_line
print u'北京时间：--> || ',mm[0],' ||'
print my_line,'\n',my_line


raw_input('Please enter any key to exit!')

