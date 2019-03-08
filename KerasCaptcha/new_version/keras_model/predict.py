# /usr/bin/python3
# -*- coding: utf-8 -*-


__author__ = 'zhuangshui'
__time__ = '2019-03-08'

import numpy as np
import keras.backend as K

from keras_model.config import *
from keras_model.model import get_model


def predict_(img, img_type='base64'):
    """验证码预测"""
    if img_type == 'base64':
        convert_img(img)


def convert_img(img):
    pass


def predict(model_weight_path, img_data):
    conv_shape, base_model, model = get_model()

    model.load_weights(model_weight_path)
    all_characters = CHARACTERS + ' '

    X = img_data
    X = np.expand_dims(X, 0)

    y_pred = model.predict(X)
    y_pred = y_pred[:, 2:, :]

    out = K.get_value(K.ctc_decode(y_pred, input_length=np.ones(y_pred.shape[0]) * y_pred.shape[1], )[0][0])[:, :4]

    return ''.join([all_characters[x] for x in out[0]])
