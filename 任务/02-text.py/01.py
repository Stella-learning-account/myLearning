import csv


d = {}
d['3'] = 'adcs'
row = '1,战狼2,175.4万,1.05亿,36.6,吴京,吴京,余男,弗兰克·格里罗,张翰,卢靖姗,2017-07-27,100分钟,中国大陆,剧情,动作,战争'
d[row.split(',',1)[0]] = row.split(',',1)[1].replace(',', '，')  # 如果是英文逗号，不论值是否为一个完整的字符串，csv打印的值都将会被""所包含（如何解决这个问题？）
print(d)
with open('text.csv','w',encoding='utf-8',newline='') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(['名次','电影名称','总场次','人次','票价(元)','导演','主演','上映时间','片长','制作国家/地区','电影类型'])
        for i in d.items():
            csvwriter.writerow(i)