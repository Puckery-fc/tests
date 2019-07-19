# -*- coding: utf-8 -*-
# File  : 666.py
# Date  : 2019/3/12

import requests
from bs4 import BeautifulSoup
import traceback  # 处理异常
import re


# 获取页面的函数
def getHTMLText(url, code = 'utf-8'):  # 这里编码事先查看网页的编码格式
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return ""


# 获取所有的股票代码保存在一个列表中
def getStockList(lst, stockURL):
    html = getHTMLText(stockURL, 'GB2312')
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
        except:
            continue


# 获取每只个股股票的信息并保存到文件中,并显示保存爬取的进度
def getStockInfo(lst, stockURL, fpath):
    count = 0
    for stock in lst:
        url = stockURL + stock + '.html'
        html = getHTMLText(url)
        try:
            if html == "":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div', attrs = {'class': 'stock-bets'})
            name = stockInfo.find.all(attrs = {'class': 'bets-name'})[0]
            infoDict.update({'股票名称': name.text.split()[0]})
            
            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val
            
            with open(fpath, 'a', encoding = 'utf-8') as f:
                f.write(str(infoDict) + '\n')
                count = count + 1
                print("\r当前进度:{:.2f}%".format(count * 100 / len(lst)), end = "")
        except:
            count = count + 1
            print("\r当前进度:{:.2f}%".format(count * 100 / len(lst)), end = "")
            continue


# 主函数
def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = 'H:\\BaiduStockInfo.txt'
    slist = []
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, output_file)


main()
