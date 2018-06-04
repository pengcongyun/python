__author__ = 'Administrator'
#coding=utf-8
import re
mystr="""<li>
<span>16519</span>
<span>16513</span>
<b>委托客户</b>
</li>"""
#不带括号，是匹配所有的东西
#restr="<span>\\d+</span>"
#带括号，是匹配返回括号里面的东西
restr="<span>(\\d+)</span>"
regex=re.compile(restr,re.IGNORECASE)
mylist=regex.findall(mystr)
print mylist
print mylist[0]+'||'+mylist[1]