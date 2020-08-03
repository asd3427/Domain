#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: baidu_share_for_JX.py
@time: 2020/4/30 上午 11:39
@desc:
'''
import tkinter as tk


def get_text():
    texts = input('输入')

    datas = texts.replace(' ', '').replace('链接:', '').replace('提取码:', ',').replace('链接:', '').replace(
        '复制这段内容后打开百度网盘手机App，操作更方便哦', '').split(',')
    print(datas)
    final = '下载|{}|tq={},jy=51acg.xyz'.format(datas[0], datas[1])
    print(final)


if __name__ == "__main__":
    while True:
        get_text()


