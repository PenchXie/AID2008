'''
send request to jd and get the response
'''

import requests

resp = requests.get(url='https://www.jd.com/')
# text: the response text
html = resp.text
# content: byte, for images, files, etc.
html_b = resp.content
# status_code: HTTP response
code = resp.status_code
# url:
url = resp.url
print(code, url)