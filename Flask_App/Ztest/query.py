import base64
import json
import time
from threading import Thread
# import json

import redis
import requests


def get_task():
    return '13017202140'
    # conn = redis.Redis()
    # phone = conn.rpop('zhifubao_phone')
    # if not phone:
    #     return None
    # return phone.decode()


def push_task(phone):
    conn = redis.Redis()
    conn.lpush('zhifubao_phone_error', phone)


def phone_query(t_name):

    print('thread【%s】 query begin！' % t_name)

    url = 'http://127.0.0.1:5000/phone/register/verify/'

    f = open('query_result_%s.log' % t_name, 'a', encoding='utf-8')

    count = 0
    right = 0
    start = time.time()
    while True:
        count += 1
        phone = get_task()
        if not phone:
            break

        data = {
            "serialNum": 'reg123',
            "phone": str(phone)
        }

        try:
            begin = time.time()
            resp = requests.post(url, data=json.dumps(data))
            content = resp.content.decode()
            f.write(content + '\n')
            json_content = json.loads(content)

            r = json_content.get('checkResult').get('statusCode')
            if r == 0:
                right += 1
            print('本次耗时:【%.2fs】, content: ' % (time.time() - begin), json_content)
            print('平均耗时【%.2fs】, 成功率:【%.2f%%】,总请求次数:【%d】' % ((time.time()-start)/count, right/count, count))
        except Exception as e:
            print('e: ', e)
            push_task(phone)
    f.close()
    end = time.time()
    print('thread【%s】 query down！' % t_name)
    print('共花费%s秒' % str(end - begin))


def multi_thread(t_num):
    for n in range(t_num):
        t = Thread(target=phone_query, args=(str(n),))
        t.start()


def img_query():
    img_file = r'C:\Users\YongHu\Desktop\TMP\data\train\2ABU_abeb7912-d5af-11e7-ae6a-dc4a3e8b7c67.png'
    f = open(img_file, 'rb')
    img_data = f.read()

    img_b64 = base64.encodebytes(img_data).decode()

    url = 'http://127.0.0.1:5010/captcha/crack/'
    data = {
        "serialNum": 'zfb001',
        "imgBase64": img_b64
    }
    content = requests.post(url, data=json.dumps(data)).content

    return json.loads(content)['captcha']


if __name__ == '__main__':
    t_num = 3
    multi_thread(t_num)
    # print(img_query())
