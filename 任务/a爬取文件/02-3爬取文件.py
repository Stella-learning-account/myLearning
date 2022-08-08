from importlib.resources import contents
from multiprocessing import Pool
import requests
from lxml import etree
import csv 

def work(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77"
    }
    resp = requests.get(url,headers=header)
    resp.encoding = 'utf-8'
    html = etree.HTML(resp.text)
    data_list = []
    d = {}
    for i in range(1,51):
        content = html.xpath(f'//*[@id="content"]/div[2]/table/tbody/tr[{i}]/td//text()')
        d.setdefault('名次',[]).append(content[0])
        d.setdefault('电影名称',[]).append(content[1])
        d.setdefault('总场次',[]).append(content[2])
        d.setdefault('人次',[]).append(content[3])
        d.setdefault('票价(元)',[]).append(content[4])
        web = 'http://58921.com' + html.xpath(f'//*[@id="content"]/div[2]/table/tbody/tr[{i}]/td[2]/a/@href')[0]
        num = web.split('/')[-1]
        resp2 = requests.get(web,headers=header)
        resp2.encoding = 'utf-8'
        html2 = etree.HTML(resp2.text)
        direct = html2.xpath(f'//*[@id="content_view_{num}"]/div[2]/div/ul/li[2]/a/text()')
        act = [','.join(html2.xpath(f'//*[@id="content_view_{num}"]/div[2]/div/ul/li[3]/a//text()'))]
        time = html2.xpath(f'//*[@id="content_view_{num}"]/div[2]/div/ul/li[4]/text()')
        long = html2.xpath(f'//*[@id="content_view_{num}"]/div[2]/div/ul/li[5]/text()')
        place = html2.xpath(f'//*[@id="content_view_{num}"]/div[2]/div/ul/li[6]/a//text()')
        type = [','.join(html2.xpath(f'//*[@id="content_view_{num}"]/div[2]/div/ul/li[7]/a//text()'))]
        list = [direct, act, time, long, place, type]
        for i in list:
            if len(i)==0:
                i.append('空')
        d.setdefault('导演',[]).append(direct[0])
        d.setdefault('主演',[]).append(act[0])
        d.setdefault('上映时间',[]).append(time[0])
        d.setdefault('片长',[]).append(long[0])
        d.setdefault('制作国家/地区',[]).append(place[0])
        d.setdefault('电影类型',[]).append(type[0])
        # data_list.append(['/'.join(content+direct+act+time+long+place+type).replace(',', '，')])
    print('end: ' + url)
    resp.close()
    resp2.close()
    return d


if __name__ == "__main__":
    urls,multi_result = [],[]
    pool = Pool(10)
    for i in range(10):
        url = f'http://58921.com/alltime/wangpiao?page={i}&pagr=7'
        multi_result.append(pool.apply_async(func=work,args=(url, )))
    pool.close()
    pool.join()
    listw = []
    for _r in multi_result:
        listw.append(_r.get())
    print(_r.get())
    print(listw)
    d = {}
    for i in listw:
        for a,b in i.items():
            for j in ['名次','电影名称','总场次','人次','票价(元)','导演','主演','上映时间','片长','制作国家/地区','电影类型']:
                if a == j:
                    d.setdefault(j, []).extend(b)

    # d ={}
# 名次,电影名称,总场次,人次,票价(元),导演,主演,上映时间,片长,制作国家/地区,电影类型
    with open('movieRank_dictionary2.csv','w',encoding='utf-8',newline='') as f:
        csvwriter = csv.writer(f)
        for i in d.items():
            csvwriter.writerow(i)
    print('over')