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
                if row[1].split('|')[8] in ['印度', '中国香港', '中国台湾', '英国', '法国', '日本', '西班牙', '俄罗斯', '中国大陆', '美国']:
                        d.setdefault(row[1].split('|')[8], []).append(row[1].split('|')[3])
    eval_data = []
    for i in list(d.values()):
        for j in list(map(float,i)):
            if j>100:
                i.remove(f'{j}')
        eval_data.append(round(sum(list(map(float,i)))/len(i), 1))
    print(eval_data)


    plt.rcParams["font.sans-serif"]=['SimHei']
    plt.rcParams["axes.unicode_minus"]=False

    # plt.bar(list(d.keys()), eval_data,width=0.6, label='平均票价')
    for i in range(len(list(d.keys()))):
        plt.bar(list(d.keys())[i],eval_data[i],label=list(d.keys())[i],width=0.6)

    for x,y in zip(list(d.keys()), eval_data):
        plt.text(x,y,f'{y}元',ha='center', va='bottom', rotation=0, fontsize=12)
    plt.legend(fontsize=12)
    
    plt.yticks(np.linspace(0,60,6,endpoint=True), fontsize=12)
    plt.xticks(fontsize=12)
    plt.title('制作地区平均票价对比图', fontsize=18)
    plt.xlabel('国家', fontsize=12)
    plt.ylabel('价格（元）', fontsize=12)

    plt.show()