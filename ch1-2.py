import requests
from bs4 import BeautifulSoup
url="http://politics.people.com.cn/n1/2018/1020/c1001-30352747.html"
try:
    r=requests.get(url,timeout=5)
except requests.Timeout:
    print("程序超时")
if r.status_code==200:
    r.encoding=r.apparent_encoding
    bsObj=BeautifulSoup(r.text,"html.parser")
    title=bsObj.find("h1").text
    node=bsObj.find("div",{"id":"rwb_zw"})
    content=node.text
    with open("dirty_content.txt","w",encoding="utf8") as f:
        f.write("title"+title+"\n"+content)