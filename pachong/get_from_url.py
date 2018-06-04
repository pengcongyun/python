__author__ = 'Administrator'
#coding=utf-8
import urllib2
#下载读取网页
def download(url):
    return urllib2.urlopen(url).read() #读取全部网页
#保存数据到某个文件中，文件可以不建立
def saveFile(data):
    save_path = 'D:\python\www\pachong/reptile.html'
    f_obj = open(save_path, 'wb') # wb 表示打开方式,也可用w
    f_obj.write(data)
    f_obj.close()
url="http://www.doggod.cn" #urlopen只能处理http，不可以处理https
html=download(url)
saveFile(html)
