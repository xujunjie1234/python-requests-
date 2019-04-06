import requests
import json
from lxml import etree
from fake_useragent import UserAgent
import random
import pandas as pd
import pymysql
import datetime,time
#-----------------设置请求头------------------------------------------
ua = UserAgent()
headers = {'Host': 'music.163.com','User-Agent':ua.random}

#------------创建Mysql数据库连接---------------------------------
db= pymysql.connect(host="localhost",user="root",
    password="123456",db="t2",port=3306)
cur = db.cursor()
sql_create = '''create table if not exists songss(id int primary key auto_increment,
                                    nickname varchar(30),
                                    date varchar(20),
                                    likecount int(10),
                                    content varchar(500) ,
                                    song varchar(150),
                                    comment_count int(10)
                                    )'''
cur.execute(sql_create)
db.commit()

#---------------------获取热门评论---------------------------------
def get_hotcomment(headers=headers):      

    df = pd.read_csv('song.csv')
    data1 = df.drop_duplicates(['id']).reset_index()[:10]

    songs = data1['song']
    urls = ['https://music.163.com/api/v1/resource/comments/R_SO_4_{}?csrf_token='.format(i) for i in data1['id']]
    
    n=0
    for song,url in zip(songs,urls):
        res = requests.get(url,headers=headers)
        js = json.loads(res.text)
        comment_count = js['total']
        hotcomments = js['hotComments']
        for info in hotcomments:
            nickname = info['user']['nickname']
        
            timestamp = info['time']
            utc_time = datetime.datetime.utcfromtimestamp(timestamp//1000)
            date = utc_time + datetime.timedelta(hours=8)
             
            content = info['content']
            likecount = info['likedCount']

            data=[nickname,date,likecount,content,song,comment_count]

            to_mysql(data)
        # time.sleep(1)
        n+=1
        print('第',str(n),'条储存完成，已完成：','%.2f%%' %(100*n/65340))
    db.close()
    print('爬取完成，数据库已关闭')
#--------------------插入数据------------------------------
def to_mysql(data):
    command = 'insert into songss(nickname,date,likecount,content,song,comment_count) values(%s,%s,%s,%s,%s,%s)'
    cur.execute(command,data)
    db.commit()
    
#-----------开始运行---------------------------------------
if __name__ =='__main__':

    get_hotcomment()
    

    
    
