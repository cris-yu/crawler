import requests
from requests.models import encode_multipart_formdata
r=requests.get("http://www.baidu.com")
r.encoding='utf-8'
print (r.text)
