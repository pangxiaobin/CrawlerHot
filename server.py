#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 19-8-2 下午10:04
# @Author  : Hubery
# @File    : server.py
# @Software: PyCharm

import os
import json
import web

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

urls = (
    '/hot', 'hot'
)
app = web.application(urls, globals())
application = app.wsgifunc()

class hot:
    def GET(self):
        web.header('content-type','text/json')
        web.header("Access-Control-Allow-Origin", "*")
        file_path = r'{}/result.json'.format(os.path.join(BASE_DIR, 'result'))
        with open(file_path, 'r', encoding='utf8') as f:
            json_data = f.read()
        return json.dumps(json_data)


if __name__ == "__main__":
    app.run()