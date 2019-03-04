#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 15:11
# @Email   : Zhuangshui@qiyi.com
# @Desc    :

import json
import time
import numpy as np
import keras.backend as K
from PIL import Image

from model.keras_model import get_ssd_model
from config import *


def decode(y):
    characters = CHARACTERS + ' '
    y = np.argmax(np.array(y), axis=2)[:, 0]
    return ''.join([characters[x] for x in y])


def predict(model, img_data):
    model.load_weights(os.path.join(BASE_DIR, 'model_parameter', 'weights_first.7.hdf5'))
    characters2 = CHARACTERS + ' '

    X = img_data
    X = np.expand_dims(X, 0)

    y_pred = model.predict(X)
    y_pred = y_pred[:, 2:, :]
    out = K.get_value(K.ctc_decode(y_pred, input_length=np.ones(y_pred.shape[0]) * y_pred.shape[1], )[0][0])[:, :4]
    out = ''.join([characters2[x] for x in out[0]])
    print('y_pred: %s' % out)

    return out


def main(img):
    base_model, model = get_ssd_model()
    img_data = Image.open(img)
    # img_data.resize((80, 170))
    img_data = np.array(img_data).transpose((1, 0, 2))
    # out = predict(model, img_data)
    out2 = predict(base_model, img_data)
    return out2


def verify(times, model_params_dir, test_captcha_dir):
    characters2 = CHARACTERS + ' '
    base_model, model = get_ssd_model()

    base_model.load_weights(os.path.join(model_params_dir, 'weight_first.{}.hdf5'.format(str(times).zfill(2))))

    # folder = r'F:\WorkSpace\others-master\KerasCaptcha\data\captchas\test'
    img_list = os.listdir(test_captcha_dir)

    count = 0
    ttl = 0
    begin = time.time()
    for i in img_list:
        ttl += 1
        y_true = i.split('_')[0]

        img = os.path.join(test_captcha_dir, i)
        img_data = Image.open(img)
        img_data = np.array(img_data).transpose((1, 0, 2))
        X = img_data
        X = np.expand_dims(X, 0)
        y_pred = base_model.predict(X)
        y_pred = y_pred[:, 2:, :]
        out = K.get_value(K.ctc_decode(y_pred, input_length=np.ones(y_pred.shape[0]) * y_pred.shape[1], )[0][0])[:, :4]
        y_predict = ''.join([characters2[x] for x in out[0]])

        if y_predict.lower() == y_true.lower():
            count += 1
            print('count: 【%s】, ttl: 【%s】, 正确率: 【%s】' % (str(count), str(ttl), str(count / ttl)))
        else:
            print('img【%s】error, y_true: 【%s】, y_predict: 【%s】' % (i, y_true, y_predict))

    print('正确率为: %s' % str(count / ttl))
    print('共花费【%s】秒' % str(time.time() - begin))
    del base_model, model
    return {'times': times, 'accuracy': count / ttl}


def captcha_crack_test():
    """验证码识别测试"""
    model_params_dir = r'F:\WorkSpace\others-master\KerasCaptcha\model\model_parameters'
    test_captcha_dir = r'F:\WorkSpace\others-master\KerasCaptcha\data\captchas\test'

    f = open('captcha_crack_test.log', 'a', encoding='utf-8')
    for i in range(70, 91):
        r = verify(i, model_params_dir, test_captcha_dir)
        print(r)
        f.write(json.dumps(r) + '\n')
        f.flush()
    f.close()
    print('down!...')


if __name__ == '__main__':
    captcha_crack_test()
