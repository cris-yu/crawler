#最好大学排名
import requests
import re
from bs4 import BeautifulSoup
import bs4


# 获取目标网址的文本信息
def getHtmlText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "获取文本异常"


# 通过BeautifulSoup库解析网页，将需要的信息加入到一个列表中
def fillUnivList(ulist, demo):
    soup = BeautifulSoup(demo, "html.parser")
    for tr in soup.find("tbody").children:
        if isinstance(tr, bs4.element.Tag):  # 判断tr标签是不是bs4定义的tag标签，过滤掉其它的
            tds = tr.find_all('td')  # 将td标签内容加入到tds列表中
            ##  print(tds[0].text.strip())
            ##  print(tds[1].text.strip())
            ##  print(tds[2].text.strip())
            aa = tds[1].find("a").text.strip()  # 因为大学名字在td标签的子标签a中，所以需要单独提取
            ulist.append([tds[0].text.strip(), aa,
                          tds[4].text.strip()])  # 因为修正过后的网站标签中的内容直接用string获取为空，是因为有换行问题，所以用text获取并用strip删除回车符号显示


def printUlist(ulist, num):
    tplt = "{0:^10}{1:{3}^10}{2:^10}"
    print(tplt.format("序号", "学校名称", "分数", chr(12288)))  # 中文空格填充，能保证输出对齐
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))


def main():
    url = "https://www.shanghairanking.cn/rankings/bcur/2020"
    ulist = []
    demo = getHtmlText(url)
    fillUnivList(ulist, demo)
    printUlist(ulist, 30)


main()