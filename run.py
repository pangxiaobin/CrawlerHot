#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 19-7-19 下午4:10
# @Author  : Hubery
# @File    : run.py
# @Software: PyCharm
import json
import os

from apscheduler.schedulers.blocking import BlockingScheduler

from concurrent.futures import ThreadPoolExecutor
from crawler import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def run_crawler():
    """
    多线程爬取
    :return:
    """
    crawler_list = [crawler_zhi_hu, crawler_v2ex, crawler_github, crawler_wei_bo, crawler_tie_ba, crawler_dou_ban,
                    crawler_tian_ya, crawler_wang_yi]
    result = []
    with ThreadPoolExecutor(max_workers=4) as pool:

        def get_result(future):
            """
            这个是 add_done_callback()方法来添加回调函数,
            future.result()为函数运行的结果
            :param future:
            :return:
            """
            crawler_result = future.result()
            result.append(crawler_result)

            # 这里是分别保存为txt文件
            # hot_name = crawler_result.get('hot_name', '')
            # file_path = r'%s/%s.txt' % (os.path.join(BASE_DIR, 'result'), hot_name)
            # with open(file_path, 'a+', encoding='utf8') as f:
            #     f.write(str(crawler_result) + '\n')

        for future in crawler_list:
            pool.submit(future).add_done_callback(get_result)
    file_path = r'{}/result.json'.format(os.path.join(BASE_DIR, 'result'))
    with open(file_path, 'w', encoding='utf8') as f:
        f.write(json.dumps(result, ensure_ascii=False, indent=4))
    print('done')


def run():
    """
    定时爬取
    :return:
    """
    print('开启定时任务')
    scheduler = BlockingScheduler()
    scheduler.add_job(func=run_crawler, trigger='interval', minutes=20)  # 每20分钟抓取一次
    scheduler.start()


if __name__ == '__main__':
    run_crawler()
    run()
