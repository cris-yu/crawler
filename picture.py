import requests
import os
root = "/Users/yusi/Desktop/picture/1"  # 保存的目录
url = "https://images-cn.ssl-images-amazon.cn/images/I/714t2CZMx1L._AC_SL1400_.jpg"  # 图片链接
path = root+url.split('/')[-1]  # 以最后一个反斜杠后面的名称保存文件
try:
    if not os.path.exists(root):  # 如果路径不存在，创建路径
        os.mkdir(root)
    if not os.path.exists(path):  # 如果保存的文件不存在
        r = requests.get(url)  # 获取文件链接
        with open(path, 'wb')as f:  # 打开链接
            f.write(r.content)  # 写入链接
            f.close()  # 关闭
            print("success")  # 输出 成功
    else:
        print("already existed")  # 如果路径存在，显示已存在
except:
    print("error")
