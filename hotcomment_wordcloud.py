import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
import pandas as pd
import random
import pymysql  #导入 pymysql

def random_color_func(word=None, font_size=None, position=None,  orientation=None, font_path=None, random_state=None):
    h  = random.randint(120,250)
    s = int(100.0 * 255.0 / 255.0)
    l = int(100.0 * float(random.randint(60, 120)) / 255.0)
    return "hsl({}, {}%, {}%)".format(h, s, l)


#打开数据库连接
db= pymysql.connect(host="localhost",user="root",
     password="123456",db="t2",port=3306)

# 使用cursor()方法获取操作游标
cur = db.cursor()
sql = 'select content from songs'
cur.execute(sql)
res = cur.fetchall()
df = pd.DataFrame(list(res),columns=[x[0] for x in cur.description])

text1 = ''.join(df['content'])
text2 = jieba.lcut(text1,cut_all=False)
text = ' '.join(text2)

words = pd.read_csv('C:\\Python\\chineseStopWords.txt', encoding='utf-8', sep='\t', names=['stopword'])
stopwords=set(' ')

stopwords.update(words['stopword'])

bk_pic = plt.imread('C:\\Python\\timg.jpg')

wc = WordCloud(background_color='white',
               # width=800,height=1200,
                scale=2,
                colormap='Blues',
                max_font_size=300,
                min_font_size=5,
                stopwords=stopwords,
                max_words=200000,
                font_path='c:\\windows\\Fonts\\simhei.ttf',
                mask=bk_pic,
                random_state=50,
                prefer_horizontal=1,
                collocations=False,  #去除重复词
                color_func=random_color_func)
wc.generate(text)
plt.imshow(wc,interpolation='bilinear')     #interpolation='bilinear'对生成的图像进行插值，保证生成图像的平滑
# plt.tight_layout()
plt.axis('off')
plt.show()
wc.to_file('网易云歌曲热评词云图.jpg')
