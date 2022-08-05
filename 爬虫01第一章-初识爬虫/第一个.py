from urllib import response
from urllib.request import urlopen

url = "http://www.baidu.com"
resp = urlopen(url)

with open("mybaidu.html", mode="w", encoding='utf-8') as f:
    f.write(response.read().decode("utf-8"))
print("over")
resp.close()#关掉程序