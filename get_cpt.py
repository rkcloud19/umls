import requests
from lxml.html import fromstring

api_key = "e5a89701-8989-4121-a1fb-39a478b1cefd"
params = {'apikey',api_key}
h = {"Content-type": "application/x-www-form-urlencoded","Accept":"text/plain","User-Agent":"python"}
r = requests.post("https://utslogin.nlm.nih.gov/cas/v1/api-key",data=params,headers=h)
response = fromstring(r.text)
tgtKey = response.xpath('//form/@action')[0]
print(tgtKey)