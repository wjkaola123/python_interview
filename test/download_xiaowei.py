import requests

url = "http://down.cunguzhibo.com/xw/upload/202203/xiaowei_2.5.0.5.apk"
filename = "xiaowei_2.5.0.5.apk"

response = requests.get(url)
with open(filename, "wb") as file:
    file.write(response.content)

print("文件已下载完成。")