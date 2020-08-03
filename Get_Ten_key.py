# -*- coding: utf8 -*-
import base64
import hashlib
import hmac
import time

import requests
import random

secret_id = "AKIDOuT8jSgd576xjLx2CGY4YM5Njx0ujxbf"
secret_key = "wSzl5IRQhqtngR64OeUJ3lXCXt7A1jP2"


def get_porxy():
    proxy = requests.get(
        'http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=0&city=0&yys=0&port=1&pack=44642&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions='
    ).text.replace(
        '\r', '').split('\n')
    time.sleep(2)
    print(proxy)


def get_string_to_sign(method, endpoint, params):
    s = method + endpoint + "/?"
    query_str = "&".join("%s=%s" % (k, params[k]) for k in sorted(params))
    return s + query_str


def sign_str(key, s, method):
    hmac_str = hmac.new(key.encode("utf8"), s.encode("utf8"), method).digest()
    return base64.b64encode(hmac_str)


def return_data(DomainName):
    """

    :param DomainName:
    :return:urls
    """
    # prox = get_porxy()
    # pr = random.choices(prox)
    endpoint = "domain.tencentcloudapi.com"
    data = {
        'Action': 'CheckDomain',
        'Nonce': 11886,
        'SecretId': secret_id,
        'DomainName': DomainName,
        'Timestamp': int(time.time()),
        'Version': '2018-08-08'
    }
    s = get_string_to_sign("GET", endpoint, data)
    data["Signature"] = sign_str(secret_key, s, hashlib.sha1)
    # print(data["Signature"])
    # 此处会实际调用，成功后可能产生计费
    try:
        try:

            resp = requests.get("https://" + endpoint, params=data,
                                proxies={'http': 'http://{}'.format('58.218.200.253:9220')})
            # print(resp.url)
            if resp.status_code == 200:
                #print(resp.json())

                time.sleep(1)
                if 'Available' in resp.json()['Response']:

                    datas = resp.json()['Response']['Available']
                    #rint(datas)
                    return datas
                else:
                    return False
        except Exception as e:
            print('好像太快')
            # time.sleep(100)
            proxs = ["117.57.63.22:4275",
                     "117.69.98.81:4251",
                     "218.62.233.150:4281",
                     "121.57.165.44:4245",
                     "120.34.241.169:4216",
                     "49.68.55.244:4243"]
            px = random.choice(proxs)
            resp = requests.get("https://" + endpoint, params=data,
                                proxies={'http': 'http://{}'.format(px)})
            if resp.status_code == 200:
                time.sleep(1)
                if 'Available' in resp.json()['Response']:

                    datas = resp.json()['Response']['Available']
                    # rint(datas)
                    return datas
                else:
                    return False
    except Exception as e:
        print('??哪里出错了{}'.format(e))
        return False

# s= return_data('jxgroup.org')
# print(s)
