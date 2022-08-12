import csv
import matplotlib.pyplot as plt


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
                        d.setdefault(row[1].split('|')[6].split('-')[0], []).append(row[1].split('|')[8])
    data = dict(sorted(d.items(),key=lambda d:d[0]))
    need_del= []
    [need_del.append(i) for i in data.keys() if len(i)!=4]
    for i in need_del:
        del data[i]
    for i in list(data.keys()):
        if i[-2:]=='分钟':
            del data[i]
    
    new_data={}
    for i,j in data.items():
        c_data = {}
        for item in j:
            c_data.update({item: j.count(item)})
        new_data.setdefault(i,[]).append(c_data)
    # print(new_data)


    x_data = list(data.keys())
    y_all_data = []
    y_data1,y_data2,y_data3 = [], [], []
    for j in new_data.values():
        print(j[0],'____',len(j[0]))
        if len(j[0])>2:
            c_list=[]
            for i in j[0].keys():
                for b in ['印度', '中国香港', '中国台湾', '英国', '法国', '日本', '西班牙', '俄罗斯']:
                    if i==b:
                        c_list.append(j[0][b])
            y_all_data.append([j[0]['中国大陆'], j[0]['美国'],sum(c_list)])
        elif len(j[0])==2:
            y_all_data.append(list(j[0].values())+[0])
        else:
            y_all_data.append(list(j[0].values())+[0,0])
    print(y_all_data)
    for i in y_all_data:
        y_data1.append(i[0])
        y_data2.append(i[1])
        y_data3.append(i[2])
    print(y_data1)
    print(y_data2)
    print(y_data3)
    print(x_data)

    plt.figure()
    plt.rcParams["font.sans-serif"]=['SimHei']
    plt.rcParams["axes.unicode_minus"]=False

    x = range(len(x_data))

    plt.bar([i-0.3 for i in x],y_data1, width=0.3,label='中国大陆', color='r')
    plt.bar(x_data,y_data2, width=0.3,label='美国', color='#008792')
    plt.bar([i+0.3 for i in x],y_data3, width=0.3,label='其他国家', color='#7fb80e')
    for a,b in zip(x,y_data1):
        plt.text(a-0.3 , b, f'{b}', ha='center', va='bottom', fontsize=14)
    for a,b in zip(x,y_data2):
        plt.text(a , b, f'{b}', ha='center', va='bottom', fontsize=14)
    for a,b in zip(x,y_data3):
        plt.text(a+0.3 , b, f'{b}', ha='center', va='bottom', fontsize=14)

    plt.legend(loc='upper left',fontsize=14)
    
    plt.xticks(x_data, x_data, fontsize=14)
    plt.yticks(fontsize=14)
    plt.title('每年各国电影数量图', fontsize=14)
    plt.xlabel('年份', fontsize=14)
    plt.ylabel('电影数目（部）', fontsize=14)

    plt.show()
