#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = "yang";

'''
图片
'''

import requests;
from bs4 import BeautifulSoup;
from urllib.request import urlretrieve
import uuid;

# 获取地址
def qidians_page(url):
    # requests获取页面类容
    r = requests.get(url);
    # 乱码处理
    r.encoding = r.apparent_encoding;

    # 请求首页后获取整个html界面
    blog = r.content;
    # 用html.parser解析页面标签
    bs = BeautifulSoup(blog,"html.parser");
    tag_soup = bs.find(name="ul", attrs={"class":"new-search-result-box clearfix"}).find_all(name="a");

    # list_img = [];
    for i in tag_soup:
        w =i["href"];
        if("html" in w):
            # list_img.append(w);
            qidian_page(w);
    # return list_img;

# 获取图片
def qidian_page(url):
    # requests获取页面类容
    r = requests.get(url);
    # 乱码处理
    r.encoding = r.apparent_encoding;

    # 请求首页后获取整个html界面
    blog = r.content;
    # 用html.parser解析页面标签
    bs = BeautifulSoup(blog, "html.parser");
    tag_soup = bs.find(name="img", attrs={"class": "works-img"})["src"];
    # 保存图片
    urlretrieve(tag_soup,"/python/img/%s.jpg"%(uuid.uuid1(),));
    print("succes");

if __name__ == '__main__':
    qidians_page("http://www.nipic.com/design/web/index.html");
    # qidian_page("http://www.nipic.com/show/31201549.html");