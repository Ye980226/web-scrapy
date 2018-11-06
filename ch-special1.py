import redis
from decode_api import ch
from bs4 import BeautifulSoup
import time
import random
import math
import requests
from urllib.parse import unquote, quote
import re
from requests_toolbelt import MultipartEncoder
pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
redis_cli1 = redis.Redis(connection_pool=pool)
# 加密的信息，不需要看懂
ch.mxPageGuid._hexAligner = ch.mxPageGuid._getIntAligner(16)
# 构建请求会话
Session = requests.session()
# 伪装请求头
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1WOW64rv: 63.0)"}

r = Session.get("http://www.mafengwo.cn/poi/78212.html", headers=headers)
cookies = dict(r.cookies)
# unquote把url编码解析回中文
cookies = {key: str(unquote(value)) for key, value in cookies.items()}
# 存下之后要用的timestamp
timestamp = time.time()
# 因为cookies中有些固定值，遂自己构造字典
cookies.update({"__mfwvn": "1", "__mfwlv": str(
    int(timestamp)), "__mfwlt": str(int(timestamp))})
# 通过解析HTML，得到3个HTML中引入的url，保证模拟人类访问
bsObj = BeautifulSoup(r.text, "lxml")
bsObj = bsObj.findAll("script")

url1 = bsObj[1]["src"]  # js
url2 = bsObj[2]["src"]  # js
url3 = re.search("M.loadResource\(\"(.*?)\"\);", r.text).group(1)

# 因为后面内容的js里面需要传入时间戳，而且观察到时间戳，是在第二个响应cookies之前，所以在第一个响应cookies之后就尝试获取时间戳，已成功
timestamp_pagelet = int(time.time()*1000)
# 保证顺序访问，url3在第二次拿到cookies之后
r = Session.get(url1, headers=headers)
r = Session.get(url2, headers=headers)


# 生成multiple/form-data所需要的boundary的随机数，通过观察可以知道是1e14-1e15
random_number = random.randint(1e14, 1e15)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1WOW64rv: 63.0)",
           "Cookie": "PHPSESSID={}; oad_n={}; __mfwlv={}; __mfwvn={}; __mfwlt={}".format(quote(cookies["PHPSESSID"]), quote(cookies["oad_n"]), quote(cookies["__mfwlv"]), quote(cookies["__mfwvn"]), quote(cookies["__mfwlt"]))
           }
# 选取了一篇文章，所以还差fields里的u和dt没有做出自动化，不过很容易，只需要解析最初页面html的title，然后urlencode即可，u就是直接把文章链接，encode
data = MultipartEncoder(
    fields={
        "t": str(int(timestamp)), "hn": "www.mafengwo.cn", "u": "http%3A%2F%2Fwww.mafengwo.cn%2Fpoi%2F78212.html", "r": "direct", "lv": str(int(timestamp)), "vn":  "1", "ws": "1366x129", "sc": "1366x768", "s1": "zh-CN", "f1": "31.0", "cs": "UTF-8", "dt": "%E5%A2%A8%E5%B0%94%E6%9C%AC%E7%9A%87%E5%AE%B6%E6%A4%8D%E7%89%A9%E5%9B%AD%E6%94%BB%E7%95%A5%2C%E5%A2%A8%E5%B0%94%E6%9C%AC%E7%9A%87%E5%AE%B6%E6%A4%8D%E7%89%A9%E5%9B%AD%E9%97%A8%E7%A5%A8_%E5%9C%B0%E5%9D%80%2C%E5%A2%A8%E5%B0%94%E6%9C%AC%E7%9A%87%E5%AE%B6%E6%A4%8D%E7%89%A9%E5%9B%AD%E6%B8%B8%E8%A7%88%E6%94%BB%E7%95%A5%20-%20%E9%A9%AC%E8%9C%82%E7%AA%9D",
        "sts": str(int(timestamp)), "pid": str(ch.mxPageGuid.generate()), "brn": "Firefox", "brv": "63", "dev": "unknown", "os": "Windows", "os_ver": "Windows_unknow", "sid": "0", "ver": "1.2", "rdm": str(ch.mxPageGuid._getRandomInt(32)), "_nocache": str(int(timestamp * 1000)) + str(random.random()), "_method": "post"},
    boundary='-----------------------------' + str(random_number)
)
headers["Content-Type"] = "multipart/form-data; boundary=" + data.boundary
headers["Host"] = "tongji.mafengwo.cn"
headers["Referer"] = "http://www.mafengwo.cn/poi/78212.html"
# 为了获取cookies,代码不期望被看懂。
r = Session.post("http://tongji.mafengwo.cn/stat_click.gif",
                 headers=headers, data=data)
# 更新获取cookies的列表
cookies.update(dict(r.cookies))

# 因为Host更换，所以换一个headers
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1WOW64rv: 63.0)",
           "Host": "js.mafengwo.net",  "Connection": "keep-alive"}
r = Session.get(url3, headers=headers)

# 生成JQuery，181是指JQuery当前版本是1.8.1也可以做成自动化，通过解析前面引入JQuery的链接来自动获取，但短期内应该不会更新
string = "JQuery" + "181" + \
    str(random.random()).replace(".", "") + "_"

# 因为Host更换，所以更换headers
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1WOW64rv: 63.0)",
           "Host": "pagelet.mafengwo.cn", "Referer": "http://www.mafengwo.cn/poi/78212.html", "Connection": "keep-alive"}
r = Session.get(
    "http://pagelet.mafengwo.cn/user/apps/pagelet/pageViewHeadInfo?callback=%s&params={'type':1}&_=%s" % (string + str(timestamp_pagelet), str(int(time.time() * 1000))), cookies=cookies, headers=headers)

r = Session.get(
    'http://pagelet.mafengwo.cn/poi/pagelet/poiLocationApi?callback=%s&params={"poi_id":"78212"}&_=%s' % (string + str(timestamp_pagelet + 1), str(int(time.time() * 1000))), cookies=cookies, headers=headers)

r = Session.get(
    'http://pagelet.mafengwo.cn/poi/pagelet/poiTicketsApi?callback=jQuery%s&params={"poi_id":"78212"}&_=%s' % (string + str(timestamp_pagelet + 2), str(int(time.time() * 1000))), cookies=cookies, headers=headers)
r = Session.get(
    'http://pagelet.mafengwo.cn/poi/pagelet/poiCommentListApi?callback=%s&params={"poi_id":"78212"}&_=%s' % (string + str(timestamp_pagelet + 3), str(int(time.time() * 1000))), cookies=cookies, headers=headers)


redis_cli1.set('name1', r.text.encode().decode("unicode_escape"))
