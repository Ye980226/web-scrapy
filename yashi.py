import requests
import json
import time
import threading
import queue
import random
import datetime 
class ThreadPool(object):
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self._q = queue.Queue(self.maxsize)
        for i in range(self.maxsize):
            self._q.put(threading.Thread)

    def getThread(self):
        return self._q.get()

    def addThread(self):
        self._q.put(threading.Thread)

while True:
    time.sleep(random.random()*10)
    Session = requests.session()

    # cookies = {"yieldify_ujt": "18", "RT": "dm=esteelauder.com&si=6af007a5-f769-495f-bf2c-dc817063336c&ss=1552017299672&sl=9&tt=471253&obo=0&sh=1552018849888%3D9%3A0%3A471253%2C1552018818692%3D8%3A0%3A453685%2C1552018501079%3D7%3A0%3A407622%2C1552018191828%3D6%3A0%3A338547%2C1552018036385%3D5%3A0%3A183160&bcn=%2F%2F17d98a5a.akstat.io%2F&r=https%3A%2F%2Fwww.esteelauder.com%2Fbest-sellers-skincare&ul=1552020004457"}
    cookies = {}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:65.0) Gecko/20100101 Firefox/65.0"}

    r = Session.get(
        "https://www.esteelauder.com/best-sellers-skincare", headers=headers, cookies=cookies)
    cookies.update(dict(r.cookies))
    # print(cookies)
    timestamp = int(time.time()*1000)
    cookies.update({"client.isMobile": "0", "elist15"	: "1", "elist15_expire": str(timestamp), "has_js": "1", "persistent_user_cookie":
                    '{"first_time":0,"first_name":null,"pc_email_optin":null,"email":null,"is_loyalty_member":null,"points":null,"loyalty_level":null,"loyalty_level_name":null,"points_to_next_level":null,"next_level":null,"next_level_name":null}', "PSN": "{}"})
    # r = Session.get("https://ui.powerreviews.com/stable-4.0-version.json")

    data = {"JSONRPC": '[{"method":"csrf.getToken","id":1,"params":[{}]}]'}
    r = Session.post(
        "https://www.esteelauder.com/rpc/jsonrpc.tmpl?dbgmethod=csrf.getToken", data=data, headers=headers, cookies=cookies)
    # print(r.json())
    data = {"JSONRPC": '[{"method":"analytics.getDataLayer","id":2,"params":[]}]'}
    r = Session.post(
        "https://www.esteelauder.com/rpc/jsonrpc.tmpl?dbgmethod=analytics.getDataLayer", data=data, cookies=cookies, headers=headers)
    data = {"JSONRPC": '[{"method":"prodcat.querykey","params":[{"products":["PROD26959","PROD39810","PROD42475","PROD55125","PROD29363","PROD55184","PROD56918","PROD13158","PROD61744","PROD46658","PROD56919","PROD56856","PROD59625","PROD24108","PROD46655","PROD21181","PROD3298","PROD31272","PROD25713","PROD2648","PROD2651"],"query_key":"catalog-mpp-volatile"}],"id":1}]'}
    r = Session.post(
        "https://www.esteelauder.com/rpc/jsonrpc.tmpl", data=data, cookies=cookies, headers=headers)
    # print(r.json())
    data = (r.json())[0]["result"]["data"]["dataLayer"]
    values = (r.json())[0]["result"]["value"]
    # urls = (r.json())[0]["result"]["data"]["dataLayer"]["product_impression_url"]
    # urls = list(map(lambda x: "https://www.esteelauder.com"+x, urls))
    # for url in urls:
    # print(url)
    # with open("Datawhale.json", "w") as f:
    # json.dump(r.json(), f)
    prices = data["product_impression_price"]
    product_names = data["product_impression_name"]
    skus = data["product_impression_sku"]
    sizes = data["product_impression_size"]
    isShoppables = list(map(lambda x: x["isShoppable"], values["products"]))
    for product_name, sku, size, price, isShoppable in zip(product_names, skus, sizes, prices, isShoppables):
        if isShoppable==0:
            print("缺货:\t"+" ".join([product_name,sku, size, str(price), str(isShoppable)]))
        if isShoppable==1:
            print("有货:\t"+" ".join([product_name,sku, size, str(price), str(isShoppable)]))
    print("*"*20)
    print(datetime.datetime.now())
    print("\n"*3)
    