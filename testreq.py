# #!/usr/bin/env python
# # encoding: utf-8
# '''
# @author: caopeng
# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# @contact: deamoncao100@gmail.com
# @software: garner
# @file: testreq.py
# @time: 2020/7/20 下午 11:08
# @desc:
# '''
import grequests
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import asyncio
import time
from pyppeteer import launch
import random
import pandas
import threading


def exception_handler(request, exception):
    # print('{}{}'.format(request, exception))

    with open('error.txt', 'a', encoding='utf-8') as f:
        f.write('{}{}{}'.format(request, exception, '\n'))


def timer(function):
    def wrapper():
        time_start = time.time()
        function()
        time_end = time.time()
        cost_time = time_end - time_start
        print("花费时间：{}秒".format(cost_time))

    return wrapper


# 对Time函数进行装饰器的添加，@timer引用timer装饰器函数


def req():
    print('开始获取域名')
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
    web_site_names = []
    reqs = (
        grequests.get(
            'http://www.juming.com/ykj/?api_sou=1&ymhz=com&ymlx=0&qian2=500&jgpx=0&meiye=500&page={}&_={}'.format(u,
                                                                                                                  round(
                                                                                                                      time.time())),
            headers=headers, timeout=60) for u in range(1, 4))
    maps = grequests.map(reqs, gtimeout=60, exception_handler=exception_handler, size=2)
    d = 0

    for i in maps:
        soup = BeautifulSoup(i.text, 'lxml')
        domain = soup.find_all('a', attrs={'class': 'domainsc'})
        for j in domain:
            web_site_names.append(j.text)

    return web_site_names


web_site_names = req()


async def phase(st, ed, web, i):
    s = i
    jsondatas = {}
    web_site_names = web[st:ed]
    print(i, asyncio.Task.current_task())
    for web_site_name in web_site_names:
        browser = await  launch({'headless': True, 'args': [
            '--disable-extensions',
            '--hide-scrollbars',
            '--disable-bundled-ppapi-flash',
            '--mute-audio',
            '--no-sandbox',
            '--disable-setuid-sandbox',
            '--disable-gpu',
        ], 'dumpio': True})
        page = await browser.newPage()

        try:

            await page.goto('http://www.jucha.com/lishi-info?ym=a2Fua2Fua3UuY29t&token=5ff34')

            await page.evaluate('''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
            await page.evaluate('''() => {document.getElementById("domains").value ="%s"}''' % (web_site_name))
            await page.setViewport({'width': 1080, 'height': 640})
            print(i, '开始爬取{}'.format(web_site_name))
            await page.click('#domains_btns_q')
            time.sleep(5)
        except Exception as e:
            await page.close()
            await browser.close()
            print(
                1, s, e
            )
            continue
        try:
            # 鼠标移动到滑块，按下，滑动到头（然后延时处理），松开按键
            await page.hover('#nc_1_n1z')  # 不同场景的验证码模块能名字不同。
        except:
            return 1, page
        try:
            await page.mouse.down()
            steps = random.randint(58, 80)
            print("steps:{}".format(steps))
            await page.mouse.move(2000, 0, {'steps': steps})
            await page.mouse.up()
            await page.evaluate('''()=>{document.write('<p>'+tokenable1+'<p>')}''')
            token = await page.xpath('/html/body/p[1]')
            tokens = await (await token[0].getProperty('textContent')).jsonValue()
            print(web_site_name, tokens)
            if tokens == '5ff34':
                continue
            data = {
                'ym': web_site_name,
                'xq': 'y',
                'page': '1',
                'limit': '20',
                'token': tokens,  # token 是我手动去网页上抓取的
                'group': '1',
            }
            print(data)
            get_data = requests.post('http://47.56.160.68:81/api.php', data=data)

            get_data.encoding = 'utf-8'
            get_data.content.decode('unicode-escape')
            jsondatas[web_site_name] = get_data.json()
            print(get_data.json())
            print(jsondatas)

        except Exception as e:
            await page.close()
            await browser.close()
            print('{}:验证失败'.format(e))
            continue
        await page.close()
        await browser.close()
        #
        # time.sleep(6.5)
        # try:
        #     num_str = await page.xpath('/html/body/div[2]/div/div[3]/table/tbody/tr/td[3]/p')
        #     if len(num_str) < 1:
        #         time.sleep(3)
        #         num_str = await page.xpath('/html/body/div[2]/div/div[3]/table/tbody/tr/td[3]/p')
        #
        #     num_str1s = await (await num_str[0].getProperty('textContent')).jsonValue()
        #     num_str1 = int(num_str1s) + 2
        #
        #     datas = [[], []]
        #     if num_str1 - 2 <= 2:
        #         await page.close()
        #         await browser.close()
        #         continue
        # except Exception as e:
        #     print(2, i, e)
        #     continue
        # try:
        #     for i in range(2, num_str1):
        #         date = await page.xpath('//*[@id="tableList"]/tbody/tr[{}]/td[2]'.format(i))
        #         date_str = await (await date[0].getProperty('textContent')).jsonValue()
        #         title = await page.xpath('//*[@id="tableList"]/tbody/tr[{}]/td[3]'.format(i))
        #         title_str = await page.evaluate('item => item.textContent', title[0])
        #
        #         if title_str == '':
        #             title_str = '未知'
        #         datas[0].append(str(date_str))
        #         datas[1].append(title_str)
        #     di = {'域名': web_site_name, '历史title': str(datas[1]),
        #           "建站时间列表": str(datas[0]),
        #           '历史起站时间': datas[0][-1], '最后建站时间': datas[0][0],
        #           '历史快照数': num_str1 - 2}
        #     df = pandas.DataFrame(di, index=['0'])
        #     df.to_csv('test.csv', mode='a', encoding='utf_8_sig', header=False)
        #     print(s, 'down with {}'.format(web_site_name))
        #     time.sleep(1.5)
        #     await page.close()
        #     await browser.close()
        # except Exception as e:
        #     await page.close()
        #     await browser.close()
        #     print(3, s, e)
        #     continue
        #


if __name__ == '__main__':
    st = 0
    ed = 500
    task = []
    for i in range(2):
        task.append(phase(st=st, ed=ed, i=i, web=web_site_names))
        st+=500
        ed+=500
    loop = asyncio.new_event_loop()

    try:
        asyncio.set_event_loop(asyncio.new_event_loop())

        loop.run_until_complete(asyncio.wait(task))
    except KeyboardInterrupt as e:
        all_tasks = asyncio.Task.all_tasks()
        for task in all_tasks:
            print("cancel task")
            print(task.cancel())
        loop.stop()
        # stop 调用之后，需要调用 run_forever，不然会报错
        loop.run_forever()
    finally:
        loop.close()
# import asyncio
# from pyppeteer import launch
# !
# async def main():
#
#     browser = await launch({'args': ['--proxy-server={}:'], 'headless': False })
#     page = await browser.newPage()
#     await page.goto('https://www.myip.com/')
#     await page.authenticate({'username': 'user', 'password': 'passw'})
#     input()
#     await browser.close()
#
# asyncio.get_event_loop().run_until_complete(main())
# import time
#
#
# class InterviewTest:
#     def __init__(self):
#         pass
#
#     @staticmethod
#     def given_one(start, end):
#         """
#         :param start: 查詢開始時間 times map
#         :param end: 查詢結束時間 times map
#         :return: bout int 開始與結束共有次訪問
#         """
#         # visitors1:start time float(timesmap),end time float(timesmap)
#         # 假資料
#         start = round(start)  # 四捨五入
#         end = round(end)
#         visitors_time = {'visitors0': [1595940594, 1595940600], 'visitors1': [1595940594, 1595940610],
#                          'visitors2': [1595940400, 1595940600], 'visitors3': [1595940600, 1595940800]}
#         bout = 0
#         for i in range(0, len(visitors_time.keys())):
#             if visitors_time[f'visitors{i}'][0] <= start and visitors_time[f'visitors{i}'][1] <= end:
#                 bout += 1
#
#         return bout
#
#     def given_three(self, n):
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
#         else:
#             return self.given_three(n - 1) + self.given_three(n - 2)
#
#     @staticmethod
#     def given_four(lists):
#         n = len(lists)
#
#         if (n == 1):
#             return a[0]
#         max_neg = float('-inf')
#         min_pos = float('inf')
#         count_neg = 0
#         count_zero = 0
#         prod = 1
#         for i in range(0, n):
#             if lists[i] == 0:
#                 count_zero = count_zero + 1
#                 continue
#
#             if lists[i] < 0:
#                 count_neg = count_neg + 1
#                 max_neg = max(max_neg, lists[i])
#
#             if lists[i] > 0:
#                 min_pos = min(min_pos, lists[i])
#
#             prod = prod * lists[i]
#         if count_zero == n or (count_neg == 0 and count_zero > 0):
#             return 0
#
#         if count_neg == 0:
#             return min_pos
#
#         if (count_neg & 1) == 0 and count_neg != 0:
#             prod = int(prod / max_neg)
#
#         return prod
#
#     @staticmethod
#     def given_five(n):
#         datas = [0 for i in range(n + 1)]
#
#         for i in range(n + 1):
#
#             if i <= 2:
#                datas[i] = i
#             else:
#                 datas[i] =datas[i - 1] + (i - 1) * datas[i - 2]
#
#         return datas[n]
#
#
# ans1 = InterviewTest().given_one(1595940400, 1595940600)
# ans2 = InterviewTest().given_three(9)
# ans3 = InterviewTest().given_four([-1, -1, -2, 4, 3])
# ans4 = two = InterviewTest().given_five(9)
#
# print(f'第一題答案 : {ans1},\n第三題答案 : {ans2},\n第四題答案 : {ans3},\n第五題答案 : {ans4}')
