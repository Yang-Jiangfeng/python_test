#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = "yang";

import requests;
from bs4 import BeautifulSoup;

# 获取地址
def muiscs_page(url):
    # requests获取页面类容
    r = requests.get(url);
    # 乱码处理
    r.encoding = r.apparent_encoding;

    # 请求首页后获取整个html界面
    blog = r.content;
    # 用html.parser解析页面标签
    bs = BeautifulSoup(blog, "html.parser");
    tag_soup = bs.find(name="div", attrs={"class": "songlist-group"}).find_all(name="a");
    # print(tag_soup)
    # list_img = [];
    for i in tag_soup:
        w = i["href"];
        print(w);
        url = "http://music.taihe.com"+w;

# 获取音乐
def muisc_page(url):
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
    # urlretrieve(tag_soup,"/python/img/%s.jpg"%(uuid.uuid1(),));
    print("succes");

if __name__ == '__main__':
    muiscs_page("http://music.taihe.com/songlist/263016");