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
from multiprocessing import Process
import re
import time
import random


async def check_domain_is_use():
    domain_list = open("not_check_domains.txt", 'r').read().split('\n')
    print(len(domain_list))
    sess = aiohttp.ClientSession()
    time_start = time.time()
    web_site_names = []
    check_d = 0
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
        if ".cc" in domain or ".com" in domain or ".net" in domain or ".org:" in domain:
            try:
                data = await sess.get(url=url.format(domain))
                print(data.status)
                data = await data.text()
                if "<original>210 : Domain name is available</original>" in data:
                    with open('checked_domains.txt', 'a') as f:
                        f.write(f"{domain}\n")
            except Exception as e:
                print('too fast')
                time.sleep(4)
            else:
                continue
            await asyncio.sleep(2)
            time.sleep(3)

    time_end = time.time()
    cost_time = time_end - time_start
    print("花费时间：{}秒".format(cost_time))


loop = asyncio.new_event_loop()
loop.run_until_complete(check_domain_is_use())
