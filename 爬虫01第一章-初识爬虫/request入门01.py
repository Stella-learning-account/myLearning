import requests

wd = input("输入一个你喜欢的明星：")
url = f"https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd={wd}"
dic = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44"
}
resp = requests.get(url,headers=dic)#headers=dic处理一个小小的反爬

print(resp)
print(resp.text)#拿到页面源代码
resp.close()