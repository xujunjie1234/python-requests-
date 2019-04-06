import pandas as pd 
import matplotlib.pyplot as plt
import squarify

df = pd.read_csv('C:\\Python\\Python37\\python_pachong\\songlist.csv')
tags = df['标签'].dropna()
tags = '/'.join(tags).split('/')
tag = list(set(tags))

count = [tags.count(i) for i in tag]
data = {'tag':tag,'count':count}
df = pd.DataFrame(data)
df1=df.sort_values(by='count',ascending=False)

tags = df1['tag'][:10]
counts = df1['count'][:10]

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
# colors = ['steelblue','#9999ff','red','indianred','deepskyblue','lime','magenta','violet','peru',  'green','yellow','orange','tomato','lawngreen','cyan','darkcyan','dodgerblue','teal','tan','royalblue']
colors = ['#993333', '#CC9966',  '#333333', '#663366', '#003366', '#009966', '#FF6600', '#FF0033', '#009999', '#333366']
plot = squarify.plot(sizes = counts, # 指定绘图数据
                     label = tags, # 指定标签
                     color = colors, # 指定自定义颜色
                     alpha = 1, # 指定透明度
                     value = counts, # 添加数值标签
                     edgecolor = 'white', # 设置边界框为白色
                     linewidth =1.5 # 设置边框宽度为3
                    )
# 设置标签大小为10
plt.rc('font', size=8)
# 设置标题大小
plot.set_title('网易云音乐歌单标签TOP10',fontdict = {'fontsize':13})
# 除坐标轴
plt.axis('off')
# 除上边框和右边框刻度
plt.tick_params(top = 'off', right = 'off')
# 图形展示
plt.show()
