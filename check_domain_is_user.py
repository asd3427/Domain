# # -*- coding: utf-8 -*-
# # @Time : 2021/1/13 4:36 下午
# # @Author : mike
# # @File : check_domain_is_use.py
# #        ┏┓　　　┏┓+ +
# # 　　　┏┛┻━━━┛┻┓ + +
# # 　　　┃　　　　　　　┃ 　
# # 　　　┃　　　━　　　┃ ++ + + +
# # 　　 ████━████ ┃+
# # 　　　┃　　　　　　　┃ +
# # 　　　┃　　　┻　　　┃
# # 　　　┃　　　　　　　┃ + +
# # 　　　┗━┓　　　┏━┛
# # 　　　　　┃　　　┃　　　　　　　　　　　
# # 　　　　　┃　　　┃ + + + +
# # 　　　　　┃　　　┃　　　　Codes are far away from bugs with the animal protecting　　　
# # 　　　　　┃　　　┃ + 　　　　神兽保佑,代码无bug　　
# # 　　　　　┃　　　┃！
# # 　　　　　┃　　　┃　　+　　　　　　　　　
# # 　　　　　┃　 　　┗━━━┓ + +
# # 　　　　　┃ 　　　　　　　┣┓
# # 　　　　　┃ 　　　　　　　┏┛
# # 　　　　　┗┓┓┏━┳┓┏┛ + + + +
# # 　　　　　　┃┫┫　┃┫┫
# # 　　　　　　┗┻┛　┗┻┛+ + + +
#
# import aiohttp
# import asyncio
# import multiprocessing
# import time
# import random
# from aiohttp_proxy import ProxyConnector, ProxyType
#
#
# async def check_domain_is_use(**keywords):
#     domain = open("not_check_domains.txt", 'r').read().split('\n')
#
#     s = keywords['keywords']['s']
#     e = keywords['keywords']['e']
#     domain_list = domain[s:e]
#     print(len(domain_list))
#     time_start = time.time()
#
#     url = 'http://panda.www.net.cn/cgi-bin/check.cgi?area_domain={}'
#     for domain in domain_list:
#
#         pplist = ['110.38.74.58:8080',
#                   '94.127.217.66:40115',
#                   '114.5.35.98:38554',
#                   '135.181.18.96:37291',
#                   '128.199.3.127:3127',
#                   '124.158.183.190:8080',
#                   '180.211.183.138:8080']
#         px = random.choice(pplist)
#         connector = ProxyConnector.from_url(f'http://{px}')
#         sess = aiohttp.ClientSession(connector=connector)
#
#         if ".cc" in domain or ".com" in domain or ".net" in domain or ".org:" in domain:
#             try:
#                 data = await sess.get(url=url.format(domain))
#                 data = await data.text()
#                 if "<original>210 : Domain name is available</original>" in data:
#                     with open('checked_domains.txt', 'a') as f:
#                         f.write(f"{domain}\n")
#                     print(f"{multiprocessing.Process.pid} is finish with {domain}")
#                 await sess.close()
#             except Exception as e:
#
#                 print(f'too fast of {e}')
#                 time.sleep(4)
#                 await sess.close()
#                 pass
#             else:
#                 continue
#         else:
#             await  sess.close()
#     time_end = time.time()
#     cost_time = time_end - time_start
#     print(f"{multiprocessing.Process.pid}花费时间：{cost_time}秒")
#
#
# def sub_loop(**keywords):
#     loop = asyncio.new_event_loop()
#     loop.run_until_complete(check_domain_is_use(keywords=keywords))
#
#
# async def main():
#     s = 0
#     e = 1000
#     for i in range(10):
#         p = multiprocessing.Process(target=sub_loop, kwargs={"s": s, "e": e})
#         p.start()
#         s += 1000
#         e += 1000
#
#
# if __name__ == '__main__':
#     asyncio.get_event_loop().run_until_complete(main())
import grequests
import random
import multiprocessing

domain_list = open('not_check_domains.txt', 'r').read().split('\n')


def exception_handler(request, exception):
    print(f'{request}   {exception}')

    # with open('error.txt', 'a', encoding='utf-8') as f:
    #     f.write('{}{}{}'.format(request, exception, '\n'))


def check_domain(s, e):
    pplist = ['36.94.142.163:8000',
              '188.252.97.34:80',
              '34.64.87.82:3128',
              '188.34.137.126:3128',
              '186.6.28.28:3128',
              '201.91.82.155:3128',
              '188.113.190.7:80',
              '51.178.220.22:3128',
              '20.186.110.157:3128',
              '79.120.177.106:8080',
              '192.53.115.97:8080',
              '47.57.188.208:80',
              '117.204.255.109:8080',
              '207.74.74.6:3128',
              '192.53.116.107:8080', ]

    domain = domain_list[s:e]
    url = 'http://panda.www.net.cn/cgi-bin/check.cgi?area_domain={}'
    req = (grequests.get(url.format(u), timeout=10, proxies={'http': 'http://{}'.format(random.choice(pplist))}) for u
           in domain if
           ".cc" in u or ".com" in u or ".net" in u or ".org:" in u)
    print(req)
    maps = grequests.map(req, gtimeout=10, exception_handler=exception_handler, size=15)
    print(maps)
    for i in maps:
        if i is not None and i.status_code == 200:
            if "<original>210 : Domain name is available</original>" in i.text:
                with open('checked_domains.txt', 'a') as f:
                    f.write(f"{i.url.replace('http://panda.www.net.cn/cgi-bin/check.cgi?area_domain=', '')}\n")


if __name__ == '__main__':
    s = 0
    e = 1000
    # check_domain(s, e)

    for i in range(10):
        p = multiprocessing.Process(target=check_domain, args=(s, e))
        s += 0
        e += 1000
        p.start()
