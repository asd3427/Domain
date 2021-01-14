# -*- coding: utf-8 -*-
# @Time : 2021/1/13 11:36 上午
# @Author : mike
# @File : google_sheet.py


import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import aiohttp
from aiohttp import TCPConnector
from bs4 import BeautifulSoup
import asyncio

auth_json_path = 'my-project-c076d-4027763f84f3.json'
gss_scopes = ['https://spreadsheets.google.com/feeds']
# 連線
credentials = ServiceAccountCredentials.from_json_keyfile_name(auth_json_path, gss_scopes)
gss_client = gspread.authorize(credentials)
# 開啟 Google Sheet 資料表
spreadsheet_key = '13xjP6N8gYoN4qA_rYaXWUHXXzbfJqnC2aIA-72VcEmE'
# 建立工作表1
sheet = gss_client.open_by_key(spreadsheet_key)
dataframe = pd.DataFrame(sheet.sheet1.get_all_records())


async def get_():
    titles = []
    for i in dataframe.site_link:
        sess = aiohttp.ClientSession(connector=TCPConnector(ssl=False))
        data = await sess.get(i)
        soup = BeautifulSoup(await data.text(), 'lxml')
        title = soup.find('title')
        k = title.text
        titles.append(k)
        await  sess.close()
        print(titles)
    return titles


loop = asyncio.new_event_loop()
# data = loop.run_until_complete(get_())
sheet.sheet1.update("B2", [['[武侠风][风流刀客]ver8.01 官方中文步兵版[PC][国产ACT][不限速][会员免费] – 绿色QQ资源网'],
                           ['[姐姐的诱惑]Ver0.8a完整汉化版[PC][欧美SLG][网盘链接][会员免费] – 虎爷秘籍'],
                           ['[金庸群侠传X]Ver0.4Renpy重制中文版[PC+安卓][国产SLG][游戏网盘][会员免费] – 虎爷秘籍'],
                           ['[堕落]ver0.581完整汉化版[PC+安卓][欧美SLG][网盘链接][会员免费] – 虎爷秘籍'],
                           ['「治愈我的性瘾」完整汉化版「PC+安卓 网盘链接」 – 虎爷秘籍'],
                           ['「渴望的爱」Ver0.64完整汉化版「PC+安卓\u3000网盘链接」 – 虎爷秘籍'],
                           ['[NTR传说]Ve4.19完整汉化版[PC][日系SLG][网盘链接][会员免费] – 虎爷秘籍'],
                           ['[淑母老师风流记]完整汉化版[PC+安卓][欧美SLG][网盘链接][会员免费] – 虎爷秘籍'],
                           ['「我在兄弟会的时光」Ver0.5完整汉化版「PC\u3000网盘链接」 – 虎爷秘籍'],
                           ['「欲望之梦」1-12章完整汉化版「PC+安卓 网盘链接」 – 虎爷秘籍'],
                           ['[狂热妻母~迪伦的妈妈人O尽可夫 ]完整汉化版[PC][不限速][游戏网盘][会员免费] – 绿色QQ资源网'],
                           ['[美好PAPA家园与地下城]官方中文步兵无敌版[PC][欧美SLG][网盘链接][会员免费] – 虎爷秘籍'],
                           ['「爆炎怀孕 超エロ催.眠爆汝学园2」ver2.0完整汉化「PC/安卓 网盘链接」 – 虎爷秘籍'],
                           ['「我的新生活重置」Ver0.65完整汉化版「存档+CG+攻略 PC+安卓 网盘链接」 – 虎爷秘籍'],
                           ['「威利大冒险」Ve0.48完整汉化版「PC 网盘链接」 – 虎爷秘籍'],
                           ['[金庸群侠传X：绅士无双]ver19完整汉化[pc/安卓][国产RPG][不限速] – 绿色QQ资源网'],
                           ['[尾O行1-4]全系列中文版合集+青行灯COS珍藏版[PC][欧美SLG][不限速] – 绿色QQ资源网'],
                           ['「爱巢」正式最终完结版+国配动画「PC+安卓\u3000网盘链接」 – 虎爷秘籍'],
                           ['「舔狗生活」那个我爱的女孩 完整汉化版「完结 PC 网盘链接」 – 虎爷秘籍'],
                           ['「撒娇鬼:不求回报的母女」 完整汉化版「PC+安卓 网盘链接」 – 虎爷秘籍'],
                           ['「精灵·特别教师:異」官方中文步兵版「PC\u3000网盘链接」 – 虎爷秘籍'],
                           ['[和妈妈在孤岛银乱生活]完整汉化版[PC+安卓][日系RPG][游戏网盘][会员免费] – 虎爷秘籍'],
                           ['「金庸群侠传X」ver1.106终极整合「全攻略」「PC」「网盘链接」 – 虎爷秘籍'],
                           ['「夏日狂想曲~乡间的难忘回忆」Ver0.6完整汉化版「PC\u3000网盘链接」 – 虎爷秘籍'],
                           ['[腐化]ver2.10完整汉化版[PC+安卓][欧美SLG][游戏网盘][会员免费] – 虎爷秘籍'],
                           ['[我的大学生活] Ver0.52完整汉化版[PC][欧美SLG][不限速][会员免费] – 技术之路资源网'],
                           ['[HoneySelect 2:原欲]璇玑公主 ver1.8完整汉化步兵版[8月精修汉化整合版][PC][欧美SLG][不限速][会员免费] – 技术之路资源网'],
                           ['「居家隔离」汉化完结版「PC+安卓」「网盘链接」 – 虎爷秘籍'],
                           ['「终焉之刻 APPEND」 Ver2.01 汉化版「网盘链接」 – 虎爷秘籍'],
                           ['「魔王使魔」完整汉化版「PC」「日系SLG」「网盘链接」 – 虎爷秘籍'],
                           ['「哥哥，早上起床之前都要抱紧我哦」 中文版 存档「网盘链接」 – 虎爷秘籍'],
                           ['[骨头的故事:庄园]ver1.61完整汉化版[PC][欧美SLG][不限速][游戏网盘][会员免费] – 虎爷秘籍'],
                           ['「性.感的爱」 V20.1.1 中文汉化作弊版+全CG「pc+安卓」「网盘链接」 – 虎爷秘籍'],
                           ['[战国兰斯Rance] 全系列1-10部 汉化版合集 存档 全CG[不限速] – 技术之路资源网'],
                           ['[和妈妈在孤岛银乱生活]完整汉化版[PC+安卓][日系RPG][不限速][会员免费] – 技术之路资源网'],
                           ['[农民的追求]Ver2.00最新详细攻略[图文教程] – 虎爷秘籍'],
                           ['「死宅 天使 和银荡之家」 V1.05 汉化作弊版 动画「网盘链接」 – 虎爷秘籍'],
                           ['「自宅警备员2」「整合」完整汉化+1代「PC」「网盘链接」 – 虎爷秘籍'],
                           ['[松木夏令营 ]Ver1.9 完整汉化版[PC+安卓][欧美SLG][游戏网盘] – 虎爷秘籍'],
                           ['[欢迎来到异世界：随便侵饭NPC！]DL正式版[PC][日系SLG][游戏网盘] – 虎爷秘籍'],
                           ['[魔矢幻想]完整汉化版[PC+安卓][国产RPG][不限速][会员免费] – 技术之路资源网'],
                           ['「家事代行」 V2汉化修复版「PC+安卓」「网盘链接」 – 虎爷秘籍'],
                           ['[被魔军占领的街道]完整汉化版[PC+安卓][日系RPG][网盘链接][会员免费] – 虎爷秘籍'],
                           ['「女體化王子露特的H冒险」ver1.1完整汉化「PC 网盘链接」 – 虎爷秘籍'],
                           ['[梅丽亚与恶鬼之岛]完整汉化版[PC][日系RPG][网盘链接][会员免费] – 虎爷秘籍'],
                           ['[赫雷斯的角斗场]完整汉化版[PC][日系SLG][不限速][会员免费] – 绿色QQ资源网'],
                           ['「阴影笼罩的曼斯顿」Ver3.2完整汉化版「PC+安卓 网盘链接」 – 虎爷秘籍'],
                           ['「堕落觉醒」ver1.0完整汉化版「PC+安卓 网盘链接」 – 虎爷秘籍'],
                           ['[啪啪酒吧]官方中文步兵版+DLC完整合集[PC+安卓][日系SLG][网盘链接][会员免费] – 虎爷秘籍'],
                           ['[我的都市生活] Ver0.41B完整汉化版[PC+安卓][国产RPG][不限速][会员免费] – 绿色QQ资源网'],
                           ['[火影女忍训练:最后的战争 ]Ver2.2完整汉化版[PC][欧美SLG][不限速][会员免费] – 绿色QQ资源网'],
                           ['[母亲的诱x惑]Ver1.0完整汉化版[PC+安卓][欧美SLG][不限速] – 技术之路资源网'],
                           ['[猎马NTR-无情猎妈人]ver1.05完整汉化版[PC][日系RPG][不限速]会员免费] – 技术之路资源网'],
                           ['[我和妈妈&姐姐的夏天]Ver1.0最新攻略[老司机带路] – 技术之路资源网'],
                           ['[恶魔石板和被诅咒的狗子公主] 官方中文作弊完结版[PC+安卓][不限速] – 技术之路资源网'],
                           ['[潜O规则]ver0.30官方中文版[PC+安卓][欧美SLG][游戏网盘][会员免费] – 虎爷秘籍'],
                           ['「腐化」Ver1.95完整汉化版「PC+安卓\u3000网盘链接」 – 虎爷秘籍'],
                           ['[破碎的梦想之城]ver0.7(1.02)最新中文攻略[图文教程] – 虎爷秘籍'],
                           ['[私人定制发泄玩偶]完整汉化版[PC][欧美SLG][网盘链接][会员免费] – 虎爷秘籍'],
                           ['「末世余生」 Ver4.5.0 破解完整版「PC+安卓 网盘链接」 – 虎爷秘籍'],
                           ['[农民的追求]Ver2.00最新攻略[老司机带路] – 绿色QQ资源网'],
                           ['[模拟后宫]Ver0.3.1.1完整汉化版[PC+安卓][欧美SLG][不限速] – 技术之路资源网'],
                           ['[暴君]Ver0.91b完整汉化版[PC+安卓][欧美SLG][游戏网盘][会员免费] – 虎爷秘籍']]

                    )
