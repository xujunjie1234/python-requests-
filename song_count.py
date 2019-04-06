import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\Python\\Python37\\python_pachong\\song.csv')
data = df['song'].value_counts().head(20)
song = data.index[::-1]
count = data.values[::-1]
X=list(range(1,21))

plt.figure(figsize=(10,6))

plt.barh(X,count,0.7,color='c',alpha=0.8)
plt.xlabel('次数')
plt.title('网易云音乐热门歌单推荐歌曲TOP20')
plt.yticks(X,song,rotation=0,size=10)
plt.xticks(size=10)

ax = plt.gca()
ax.spines['right'].set_color('c')
ax.spines['top'].set_color('c')
ax.spines['left'].set_color('c')
ax.spines['bottom'].set_color('c')

for x,y in zip(X,count):
    plt.text(y+1,x-0.2,y,size=10,color='c',alpha=0.8)

plt.rcParams['font.sans-serif'] = ['SimHei'] # 步骤一（替换sans-serif字体）SimHei
plt.rcParams['axes.unicode_minus'] = False  # 步骤二（解决坐标轴负数的负号显示问题
plt.show()
