import requests

url = "https://fanyi.baidu.com/sug"

word = input("plz input your english words:")
dic = {
    "kw": word
}
# 发送post请求(post发送的数据必须放在字典中，通过data参数进行传递)
resp = requests.post(url,data=dic)
print(resp.json())#将服务器返回的内容直接处理成json()==》dict
resp.close()