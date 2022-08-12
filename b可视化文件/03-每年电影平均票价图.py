import csv 
import matplotlib.pyplot as plt
import numpy as np

with open('movieRank_dictionary.csv','r',encoding='utf-8') as f:
    csvreader = csv.reader(f)
    d = {}
    for row in csvreader:
        if len(row)>2:
            continue
        else:
            if len(row[1].split('|'))<7:
                continue
            else:
                d.setdefault(row[1].split('|')[6].split('-')[0], []).append(row[1].split('|')[3])
    need_del,int_num = [], []
    [need_del.append(i) for i in d.keys() if len(i)!=4]
    for i in need_del:
        del d[i]
    for i in list(d.keys()):
        if i[-2:]=='分钟':
            del d[i]
    data = {}
    for i,j in d.items():
        j = list(map(float,j))
        for single_price in j:
            if single_price>100:
                j.remove(single_price)
        data[i]=round(sum(j)/len(j),1)
        # print(i,round(sum(j)/len(j),1))
    sorted_data = dict(sorted(data.items(),key=lambda d:d[0]))


 
    plt.rcParams["font.sans-serif"]=['SimHei']
    plt.rcParams["axes.unicode_minus"]=False
    
    plt.bar(list(sorted_data.keys()), list(sorted_data.values()), label='均价', width=0.6)
    for x,y in sorted_data.items():
        plt.text(x , y , f'{y}元', ha='center', va='bottom', rotation=0, fontsize=14)
    plt.legend(fontsize=14)
    
    plt.yticks(np.linspace(0,60,6,endpoint=True), fontsize=14)
    plt.xticks(fontsize=14)
    plt.title('每年电影平均票价图', fontsize=14)
    plt.xlabel('年份', fontsize=14)
    plt.ylabel('价格（元）', fontsize=14)

    plt.show()