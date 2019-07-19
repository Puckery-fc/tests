# -*- coding: utf-8 -*-
# File  : sc.py
# Date  : 2019/3/12
import requests
import re

headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"}

def get_page(url):
    try:
        r=requests.get(url,headers=headers)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except Exception as e:
        print(e)

stock_list_url='http://quote.eastmoney.com/stocklist.html'

def get_stock_list(stock_list_url):
    try:
        stock_list=[]
        page=get_page(stock_list_url)
        stocks=re.findall(r'<li><a target="_blank" href="http://quote.eastmoney.com/sz(.*?).html">',page,re.S)
        for stock in stocks:
            stock_list.append(stock)
        return stock_list
    except Exception as e:
        print(e)


def get_stock_info(url,stock):
    try:
        stock_info={}
        page=get_page(url)
        name=re.findall('<a class="bets-name".*?>(.*?)\(',page,re.S)
        name=name[0].strip()
        stock_info['stock']=name
        stock_info['num']=stock
        datas=re.findall(r'<dl><dt>(.*?)</dt><dd.*?>(.*?)</dd>',page,re.S)
        for data in datas:
            key=data[0]
            val=data[1].strip()
            stock_info[key]=val
        with open("H:\\爬虫\\股票数据.txt","a",encoding="utf-8") as f:
            f.write(str(stock_info) + '\n')
    except Exception as e:
        print(e)


stock_list_url='http://quote.eastmoney.com/stocklist.html'
stock_list=get_stock_list(stock_list_url,)
count=0
for stock in stock_list:
    stock_info_url='https://gupiao.baidu.com/stock/sz'+str(stock)+'.html'
    get_stock_info(stock_info_url,stock)
    count=count+1
    print('\r当前进度:{:.2f}%'.format(count*100/len(stock_list)),end='')
