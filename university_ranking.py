# 排名采用js格式，无法爬取
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
        return "error"


def fillUnivList(ulist, html):  # 将html页面放入list列表（ulist）
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find("tbody").children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr.find_all('td')
            aa = tds[1].find("a").text.strip()
            ulist.append([tds[0].text.string(), aa,
                          tds[4].text.string()])


def printUnivList(ulist, num):  # 打印列表
    print("{:^10}\t{:^6}\t{:^10}".format("排名", "学校名称", "分数"))
    for i in range(num):
        u = ulist[i]
        print("{:^10}\t{:^6}\t{:^10}".format(u[0], u[1], u[2]))


def main():
    url = 'https://www.shanghairanking.cn/_nuxt/static/1616049095/rankings/bcur/2020/payload.js'
    ulist = []
    html = getHTMLText(url)
    fillUnivList(ulist, html)
    printUnivList(ulist, 20)


main()
