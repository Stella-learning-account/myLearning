import csv 
import matplotlib.pyplot as plt
import numpy as np


with open('movieRank_dictionary.csv','r',encoding='utf-8') as f:
    csvreader = csv.reader(f)
    d, data = {}, {}
    for row in csvreader:
        if len(row)>2:
            continue
        else:
            if len(row[1].split('|'))<7:
                continue
            elif len(row[1].split('|')[6].split('-')[0])!=4:
                continue
            elif row[1].split('|')[6].split('-')[0][-2:]=='分钟':
                continue
            else:
                d.setdefault(row[1].split('|')[6].split('-')[0], []).append(row[1].split('|')[6].split('-')[0])
    d = dict(sorted(d.items(),key=lambda d:d[0]))
    for i,j in d.items():
        data[i]=len(j)
    print(data)


    plt.rcParams["font.sans-serif"]=['SimHei']
    plt.rcParams["axes.unicode_minus"]=False


    for i in range(len(list(data.keys()))):
        plt.bar(list(data.keys())[i],list(data.values())[i],width=0.4)

    for x,y in zip(list(data.keys()), list(data.values())):
        plt.text(x,y,f'{y}部',ha='center', va='bottom', rotation=0, fontsize=12)
    
    plt.yticks(fontsize=12)
    plt.xticks(fontsize=12)
    plt.title('每年电影数目图', fontsize=18)
    plt.xlabel('年份', fontsize=12)
    plt.ylabel('数目（部）', fontsize=12)

    plt.show()