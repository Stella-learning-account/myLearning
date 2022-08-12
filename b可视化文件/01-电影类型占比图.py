import csv
import matplotlib.pyplot as plt
import pandas as pd


with open('movieRank_dictionary2.csv','r',encoding='utf-8') as f:
    csvreader = csv.reader(f)
    type,lst = [], []
    for row in csvreader:
        type = row
    # print(type)
    for i in type:
        if i not in lst:
            if i != '':
                lst.append(i)
    print(lst)
    d, data = {}, {}
    for i in type:
        for j in lst:
            if i == j:
                d.setdefault(i,[]).append(j)
    print(d)
    for i in lst:
        for a,b in d.items():
            if i==a:
                data[i]=len(b)

    data['剧情']=160+576
    data['动作']=180+1296
    data['动画']=47+49
    data['惊悚']=36+9
    data['喜剧']=136+169
    data['纪录片']=9
    data['冒险']=119+4
    data['爱情']=77+1
    print(data)
    print(len(data.keys()))

    data = dict(sorted(data.items(),key = lambda x:x[1],reverse = True))

    # 创建figure，axes，并用axes画图
    fig,ax1 = plt.subplots()
    x_data, y_data, y2_data= [], [], []
    [x_data.append(i) for i,j in data.items()]
    [y_data.append(j) for i,j in data.items()]
    [y2_data.append(round(j/sum(y_data)*100,2)) for i,j in data.items()]
    print(y2_data)
    print(x_data)
    print(y_data)
    df2 = pd.DataFrame({'contry': x_data,
                    'pice': y2_data})

    # 中文和正负号设置
    plt.rcParams["font.sans-serif"] = ["SimHei"]  # 指定默认字体（解决中文无法显示的问题）
    plt.rcParams["axes.unicode_minus"] = False  # 解决保存图像时负号“-”显示方块的问题

    ax1.bar(x=x_data, height=y_data,label='电影数目')
    for x, y in zip(x_data, y_data):
        plt.text(x , y + 0.05, '%.f' % y, ha='center', va='bottom')

    ax2 = ax1.twinx()
    ax2.plot(df2.contry, df2.pice,label='电影占比(%)', color='#EE4000',marker='o', linewidth=1)
    for x2, y2 in zip(x_data, y2_data):
        plt.text(x2 , y2 + 1, f'{y2}%', ha='center', va='bottom', color='r', rotation=0)

    # 图例1
    fig.legend(loc=1,bbox_to_anchor=(1,1),bbox_transform=ax1.transAxes)

    # 图例2
    # ins = [p1,p1]
    # labels = [l.get_label() for l in ins]
    # plt.legend(ins,labels)  # 为什么会出现‘ValueError: too many values to unpack (expected 1)’的情况？

    plt.title("各国电影比例图")
    plt.xlabel("国家")
    ax1.set_ylabel('数目')   #设置Y1轴标题
    ax2.set_ylabel('占比(%)')   #设置Y2轴标题

plt.show()