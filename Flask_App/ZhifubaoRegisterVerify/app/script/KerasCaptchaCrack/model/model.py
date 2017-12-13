# --*-- coding: utf-8 --*--
import os
import importlib

import keras.backend as K
from keras.models import Input, Model
from keras.layers import Convolution2D, MaxPooling2D, Reshape, Dense, GRU, Dropout, Lambda
from keras.layers.merge import add
from keras.optimizers import SGD


# 选用tensorflow作为BACKEND
os.environ['KERAS_BACKEND'] = 'tensorflow'
K.set_image_dim_ordering('tf')


# 公共参数
from . import config
config_module = config
characters = config_module.CHARACTERS
captcha_len, captcha_class = config_module.CAPTCHA_LEN, config_module.CAPTCHA_CLASS
width, height = config_module.IMG_WIDTH, config_module.IMG_HEIGHT


# # 定义 CTC Loss
def ctc_lambda_func(args):
    y_pred, labels, input_length, label_length = args
    y_pred = y_pred[:, 2:, :]
    return K.ctc_batch_cost(labels, y_pred, input_length, label_length)


# # 定义网络结构
def model(print_model=False):
    rnn_size = 128
    input_tensor = Input((width, height, 3))

    x = input_tensor
    for i in range(3):
        x = Convolution2D(32, (2, 2), activation='relu')(x)
        x = Convolution2D(32, (2, 2), activation='relu')(x)
        x = MaxPooling2D(pool_size=(2, 2))(x)

    conv_shape = x.get_shape()

    x = Reshape(target_shape=(int(conv_shape[1]), int(conv_shape[2] * conv_shape[3])))(x)
    x = Dense(32, activation='relu')(x)

    gru_1 = GRU(rnn_size, return_sequences=True, kernel_initializer="he_normal", name='gru1')(x)
    gru_1b = GRU(rnn_size, return_sequences=True, go_backwards=True, kernel_initializer="he_normal", name='gru1_b')(x)
    gru1_merged = add([gru_1, gru_1b])

    gru_2 = GRU(rnn_size, return_sequences=True, kernel_initializer="he_normal", name='gru2')(gru1_merged)
    gru_2b = GRU(rnn_size, return_sequences=True, go_backwards=True, kernel_initializer="he_normal", name='gru2_b')(
        gru1_merged)

    x = add([gru_2, gru_2b])
    x = Dropout(0.25)(x)
    x = Dense(captcha_class, kernel_initializer="he_normal", activation='softmax')(x)

    # base_model = Model(input=input_tensor, output=x)
    # sgd = SGD(lr=0.001, decay=1e-6, momentum=0.9, nesterov=True)
    # # lr:学习率  decay:学习率衰减率  momentum:动量(值越大,约趋向于原来变化方向)  nesterov:牛顿动量 - 对传统momentum方法的一项改进
    base_model = Model(inputs=[input_tensor], outputs=[x])
    # base_model.compile(loss='categorical_crossentropy', optimizer='adadelta', metrics=['accuracy'])

    labels = Input(name='the_labels', shape=[captcha_len], dtype='float32')
    input_length = Input(name='input_length', shape=[1], dtype='int64')
    label_length = Input(name='label_length', shape=[1], dtype='int64')
    loss_out = Lambda(ctc_lambda_func, output_shape=(1,), name='ctc')([x, labels, input_length, label_length])

    # model = Model(input=[input_tensor, labels, input_length, label_length], output=[loss_out])
    model = Model(inputs=[input_tensor, labels, input_length, label_length], outputs=[loss_out])

    model.compile(loss={'ctc': lambda y_true, y_pred: y_pred}, optimizer='adadelta')

    # 打印模型
    if print_model:
        from keras.utils import plot_model
        plot_model(base_model, to_file='base_model.png', show_shapes=True)
        plot_model(model, to_file='model.png', show_shapes=True)

    return base_model, model

if __name__ == '__main__':
    model(True)
