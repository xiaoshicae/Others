import requests
import json


def get_proxies2():
    url = 'http://166.188.20.55:3000/api/proxy/web'
    headers = {
        'Content-Type': 'application/json'
    }
    data = {'name': '阿里', url: 'http://www.alipay.com/'}
    data = json.dumps(data)

    count = 0
    while count < 5:
        info = requests.post(url, headers=headers, data=data).json()
        print(info)
        region = info.get('proxy').get('region')

        if region != 'R3' and region != 'R4':
            url = info.get('proxy').get('url')
            proxies = {
                'http': 'http://%s' % url,
                'https': 'http://%s' % url
            }

            # ip = info.get('proxy').get('ip')
            # port = '30000'
            # proxies = {
            #     'http': 'http://%s:%s' % (ip, port),
            #     'https': 'http://%s:%s' % (ip, port)
            # }
            return proxies

    print('请求超过5次')


def get_proxies3():
    url = 'http://http-api.taiyangruanjian.com/getip?num=1&type=2&pro=0&city=0&yys=0&port=11&pack=9318&ts=0&ys=0&cs=0&lb=1&sb=0&pb=45&mr=1&regions='
    # url = 'http://http-api.taiyangruanjian.com/getip?num=1&type=2&pro=0&city=0&yys=0&port=1&pack=9318&ts=0&ys=0&cs=0&lb=1&sb=0&pb=45&mr=2&regions='
    resp = requests.get(url).json()
    print(resp)
    ip = resp.get('data')[0].get('ip')
    port = resp.get('data')[0].get('port')
    proxies = {
        'http': 'http://%s:%s' % (ip, port),
        'https': 'http://%s:%s' % (ip, port)
    }
    print('代理IP【%s】' % str(proxies))
    ip_port = str(ip) + ':' + str(port)
    return ip_port


if __name__ == '__main__':
    p = get_proxies3()
    print(p)
