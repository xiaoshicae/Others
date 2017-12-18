import requests
import json
import threading


def tt():
    for i in range(40):
        url = 'http://127.0.0.1:5020'

        resp = requests.get('http://127.0.0.1:5020/ip/get/')

        proxies = resp.json().get('proxies')
        print(proxies)

        resp2 = requests.post('http://127.0.0.1:5020/ip/del/', data=json.dumps(proxies))

        print(resp2.content)


def multi_thread():
    ttt = []
    for j in range(5):
        t = threading.Thread(target=tt)
        ttt.append(t)

    for t in ttt:
        t.start()


import redis


def redis_test():
    conn = redis.Redis(host='localhost', port='6379', db=1)
    s = conn.delete("{\"http\": \"http://123.55.92.35:37254\", \"https\": \"http://123.55.92.35:37254\"}")
    print(s)

if __name__ == '__main__':
    multi_thread()
    # redis_test()