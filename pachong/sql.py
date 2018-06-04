__author__ = 'Administrator'
#coding=utf-8
import mysql.connector
# 打开数据库连接
conn=mysql.connector.connect(host='localhost',port=3306,user='root',passwd='root',db='test')
# 使用cursor()方法获取操作游标
cur=conn.cursor()
#插入数据
#cur.execute('insert into video(id,video) VALUES (9,22)')
#conn.commit()
#查询
#cur.execute('select * from video')
#data=cur.fetchall()
#print(data)
#cur.execute('select * from video where id=%s',('9',))
#row=cur.fetchall()
#print(row)
#删除
"""try:
    cur.execute('delete from video where id=%s',(3,))
    conn.commit()
except:
    conn.rollback()
"""
#删除id小于2的数据
#cur.execute('delete from video where id<%s',(3,))
cur.execute('delete from video where id<%s'%(3))
conn.commit()
#关闭数据库
conn.close()

