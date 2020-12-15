import requests
import json
import time
import random
from hashlib import md5

class YdSpider():
    def __init__(self):
        # F12抓包抓到的post地址
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        # Cookie, User-Agent, Referer检查概率最高
        self.headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Length": "241",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "OUTFOX_SEARCH_USER_ID=382211788@10.169.0.102; OUTFOX_SEARCH_USER_ID_NCOO=120454242.13681264; JSESSIONID=aaadkP1hVS3Uy7oJ_sKzx; ___rl__test__cookies=1608003941516",
            "Host": "fanyi.youdao.com",
            "Origin": "http://fanyi.youdao.com",
            "Referer": "http://fanyi.youdao.com/",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
}

    def md5_str(self, s):
        """加密函数"""
        m = md5()
        m.update(s.encode())
        return m.hexdigest()

    def get_ts_salt_sign(self, word):
        # 获取ts salt sign
        ts = str(int(time.time() * 1000))
        salt = ts + str(random.randint(0, 9))
        s = "fanyideskweb" + word + salt + "Tbh5E8=q6U3EXe+&L[4c@"
        sign = self.md5_str(s)

        return ts, salt, sign

    def attack_yd(self, word):
        """爬虫逻辑函数"""
        ts, salt, sign = self.get_ts_salt_sign(word)
        # 一般检查salt和sign
        form_data = {
            "i": word,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,
            "sign": sign,
            # "lts": ts,
            "bv": "a3a1f35bedb03effa4e1ddb4f2133c39",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME",
        }
        # 请求解析提取数据
        # html = requests.post(url=self.url, data=form_data, headers=self.headers).text
        # html = json.loads(html)
        html = requests.post(url=self.url, data=form_data, headers=self.headers).json()
        print(html['translateResult'][0][0]['tgt'])

    def crawl(self):
        word = input('请输入要翻译的单词:')
        self.attack_yd(word)

if __name__ == '__main__':
    spider = YdSpider()
    spider.crawl()