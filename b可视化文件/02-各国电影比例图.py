import csv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager as fm


with open('movieRank_dictionary2.csv','r',encoding='utf-8') as f:
    csvreader = csv.reader(f)
    place,lst = [], []
    i = 0
    for row in csvreader:
        i += 1
        if i == 10:
            place = row
            for j in place:
                if j == '':
                    continue
                else:
                    lst.append(j)
    d, data = {}, {}
    for i in place:
        for j in lst:
            if i == j:
                d.setdefault(i,[]).append(j)
    for i in lst:
        for a,b in d.items():
            if i==a:
                data[i]=len(b)
    # print(data)
    for i in ['动作', '动画', '惊悚', '剧情', '喜剧', '纪录片', '冒险', '爱情']:
        del data[i]
    print(data)

    data_list,other = [],[]
    name,other_name = ['其他国家'],[]
    for i,j in data.items():
        f = j/sum(data.values())*100
        print(round(f,3))
        if f <= 1:
            other_name.append(i)
            other.append(round(f,3))
        else:
            name.append(i)
            data_list.append(round(f,3))
    print(name,len(name))
    print(data_list,other,sum(other))
    print(other_name,len(other_name))


    fig, ax = plt.subplots()

    y = np.array([sum(other)]+data_list)
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei'] #指定字体为雅黑，解决文字乱码问题
    patches, texts,type_make = ax.pie(y,
            labels=name,  # 设置饼图标签
            autopct="%1.1f%%", #饼块内标签。
            colors=('black','Crimson','DeepSkyBlue'),
            explode=[0,0,0.1], 
            radius=1,
            pctdistance=0.5,
            )
    plt.title("电影类型占比")
    plt.legend()

    # 重新设置字体大小
    proptease = fm.FontProperties()
    proptease.set_size('large')
    # font size include: 'xx-small', x-small, 'small', 'medium', 'large', 'x-large', xx-large or number, e.g. '12'
    plt.setp(type_make, fontproperties=proptease)
    plt.setp(texts, fontproperties=proptease)


    plt.show()