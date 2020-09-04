#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = "yang";

'''
起点小说 
robots.txt
https://www.qidian.com/robots.txt
'''

import requests;
from bs4 import BeautifulSoup;
import re;
import uuid;

__page = 10;

# 获取文章内容
def qidian_page(url):
    # requests获取页面类容
    r = requests.get("http:"+url);
    # 乱码处理
    r.encoding = r.apparent_encoding;


    # 请求首页后获取整个html界面
    blog = r.content;
    # 用html.parser解析页面标签
    bs = BeautifulSoup(blog,"html.parser");

    tag_soup = bs.find(name="div", attrs={"class":"read-content j_readContent"});
    result = tag_soup.get_text().replace("　　", "\n\r");

    return result;

# 获取页面内容
def qidians_page(url):
    news_list = [];

    r = requests.get(url);
    r.encoding = r.apparent_encoding;

    bs = BeautifulSoup(r.text, "html.parser");
    # print(bs);
    # 获取标签
    li_list = bs.find(name="div", attrs={"class": "volume"}).find_all(name='li');
    for i in li_list:
        name = i.get_text();
        if name == "":
            pass;
        else:
            news_dict =[];
            url = i.findChildren("a",recursive=False)[0].attrs['href'];
            news_dict.append(url);
            news_dict.append(name);
            news_list.append(news_dict);
            result = qidian_page(url);
            test_keep(result,name);
    # return news_list;




# 保存文件
def test_keep(result,name):
    name=name.replace("?","");

    # f = open('/python/text/%s'%(uuid.uuid1(),), 'w');
    f = open('/python/text/%s' % (name,), 'w');
    f.write(result);
    f.close();
    print("succes!");

if __name__ == '__main__':
    # qidian_page("https://read.qidian.com/chapter/1unaNktdAOLH0qbqCO3QNg2/_7ASwMkFg5_4p8iEw--PPw2");
    qidians_page("https://book.qidian.com/info/1022313175#Catalog");