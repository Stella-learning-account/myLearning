import requests
from lxml import etree


lei = ['a','s','t','e']
erg = ['a','A','C','E']
o = []
o.append(','.join(lei+erg))
o.append(','.join(erg))
print(o)

url = f'http://58921.com/alltime/wangpiao?page=4'
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77"
}
resp = requests.get(url,headers=header)
resp.encoding = 'utf-8'
html = etree.HTML(resp.text)
for i in range(1,51):
    content = html.xpath(f'//*[@id="content"]/div[2]/table/tbody/tr[{i}]/td//text()')
    # web = 'http://58921.com' + html.xpath(f'//*[@id="content"]/div[2]/table/tbody/tr[{i}]/td[2]/a/@href')[0]
    print(content)
# print(html.xpath('//*[@id="content"]/div[2]/table/tbody/tr[1]/td[2]/a/@href'))
# # //*[@id="content"]/div[2]/table/tbody/tr[1]/td[2]/a
# //*[@id="content"]/div[2]/table/tbody/tr[1]/td[2]/a