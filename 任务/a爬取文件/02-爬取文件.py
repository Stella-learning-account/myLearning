from importlib.resources import contents
from multiprocessing import Pool
from ntpath import join
import requests
from lxml import etree
import csv 

def work(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77"
    }
    resp = requests.get(url,headers=header)
    resp.encoding = 'utf-8'
    # print(url)
    html = etree.HTML(resp.text)
    data_list = []
    for i in range(1,51):
        content = html.xpath(f'//*[@id="content"]/div[2]/table/tbody/tr[{i}]/td//text()')
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
        data_list.append(['/'.join(content+direct+act+time+long+place+type)])
    # print(data_list)
    print('end: ' + url)
    resp.close()
    resp2.close()
    return data_list


if __name__ == "__main__":
    urls,pro = [],[]
    pool = Pool(10)
    for i in range(10):
        url = f'http://58921.com/alltime/wangpiao?page={i}&pagr=7'
        pro.append(pool.apply_async(func=work,args=(url, )))
    pool.close()
    pool.join()
    listw = []
    for _r in pro:
        listw.append(_r.get())
    d ={}
    for part in listw:
        for row in part:
            d[row[0].split('/',1)[0]] = row[0].split('/',1)[1].replace(',', '，')
    with open('movieRank_dictionary.csv','w',encoding='utf-8',newline='') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(['名次','电影名称','总场次','人次','票价(元)','导演','主演','上映时间','片长','制作国家/地区','电影类型'])
        for i in d.items():
            csvwriter.writerow(i)
    with open('movieRank_justList.csv','w',encoding='utf-8',newline='') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(['名次','电影名称','总场次','人次','票价(元)','导演','主演','上映时间','片长','制作国家/地区','电影类型'])
        for part in listw:
            for row in part:
                csvwriter.writerow(row)
    print('over')