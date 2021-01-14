# -*- coding: utf-8 -*-
# @Time : 2021/1/13 4:36 下午
# @Author : mike
# @File : check_domain_is_use.py
#        ┏┓　　　┏┓+ +
# 　　　┏┛┻━━━┛┻┓ + +
# 　　　┃　　　　　　　┃ 　
# 　　　┃　　　━　　　┃ ++ + + +
# 　　 ████━████ ┃+
# 　　　┃　　　　　　　┃ +
# 　　　┃　　　┻　　　┃
# 　　　┃　　　　　　　┃ + +
# 　　　┗━┓　　　┏━┛
# 　　　　　┃　　　┃　　　　　　　　　　　
# 　　　　　┃　　　┃ + + + +
# 　　　　　┃　　　┃　　　　Codes are far away from bugs with the animal protecting　　　
# 　　　　　┃　　　┃ + 　　　　神兽保佑,代码无bug　　
# 　　　　　┃　　　┃！
# 　　　　　┃　　　┃　　+　　　　　　　　　
# 　　　　　┃　 　　┗━━━┓ + +
# 　　　　　┃ 　　　　　　　┣┓
# 　　　　　┃ 　　　　　　　┏┛
# 　　　　　┗┓┓┏━┳┓┏┛ + + + +
# 　　　　　　┃┫┫　┃┫┫
# 　　　　　　┗┻┛　┗┻┛+ + + +

import aiohttp
import asyncio
import multiprocessing
import time
import random
from aiohttp_proxy import ProxyConnector, ProxyType


async def check_domain_is_use(**keywords):
    domain = open("not_check_domains.txt", 'r').read().split('\n')

    s = keywords['keywords']['s']
    e = keywords['keywords']['e']
    domain_list = domain[s:e]
    print(len(domain_list))
    time_start = time.time()

    url = 'http://panda.www.net.cn/cgi-bin/check.cgi?area_domain={}'
    for domain in domain_list:

        pplist = ['110.38.74.58:8080',
                  '94.127.217.66:40115',
                  '114.5.35.98:38554',
                  '135.181.18.96:37291',
                  '128.199.3.127:3127',
                  '124.158.183.190:8080',
                  '180.211.183.138:8080']
        px = random.choice(pplist)
        connector = ProxyConnector.from_url(f'http://{px}')
        sess = aiohttp.ClientSession(connector=connector)

        if ".cc" in domain or ".com" in domain or ".net" in domain or ".org:" in domain:
            try:
                data = await sess.get(url=url.format(domain), timeout=5)
                data = await data.text()
                if "<original>210 : Domain name is available</original>" in data:
                    with open('checked_domains.txt', 'a') as f:
                        f.write(f"{domain}\n")
                    print(f"{multiprocessing.Process.pid} is finish with {domain}")
                await sess.close()
            except Exception as e:
                print('too fast')
                time.sleep(4)
                await sess.close()
                pass
            else:
                continue
        else:
            await  sess.close()
    time_end = time.time()
    cost_time = time_end - time_start
    print(f"{multiprocessing.Process.pid}花费时间：{cost_time}秒")


def sub_loop(**keywords):
    loop = asyncio.new_event_loop()
    loop.run_until_complete(check_domain_is_use(keywords=keywords))


async def main():
    s = 0
    e = 1000
    for i in range(10):
        p = multiprocessing.Process(target=sub_loop, kwargs={"s": s, "e": e})
        p.start()
        s += 1000
        e += 1000


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
