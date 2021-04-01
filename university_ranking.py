#排名采用js格式，无法爬取
# 从网络上获取大学排名内容  getHTMLText()
# 提取网页内容信息到合适的数据结构  fillUnivList()
# 利用数据结构展示并输出结果  printUnivList()

from re import U
from bs4.builder import HTML
from bs4.element import Tag
import requests
from bs4 import BeautifulSoup
from requests.exceptions import Timeout
import bs4


def getHTMLText(url):  # 获取URL信息
    try:  # 输出URL内容
        r = requests.get(url, Timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(ulist, html):  # 将html页面放入list列表（ulist）
    soup = BeautifulSoup(html, "html.parser")
    for td in soup.find('body').children:
        if isinstance(th, bs4.element.Tag):
            tds = th('td')
            ulist.append([tds[0].string, tds[1].string], tds[2].string)


def printUnivList(ulist, num):  # 打印列表
    print("{:^10}\t{:^6}\t{:^10}".format("排名", "学校名称", "城市"))
    for i in range(num):
        u = ulist[i]
        print("{:^10}\t{:^6}\t{:^10}".format(u[0], u[1], u[2]))


def main():
    uinfo = []
    url = 'https://www.shanghairanking.cn/rankings/bcur/202011'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)


main()
