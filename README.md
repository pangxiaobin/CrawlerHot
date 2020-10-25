### 说明
- 我的博客热点展示：https://www.panglb.top/hot/
- 前后端分离，后端使用轻量级框架web.py， 前端使用了layui，数据保存为本地json文件。
```shell
├── crawler.py  # 主要爬虫代码
├── helper.py  # 帮助函数
├── html    # 前端页面展示
│   ├── hot.html
│   └── layui  # 前端依赖
├── image
│   └── hot.png
├── LICENSE
├── README.md
├── requments.txt  # 环境依赖
├── result  # 爬虫数据保存
│   └── result.json
├── run.py  # 定时爬虫入口
├── server.py  # 后端服务
├── settings.py
└── uwsgi.ini  # uwsgi服务器配置
```

- 目前只写了以下热点信息的爬取

  - 知乎热榜
  - V2EX
  - GitHub
  - 新浪微博
  - 天涯
  - 贴吧
  - 豆瓣
  - 云音乐

- 环境

  - python3.6 

运行

- 下载

  ```shell
   git clone https://github.com/pangxiaobin/CrawlerHot.git
   cd CrawlerHot
  ```

- 安装依赖

  ```shell
  # 创建虚拟环境  需要安装virtualenv 和virtualenvwrapper
  mkvirtualenv hot
  pip install -r requments.txt
  # 注释 windows pip install uwsgi 会报错 windows下演示可先在requments.txt 注释掉uwsgi
  ```

- 本地运行效果展示

  - 数据爬取

  ```shell
  python run.py
  # 单独看爬虫效果 可以吧run() 注释
  # __name__ == '__main__':
  #    run_crawler()  # 单次爬虫运行
  #    run()  # 定时爬虫运行
  ```

  - 启动本地服务

  ```shell
  python server.py
  ```

  - 查看前端页面展示 

  ```
  把html/hot.html 在浏览器中打开就能看到效果了
  ```

- 服务器部署uwsgi+nginx 

  - 项目是前后端分离的，后端可以单独就uwsgi起服务，前端用nginx。
  - uwsgi起http服务

  ```uwsgi
  修改uwsgi.ini中的chdir
  # 这里指定你服务器端开放的端口
  http=0.0.0.0:8080
  # 配置工程目录 项目所在的绝对路径
  chdir=yourpath/CrawlerHot
  ```
  - 起动uwsgi
  ```shell
  uwsgi --ini uwsgi.ini
  ```
  - 修改前端请求的接口
  ```shell
  #/html/hot.html
  # 这里的127.0.0.1 要修改为你服务器的ip
  http://127.0.0.1:8080/hot =》http://server_ip:8080/hot
```

  - 配置nginx部署前端

  ```nginx
  # /etc/nginx/conf.d/default.conf 添加location 配置
  server {
      listen       80;
      # 这里更改为你服务器的ip
      server_name  your_server_ip;
      
      location /hot {
          # 绝对路径
         alias /youtpath/CrawlerHot/html;
         index hot.html;
      }
  }
  ```

  - 运行定时爬虫脚本

  ```shell
  nohup python -u run.py &  
  ```

    - 效果展示
    ![hot](https://github.com/pangxiaobin/CrawlerHot/raw/master/image/hot.png)



