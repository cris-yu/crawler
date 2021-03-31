import requests
url = "https://www.ip138.com/ip.asp?ip="
try:
    r = requests.get(url+'183.173.94.129')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-500:])
except:
    print("error")
