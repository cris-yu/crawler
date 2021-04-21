# 提交商品搜索请求，循环获取页面
# 对于每个页面，提取商品名称和价格信息
# 信息输出到屏幕

# import requests
# import re


# def getHTMLText(url):
#     try:
#         r = requests.get(url, Timeout=30)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#         return ""


# def parsePage(ilt, html):
#     try:
#         plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
#         tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
#         for i in range(len(plt)):
#             price = eval(plt[i].split(':')[1])
#             title = eval(tlt[i].split(':')[1])
#             ilt.append([price, title])
#     except:
#         print("")


# def printGoodslist(ilt):
#     tplt = "{:4}\t{:8}\t{:16}"
#     print(tplt.format("序号","价格","商品名称"))
#     count = 0
#     for g in ilt:
#         count = count+1
#         print(tplt.format(count, g[0], g[1]))


# def main():
#     goods = '书包'
#     depth = 2
#     start_url = 'https://s.taobao.com/search?q='+goods
#     infoList = []
#     for i in range(depth):
#         try:
#             url = start_url+'&s='+str(44*i)
#             html = getHTMLText(url)
#             parsePage(infoList, html)
#         except:
#             continue
#     printGoodslist(infoList)


# main()

import re
import requests


def get_html_text(url):
    try:
        hd = {'User-Agent': 'Chrome/89'}
        r = requests.get(url, headers=hd)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        # print(r.text)
        return r.text
    except Exception as e:
        print(e, '爬取失败')
        return False


def parser_page(ulist, html):
    try:
        # 匹配名称所在的标签
        name_tag_l = re.findall(r'p-name-type-2[\s\W\w]*?</em>', html)
        # 以em标签作为分隔符, 并删除内容文本以外的标签符号，提取到商品名
        name_l = [re.sub('\s*<.*?>\s*', '', i.split('<em>')[1]) for i in name_tag_l]
        # 匹配价格所在的标签
        price_tag_l = re.findall(r'p-price[\s\W\w]*?</i>', html)
        # 提取标签中的表示价格的价格
        price_l = [i.split('<i>')[-1].split('</i>')[0] for i in price_tag_l]
        for index in range(len(name_l)):
            ulist.append([price_l[index], name_l[index]])
    except Exception as e:
        print(e, '解析失败')


def print_goods_list(ulist):
    tplt = '{:^4}\t{:^6}\t\t{:^20}'
    print(tplt.format('序号', '价格', '商品名称'))
    count = 0
    for good in ulist:
        count += 1
        print(tplt.format(count, good[0], good[1]))


def main():
    info_list = []
    keyword = '书包'
    depth = 5
    start_url = 'https://search.jd.com/Search?keyword=' + keyword
    last_pg_num = 0
    for n in range(1, depth+1):
        try:
            now_pg_num = n + last_pg_num
            url = start_url + '&page=' + str(now_pg_num)
            last_pg_num = now_pg_num
            html = get_html_text(url)
            parser_page(info_list, html)
        except Exception as e:
            continue
    print_goods_list(info_list)


if __name__ == '__main__':
    main()


