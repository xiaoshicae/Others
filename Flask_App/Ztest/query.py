import json
import time
from threading import Thread

import redis
import requests


def get_task():
    conn = redis.Redis()
    phone = conn.rpop('zhifubao_phone')
    if not phone:
        return None
    return phone.decode()


def push_task(phone):
    conn = redis.Redis()
    conn.lpush('zhifubao_phone_error', phone)


def phone_query(t_name):
    begin = time.time()
    print('thread【%s】 query begin！' % t_name)

    url = 'http://127.0.0.1:5000/phone/register/verify/'

    f = open('query_result_%s.log' % t_name, 'a', encoding='utf-8')

    while True:
        phone = get_task()
        if not phone:
            break

        data = {
            "serialNum": 'reg123',
            "phone": str(phone)
        }

        try:
            resp = requests.post(url, data=json.dumps(data))
            content = resp.content.decode()
            f.write(content+'\n')
            print('content: ', content)
        except Exception as e:
            print('e: ', e)
            push_task(phone)
    f.close()
    end = time.time()
    print('thread【%s】 query down！' % t_name)
    print('共花费%s秒' % str(end-begin))


def multi_thread(t_num):
    for n in range(t_num):
        t = Thread(target=phone_query, args=(str(n), ))
        t.start()


if __name__ == '__main__':
    # t_num = 5
    # multi_thread(t_num)
    phone_query(100)
