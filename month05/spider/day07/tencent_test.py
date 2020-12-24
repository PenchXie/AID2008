import requests
import json

url = 'https://careers.tencent.com/tencentcareer/api/post/Query?keyword=JAVA&pageIndex=1&pageSize=10&language=zh-cn&area=cn'

resp = requests.get(url=url).text
json_obj = json.loads(resp)
print(json_obj['Data']['Count'])