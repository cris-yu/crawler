import requests
url="https://miaosha.jd.com/#100015111034"
try:
	r=requests.get(url)
	r.raise_for_status()
	r.encoding=r.apparent_encoding
	print(r.text[:1000])
except:
	print("error")