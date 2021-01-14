#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: Domain2.py
@time: 2020/3/31 上午 09:26
@desc:
'''
import grequests
import requests
import pandas as pd
from bs4 import BeautifulSoup
import requests
import random
import threading
import time
import multiprocessing


def exception_handler(request, exception):
    print('{}{}'.format(request, exception))


def prox():
    req = requests.get(
        "https://www.proxydocker.com/en/proxylist/api?email=a0981729934%40gmail.com&country=all&city=all&port=all&type=http-https&anonymity=all&state=all&need=all&format=json")
    data = req.json()['Proxies']
    datas = []
    for i in data:
        datas.append(('{}:{}'.format(i['ip'], i['port'])))
    return datas


# 对Time函数进行装饰器的添加，@timer引用timer装饰器函数


not_check_domain = open('not_check_domains.txt', 'r').read().split('\n')

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}


def exception_handler(request, exception):
    # print('{}{}'.format(request, exception))

    with open('error.txt', 'a', encoding='utf-8') as f:
        f.write('{}{}{}'.format(request, exception, '\n'))


web_site_names = open('checked_domains.txt', 'r').read().split('\n')


def chick_web_site_is_use(st, ed, pplist):
    # try:

    print('{}{}'.format(len(web_site_names[st:ed]), threading.currentThread()))
    # for web_site_name in web_site_names:  # todo
    # print('use{}'.format(proxys[0]))
    # print('查询:{}'.format(web_site_name))
    print('proxs {}'.format(len(pplist)))
    nums = len(pplist) / 2
    for web_site_name in web_site_names[st:ed]:
        print('开始检查 {}'.format(web_site_name))
        datas = True
        if datas is not False:
            # print(datas)
            history_url = {}
            times = []
            history_url[web_site_name] = [[], [], [], [], []]
            p_x = random.choice(pplist)
            try:
                try:
                    req = requests.get(
                        'https://web.archive.org/web/timemap/json?url={}&fl=original'
                        ',timestamp:14&filter=statuscode:200&filter=mimetype:text/html&collapse=timestamp:4&limit=100000'.format(
                            web_site_name), headers=headers,
                        proxies={'http': 'http://{}'.format(p_x)}, timeout=150)
                    # print('代理可以使用 {}'.format(p_x))
                    time.sleep(1)
                    with open('可以使用的代理.txt', 'a', encoding='utf-8') as f:
                        f.write('{}{}'.format(p_x, '\n'))
                # print(p_x)
                except Exception as e:
                    # print('代理无法使用 {}'.format(p_x))
                    # print(e)
                    px = random.choice(pplist)
                    print('换个试试看{}'.format(px))
                    req = requests.get(
                        'https://web.archive.org/web/timemap/json?url={}&fl=original'
                        ',timestamp:14&filter=statuscode:200&filter=mimetype:text/html&collapse=timestamp:4&limit=100000'.format(
                            web_site_name), headers=headers,
                        proxies={'http': 'http://{}'.format(px)}, timeout=150)
                    # print(px)~

                soup = BeautifulSoup(req.text, 'lxml')
                # print(soup.text)
                for i in soup.text.replace('\n', '').replace('[', '').replace(']', '').replace('"', '').split(
                        ','):
                    if '20' in i:
                        history_url[web_site_name][1].append(
                            'https://web.archive.org/web/{}/http://{}'.format(i, web_site_name))
                        history_url[web_site_name][3].append(i)
                        history_url[web_site_name][4].append(web_site_name)
                        times.append(int(i[0:4]))
                if len(history_url[web_site_name][1]) < 2:  # 如果网址 少于二 就是错的
                    history_url.pop(web_site_name)

                # time.sleep(5)

            except Exception as e:
                # print('!')
                # time.sleep(100)
                with open('error_urls.txt', 'a', encoding='utf-8') as f:
                    f.write('{}{}'.format(web_site_name, '\n'))
                continue
            try:
                ti = times[-1] - times[0]
                history_url[web_site_name][0].append(ti)
                # print(ti)
            except Exception as e:
                continue
            # print(history_url)
            # for wurl in history_url[web_site_name][1]:

            reqs = (grequests.get(u, headers=headers, timeout=60) for u in history_url[web_site_name][1])
            maps = grequests.map(reqs, gtimeout=60, exception_handler=exception_handler, size=2)
            d = 0
            for i in maps:
                # history_url = self.get_web_site_history()
                try:
                    soup = BeautifulSoup(i.text, 'lxml')

                    titles = (soup.find('title'))
                    titles = titles.text
                except:
                    titles = '疑似'
                history_url[web_site_name][2].append(titles)
            try:
                di = {'域名': history_url[web_site_name][4][0], '历史title': [history_url[web_site_name][2]],
                      '历史起站时间': history_url[web_site_name][3][0], '最后建站时间': history_url[web_site_name][3][-1],
                      '历史链接': [history_url[web_site_name][1]], '历史快照数': history_url[web_site_name][0][0]}
                df = pd.DataFrame(di, index=[1])
                df.to_csv('test.csv', mode='a', encoding='utf_8_sig', index=False, header=False)
                print('down>>{}{}'.format(web_site_name, datas))
            except Exception as e:
                with open('__name_ERROR.txt', 'a', encoding='utf-8') as f:
                    f.write('{}{}'.format(web_site_name, '\n'))


if __name__ == '__main__':
    # pplist = prox()
    pplist = ['110.38.74.58:8080',
              '94.127.217.66:40115',
              '114.5.35.98:38554',
              '135.181.18.96:37291',
              '128.199.3.127:3127',
              '124.158.183.190:8080',
              '180.211.183.138:8080']
    threads = []

    # for i in range(1):
    #     domains = n_check_domain[s:e]
    #     print(type(domains))
    #     threads.append(threading.Thread(target=check_domain_is_use, kwargs={"domain_list": not_check_domain[s:e]}))
    #     s += 100
    #     e += 100
    #
    #     threads[i].start()
    # for i in range(1):
    #     threads[i].join()
    # checked_domains = open('checked_domains.txt', 'r').read().split('\n')
    #
    # chick_web_site_is_use(0, 500, pplist)
    #
    s = 0
    e = 500
    ds = 0
    de = 923

    for i in range(10):
        threads.append(threading.Thread(target=chick_web_site_is_use, args=(s, e, pplist[ds:de])))
        s += 500
        e += 500
        ds += 923
        de += 923
        threads[i].start()
    for i in range(10):
        threads[i].join()
  # t1 = threading.Thread(target=chick_web_site_is_use, args=(40000, 45000, pplist[0:-1]))
# t2 = threading.Thread(target=chick_web_site_is_use, args=(45000, 50000, pplist[800:-1]))
# t3 = threading.Thread(target=chick_web_site_is_use, args=(50000, 55000, pplist[1600:-1]))
# t4 = threading.Thread(target=chick_web_site_is_use, args=(55000, 60000, pplist[::-1]))
# t5 = threading.Thread(target=chick_web_site_is_use, args=(60000, 65000, pplist[2200:-1]))
# t6 = threading.Thread(target=chick_web_site_is_use, args=(65000, 70000, pplist[2604:-1]))
# t7 = threading.Thread(target=chick_web_site_is_use, args=(70000, 75000, pplist[1500:-1]))
# t8 = threading.Thread(target=chick_web_site_is_use, args=(75000, 80000, pplist[908:-1]))
# t9 = threading.Thread(target=chick_web_site_is_use, args=(80000, -1, pplist[::-1]))
# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()
# t6.start()
# t7.start()
# t8.start()
# t9.start()
# # ~
# t1.join()
# t2.join()
# t3.join()
# t4.join()
# t5.join()
# t6.join()
# t7.join()
# t8.join()
# t9.join()
