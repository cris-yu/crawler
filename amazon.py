import requests
url = "https://www.amazon.cn/dp/B084DPVJR7?ref_=nav_ya_signin&smid=A3TEGLC21NOO5Y&captcha_verified=1&"
try:
    kv = {'user-agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    print("error")
