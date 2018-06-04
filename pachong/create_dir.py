__author__ = 'Administrator'
#coding=utf-8
import os
import urllib2
import urllib
import urlparse
"""
h=raw_input('请输入:') #可以输入字符串和数字
path=str(h)
if not os.path.exists(path):
    #os.makedirs()可以建立递归建立深级目录
    os.makedirs(path)
else:
    print('已经创建')

"""
url='https://www.doggod.cn/img/head-logo.jpg'
#获取图片中间路径
dirname=url[0:url.rfind('/', 1) + 1].replace('https://www.doggod.cn','')
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
    urllib.urlretrieve(url,filename)
    print('下载完成')
else:
    print('下载过了')