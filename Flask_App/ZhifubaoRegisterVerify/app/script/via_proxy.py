import sys
import time
import hashlib
import requests


class ViaXunDaiLiProxy:
    def __init__(self):
        _version = sys.version_info
        is_python3 = (_version[0] == 3)
        orderno = "ZF201712182576w1257f"
        secret = "06d4e69740774e419526c446de2a7230"
        ip = "forward.xdaili.cn"
        port = "80"
        ip_port = ip + ":" + port
        timestamp = str(int(time.time()))  # 计算时间戳
        string = "orderno=" + orderno + "," + "secret=" + secret + "," + "timestamp=" + timestamp
        if is_python3:
            string = string.encode()

        md5_string = hashlib.md5(string).hexdigest()  # 计算sign
        sign = md5_string.upper()  # 转换成大写
        auth = "sign=" + sign + "&" + "orderno=" + orderno + "&" + "timestamp=" + timestamp

        self.proxy = {"http": "http://" + ip_port, "https": "https://" + ip_port}
        self.headers = {"Proxy-Authorization": auth}
        self.session = requests.session()

    def get(self, url, *args, **params):
        resp = self.session.get(url, headers=self.headers, proxies=self.proxy, verify=False, allow_redirects=False)
        if resp.status_code == 302 or resp.status_code == 301:
            loc = resp.headers['Location']
            url_f = loc
            print('url【%s】重定向至【%s】' % (url, url_f))
            resp = self.session.get(url_f, headers=self.headers, proxies=self.proxy, verify=False,
                                    allow_redirects=False)
        return resp

    def post(self, url, data, *args, **params):
        resp = self.session.post(url, data=data, headers=self.headers, proxies=self.proxy, verify=False,
                                 allow_redirects=False)
        if resp.status_code == 302 or resp.status_code == 301:
            loc = resp.headers['Location']
            url_f = loc
            print('url【%s】重定向至【%s】' % (url, url_f))
            resp = self.session.post(url_f, data=data, headers=self.headers, proxies=self.proxy, verify=False,
                                     allow_redirects=False)
        return resp


class ViaABuYunProxy:
    def __init__(self):
        # 代理服务器
        proxyHost = "http-pro.abuyun.com"
        proxyPort = "9010"

        # 动态版
        proxyHost = "http-dyn.abuyun.com"
        proxyPort = "9020"

        # 代理隧道验证信息
        proxyUser = "H999HE14111C783D"
        proxyPass = "FD9156DF24B136B1"

        proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
            "host": proxyHost,
            "port": proxyPort,
            "user": proxyUser,
            "pass": proxyPass,
        }

        self.proxies = {
            "http": proxyMeta,
            "https": proxyMeta,
        }
        self.session = requests.session()
        # self.session = requests

    def get(self, url, *args, **params):
        resp = self.session.get(url, proxies=self.proxies)
        return resp

    def post(self, url, data, *args, **params):
        resp = self.session.post(url, data=data, proxies=self.proxies)
        return resp


if __name__ == '__main__':
    v = ViaABuYunProxy()
    resp = v.get('http://www.baidu.com')
    print(resp.content)
