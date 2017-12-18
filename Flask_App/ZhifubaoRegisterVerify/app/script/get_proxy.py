# ! -*- encoding:utf-8 -*-
import sys
import time
import hashlib
import requests
# import grequests
from lxml import etree


def via_proxy2(url='https://accounts.alipay.com/console/dispatch.htm?scene_code=resetQueryPwd&page_type=fullpage&site=1', method='GET', data=None):
    _version = sys.version_info

    is_python3 = (_version[0] == 3)

    orderno = "ZF201712182576w1257f"
    secret = "06d4e69740774e419526c446de2a7230"

    ip = "forward.xdaili.cn"
    port = "80"

    ip_port = ip + ":" + port

    timestamp = str(int(time.time()))                # 计算时间戳
    string = "orderno=" + orderno + "," + "secret=" + secret + "," + "timestamp=" + timestamp

    if is_python3:
        string = string.encode()

    md5_string = hashlib.md5(string).hexdigest()                 # 计算sign
    sign = md5_string.upper()                              # 转换成大写
    # print(sign)
    auth = "sign=" + sign + "&" + "orderno=" + orderno + "&" + "timestamp=" + timestamp

    # print(auth)
    proxy = {"http": "http://" + ip_port, "https": "https://" + ip_port}
    headers = {"Proxy-Authorization": auth}
    if method == 'GET':
        r = requests.get(url, headers=headers, proxies=proxy, verify=False, allow_redirects=False)
    else:
        r = requests.post(url, headers=headers, proxies=proxy, verify=False, allow_redirects=False, data=data)

    # print(r.status_code)
    # print(r.content)
    # print(r.status_code)
    if r.status_code == 302 or r.status_code == 301:
        # print(r.headers)
        loc = r.headers['Location']
        url_f = loc
        print('url: ', url)
        print('loc: ', loc)
        if method == 'GET':
            r = requests.get(url_f, headers=headers, proxies=proxy, verify=False, allow_redirects=False)
        else:
            r = requests.post(url_f, headers=headers, proxies=proxy, verify=False, allow_redirects=False, data=data)
        # print(r.status_code)
        # print(r.text)

    return r


def via_proxy(url, method='GET', data=None, headers=''):
    # targetUrl = "http://test.abuyun.com/proxy.php"
    targetUrl = url

    # 代理服务器
    # proxyHost = "http-dyn.abuyun.com"
    # proxyPort = "9020"

    proxyHost = "http-pro.abuyun.com"
    proxyPort = "9010"

    # 代理隧道验证信息
    proxyUser = "H5MOZDK554Q1575P"
    proxyPass = "DB2D0AABF3EAB9C2"

    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
        "host": proxyHost,
        "port": proxyPort,
        "user": proxyUser,
        "pass": proxyPass,
    }

    proxies = {
        "http": proxyMeta,
        "https": proxyMeta,
    }

    if method == 'GET':
        resp = requests.get(targetUrl, proxies=proxies)
    else:
        resp = requests.post(targetUrl, proxies=proxies, data=data)
    return resp
    # print(resp.status_code)
    # print(resp.text)


if __name__ == '__main__':
    url = 'https://accounts.alipay.com:443/console/querypwd/logonIdInputReset.htm?site=1&page_type=fullpage&scene_code=resetQueryPwd'
    r = via_proxy(url)
    print(r)