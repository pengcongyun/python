__author__ = 'Administrator'
#coding=utf-8
import urllib2
import os
import urllib
import time
#下载读取网页
def downloadHtml(url):
    return urllib2.urlopen(url).read() #读取全部网页

#下载图片 href
def downloadImg(href,url):
    #获取图片中间路径
    dirname=url[0:url.rfind('/', 1) + 1].replace(href,'')
    #图片存放地址
    img_dir='D:\python\www\pachong'+dirname
    #创建目录
    if not os.path.exists(img_dir):
        #os.makedirs()可以建立递归建立深级目录
        os.makedirs(img_dir)
    #获取图片后缀
    name=os.path.splitext(url)[0].split('/')[-1:]
    exif=os.path.splitext(url)[1]
    filename= '{}{}{}{}'.format(img_dir,os.sep,name[0],exif) #拼接图片地址  os.sep让路径在：linux系统 /  windows系统 \
    #下载图片，并保存到文件夹中
    if not os.path.exists(filename):
        #爬取页面过快造成暂时被网站ban掉的情况，设置time间隔请求
        time.sleep(1)
        urllib.urlretrieve(url,filename)
        print('下载完成')
    else:
        print('下载过了')