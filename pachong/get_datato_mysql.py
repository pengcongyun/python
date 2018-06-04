__author__ = 'Administrator'
#coding=utf-8
import re
import function #引用function里的方法
html=function.downloadHtml("http://www.doggod.cn")
#正则匹配获取所有的图片
img_rex='src="(.*?\.(jpg|png|gif))"'
rex=re.compile(img_rex,re.IGNORECASE)
data=rex.findall(html)
for i in range(len(data)):
    if  data[i][0][0]=='/':
        data[i]="https://www.doggod.cn"+data[i][0]
    else:
        data[i]=data[i][0]
    #请求图片地址下载图片
    function.downloadImg('https://www.doggod.cn',data[i])


