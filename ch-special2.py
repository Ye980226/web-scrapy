import redis
import re
from bs4 import BeautifulSoup
pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
redis_cli2 = redis.Redis(connection_pool=pool)

while True:
    content = redis_cli2.get("name1")
    redis_cli2.delete("name1")
    if content:
        html = content.decode("utf-8").replace(r"\/", "/")
        # print(html)
        comments = re.findall("<p class=\"rev-txt\">((.|\n)*?)</p>", html)
        # print(comments)
        for index, comment in enumerate(comments):
            print(str(index+1)+" : "+comment[0].replace("<br />", ""))
