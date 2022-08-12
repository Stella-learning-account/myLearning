import csv
import matplotlib.pyplot as plt
from pylab import xticks,yticks,np


with open('movieRank_dictionary.csv','r',encoding='utf-8') as f:
    csvreader = csv.reader(f)
    d={}
    for row in csvreader:
        if len(row)>2:
            continue
        else:
            if len(row[1].split('|'))<7:
                continue
            else:
                d.setdefault(row[1].split('|')[6].split('-')[0], []).append([row[1].split('|')[1].split('万')[0], row[1].split('|')[2].split('万')[0]])
    data = dict(sorted(d.items(),key=lambda d:d[0]))
    need_del= []
    [need_del.append(i) for i in data.keys() if len(i)!=4]
    for i in need_del:
        del data[i]
    for i in list(data.keys()):
        if i[-2:]=='分钟':
            del data[i]
    film, viewer=[], []
    year_film, year_viewer=[], []
    for i,j in data.items():
        for a in j:
            film.append(float(a[0]))
            if a[1][-1:]=='亿':
                viewer.append(float(a[1].split('亿')[0])*10000)
            else:
                viewer.append(float(a[1]))
        year_film.append(round(sum(film),2))
        film.clear()
        year_viewer.append(round(sum(viewer),2))
        viewer.clear()
    print(year_film)
    print(year_viewer)
    x_data = list(data.keys())
    print(x_data)

    plt.figure()
    plt.rcParams["font.sans-serif"]=['SimHei']
    plt.rcParams["axes.unicode_minus"]=False


    x = range(len(x_data))

    x1=plt.bar([i-0.15 for i in x],year_film, width=0.3,label='总场次', color='r')
    x2=plt.bar([i+0.15 for i in x],year_viewer, width=0.3,label='总人次', color='#008792')
    for a,b in zip(x,year_film):
        plt.text(a-0.15 , b, f'{b}', ha='center', va='bottom', fontsize=10)
    for a,b in zip(x,year_viewer):
        plt.text(a+0.15 , b, f'{b}', ha='center', va='bottom', fontsize=10)

    plt.legend(loc='upper left',fontsize=14)
    
    plt.xticks(range(0,9), x_data, fontsize=14)
    plt.yticks(fontsize=14)
    plt.title('每年总人次、总场次变化图', fontsize=14)
    plt.xlabel('年份', fontsize=14)
    plt.ylabel('次数（万）', fontsize=14)

    plt.show()
