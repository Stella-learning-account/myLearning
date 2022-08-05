import requests

url = "https://movie.douban.com/j/chart/top_list"

# 重新封装参数
param = {
    "type": "11",
    "interval_id": "100:90",
    "action": "",
    "start": 0,  # 变换此参数，可以获得转换页面后的数据（获得第"start"/"limit"页的数据）
    "limit": 200,  # 也可以直接增加他获取数据的限制，提升数据获取
}
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44 "
}
resp = requests.get(url=url, params=param, headers=header)
print(resp.json())
resp.close()
