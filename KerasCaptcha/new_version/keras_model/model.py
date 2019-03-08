# /usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'zhuangshui'
__time__ = '2019-03-08'

from keras import backend as K
from keras.models import *
from keras.layers import *

from keras_model.config import *


def ctc_lambda_func(args):
    """ctc loss function"""
    y_pred, labels, input_length, label_length = args
    y_pred = y_pred[:, 2:, :]
    return K.ctc_batch_cost(labels, y_pred, input_length, label_length)


def get_model():
    """获取model"""
    input_tensor = Input((IMG_WIDTH, IMG_HEIGHT, CHANNEL))

    x = input_tensor
    for i in range(3):
        x = Convolution2D(32, 3, 3, activation='relu')(x)
        x = Convolution2D(32, 3, 3, activation='relu')(x)
        x = MaxPooling2D(pool_size=(2, 2))(x)

    conv_shape = x.get_shape()

    x = Reshape(target_shape=(int(conv_shape[1]), int(conv_shape[2] * conv_shape[3])))(x)

    x = Dense(32, activation='relu')(x)

    gru_1 = GRU(BATCH_SIZE, return_sequences=True, init='he_normal', name='gru1')(x)
    gru_1b = GRU(BATCH_SIZE, return_sequences=True, go_backwards=True,
                 init='he_normal', name='gru1_b')(x)

    gru1_merged = add([gru_1, gru_1b])

    gru_2 = GRU(BATCH_SIZE, return_sequences=True, init='he_normal', name='gru2')(gru1_merged)
    gru_2b = GRU(BATCH_SIZE, return_sequences=True, go_backwards=True,
                 init='he_normal', name='gru2_b')(gru1_merged)

    x = add([gru_2, gru_2b])
    x = Dropout(0.25)(x)

    x = Dense(CATEGORY_LEN, init='he_normal', activation='softmax')(x)
    base_model = Model(input=input_tensor, output=x)

    labels = Input(name='the_labels', shape=[CAPTCHA_LEN], dtype='float32')
    input_length = Input(name='input_length', shape=[1], dtype='int64')
    label_length = Input(name='label_length', shape=[1], dtype='int64')
    loss_out = Lambda(ctc_lambda_func, output_shape=(1,),
                      name='ctc')([x, labels, input_length, label_length])

    model = Model(input=[input_tensor, labels, input_length, label_length], output=[loss_out])
    model.compile(loss={'ctc': lambda y_true, y_pred: y_pred}, optimizer='adadelta')

    return conv_shape, base_model, model
