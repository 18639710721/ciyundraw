#！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2020/5/514:42
# @Author : listem
# @File  ：爬虫.py
# @Software: PyCharm

# 数据的获取
# python

"""
Referer 防盗链
headers 请求头
User-Agent 用户代理 操作系统信息 浏览器信息
"""
import re
import requests
import csv
import jieba
import  wordcloud

# 1.网页蜘蛛  目标网站的url

# url = "https://api.bilibili.com/x/v1/dm/list.so?oid=186803402"
#
# # 请求头  使用字典表示
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
#
# }
# # 2.模拟浏览器发送请求  获取响应reponse内容
#
# response = requests.get(url,headers=headers)
#
# # 查看一下是否是自己想要获取的内容，可能会乱码
#
# html_doc = response.content.decode("utf-8")   # content二进制的解码 ，解码为utf-8
#
# # 3.解析网页  提取弹幕数据
#
# # 在d标签内用正则提取
#
# res = re.compile("<d.*?>(.*?)</d>")  # 括号里面的内容要使用 编译正则表达式
#
# danmu = re.findall(res,html_doc)   # 编译正则表达式并使用findall返回一个列表
#
# print(len(danmu))
#
# # 4.数据的保存  csv文件
#
# for i in danmu:
#     with open("I:\source code\\b站视频弹幕内容词云图展示\\b站弹幕.csv","a",newline="",encoding="utf-8-sig") as f:
#         writer = csv.writer(f)
#         danmu = []
#         danmu.append(i)
#         writer.writerow(danmu)

# 显示数据  数据可视化

# 可以通过词云图进行展示

f = open("I:\source code\\b站视频弹幕内容词云图展示\\b站弹幕.csv",encoding="utf-8")
txt = f.read()
txt_list = jieba.lcut(txt)
print(txt_list)    # 如何拼接整个字符串？
string = "".join(txt_list)
print(string)

w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color="white",
                        font_path="msyh.ttc",
                        scale=15,  # 间隔
                        stopwords={""}, # 停用词
                        # contour_width=

)

w.generate(string)
w.to_file("I:\source code\\b站视频弹幕内容词云图展示\\ciyuntu.png")










