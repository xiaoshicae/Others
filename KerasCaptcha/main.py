#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 15:11
# @Email   : Zhuangshui@qiyi.com
# @Desc    :  

import importlib
import numpy as np
import keras.backend as K
from PIL import Image

model_module = importlib.import_module('model')
config_module = importlib.import_module('config')


def decode(y):
    characters = config_module.CHARACTERS + ' '
    y = np.argmax(np.array(y), axis=2)[:, 0]
    return ''.join([characters[x] for x in y])


def predict(img):
    characters2 = config_module.CHARACTERS + ' '
    base_model, model = model_module.model()
    base_model.load_weights(r'F:\WorkSpace\others-master\KerasCaptcha\model_parameters\weights_first.23.hdf5')

    img_data = Image.open(img)
    img_data = np.array(img_data).transpose((1, 0, 2))
    X = img_data
    X = np.expand_dims(X, 0)
    y_pred = base_model.predict(X)
    y_pred = y_pred[:, 2:, :]
    out = K.get_value(K.ctc_decode(y_pred, input_length=np.ones(y_pred.shape[0]) * y_pred.shape[1], )[0][0])[:, :4]
    y_predict = ''.join([characters2[x] for x in out[0]])

    return y_predict


if __name__ == '__main__':
    img = r'F:\WorkSpace\others-master\KerasCaptcha\captcha.jpg'
    out = predict(img)
    print(out)

