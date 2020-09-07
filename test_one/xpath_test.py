#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = "yang";

'''
xpath test
'''

import requests;
from lxml import etree;


def new_page_data(url):
    r = requests.get(url);
    r.encoding = r.apparent_encoding;

    html_xpath = etree.HTML(r.text);
    new_span = html_xpath.xpath("//div[@class='wy_contMain fontSt']//span[position()=2]");
    print(type(new_span[0].text));
    print(new_span[0].text);
    new_span = html_xpath.xpath("//div[@class='wy_contMain fontSt']//span[position()=2]//text()");
    print(type(new_span[0]));
    print(new_span[0]);

def news_page_data(url):
    r = requests.get(url);
    r.encoding = r.apparent_encoding;

    html_xpath = etree.HTML(r.text);
    li_list = html_xpath.xpath("//div[@class='contMain fontSt']//li");
    for li in li_list:
        span = li.xpath("./span");
        # print(type(span));
        # print(etree.tostring(span[0]).decode("utf-8"));
        print(span[0].text);
        a = li.xpath("./a");
        print(a[0].text);  # 获取 a 标签内容
        print(a[0].xpath("attribute::href")[0]);  # 获取 a 标签节点 href 属性

if __name__ == '__main__':
    url = "http://wsjkw.sc.gov.cn/scwsjkw/gzbd01/2020/9/3/fe0eb6e3101d4709a9bbd27f5a12ae78.shtml";
    new_page_data(url);
    # url = "http://wsjkw.sc.gov.cn/scwsjkw/gzbd01/ztwzlmgl.shtml";
    # news_page_data(url);