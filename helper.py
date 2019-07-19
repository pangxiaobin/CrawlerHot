#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 19-7-4 下午5:55
# @Author  : Hubery
# @File    : helper.py
# @Software: PyCharm

import requests
from requests.exceptions import ConnectionError

from settings import BASE_HEADERS


def get_text(url, options={}):
    """
    :param method: 请求方法
    :param url: 请求的目标url
    :param options:添加的请求头
    :return:
    """
    headers = dict(BASE_HEADERS, **options)
    print('正在抓取', url)
    try:
        res = requests.get(url, headers=headers, timeout=5)
        # print(res.status_code)
        if res.status_code == 200:
            print('抓取成功', url, res.status_code)
            return res
    except ConnectionError:
        print('抓取失败', url)
        return None
