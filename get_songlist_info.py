import requests
from lxml import etree
import json
import re
import pymongo
import random
from fake_useragent import UserAgent
from collections import defaultdict
import datetime
import pandas as pd

def get_song_lists(url,headers):
    res = requests.get(url,headers=headers)
    html = etree.HTML(res.text)
    ids = html.xpath('//*[@id="m-pl-container"]//li/p[1]/a/@href')
    urls = ['https://music.163.com'+i for i in ids]

    for url in urls:
        res = requests.get(url,headers=headers)
        html = etree.HTML(res.text)

        title = html.xpath('//div[@class="tit"]/h2/text()')[0]
        author=html.xpath('//span[@class="name"]/a/text()')[0]
        user_id = html.xpath('//span[@class="name"]/a/@href')[0]
        date = html.xpath('//span[@class="time s-fc4"]/text()')[0][:-3]
        description= "".join(html.xpath('//*[@id="album-desc-more"]/text()'))
        
        collection = html.xpath('//*[@id="content-operation"]/a[3]/i/text()')[0][1:-1]
        tag = "/".join(html.xpath('//a[@class="u-tag"]/i/text()'))
        
        play = html.xpath('//*[@id="play-count"]/text()')[0]
        share = html.xpath('//*[@id="content-operation"]/a[4]/i/text()')[0][1:-1]
        comments_count = html.xpath('//*[@id="cnt_comment_count"]/text()')[0]

        data['歌单标题'].append(title)
        data['作者'].append(author)
        data['作者id'].append(user_id)
        data['日期'].append(date)
        data['收藏量'].append(collection)
        data['标签'].append(tag)
        data['播放量'].append(play)
        data['转发量'].append(share)
        data['评论数'].append(comments_count)
        data['介绍'].append(description)

        songs = html.xpath('//ul[@class="f-hide"]/li/a/text()')
        raw_ids = "".join(html.xpath('//ul[@class="f-hide"]/li/a/@href'))
        ids = re.findall('\d+',raw_ids)
            
        for song,id in zip(songs,ids):
            data1['song'].append(song)
            data1['id'].append(id)
    
if __name__ == '__main__':
    data = defaultdict(list)
    data1 = defaultdict(list)
    ua = UserAgent()
    headers = {'User-Agent':ua.random}
    
    urls = ['https://music.163.com/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset={}'.format(str(35*i)) for i in range(38)]
    for url in urls:
        get_song_lists(url,headers)
    df = pd.DataFrame(data)
    df1 = pd.DataFrame(data1)
    df.to_csv('wanyiyun.csv',encoding='utf-8-sig',index=False)
    df1.to_csv('song1.csv',encoding='utf-8-sig',index=False)
    print(df1.tail())
    


