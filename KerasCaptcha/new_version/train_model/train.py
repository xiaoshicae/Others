# /usr/bin/python3
# -*- coding: utf-8 -*-
from keras.callbacks import ModelCheckpoint, EarlyStopping

from keras_model.model import get_model

__author__ = 'zhuangshui'
__time__ = '2019-03-08'
import os
import random

import numpy as np
from PIL import Image

from keras_model.config import *

IMG_TRAIN_FOLDER = '/Users/zhuangshui/PycharmProjects/github/others/KerasCaptcha/new_version/train_model/data/train'
MODEL_PARAMETERS_FOLDER = '/Users/zhuangshui/PycharmProjects/github/others/KerasCaptcha/new_version/train_model/model_parameters'


def gen_img_array(conv_shape):
    """img array 生成器"""

    img_list = os.listdir(IMG_TRAIN_FOLDER)
    random.shuffle(img_list)

    X = np.zeros((BATCH_SIZE, IMG_WIDTH, IMG_HEIGHT, 3), dtype=np.uint8)
    Y = np.zeros((BATCH_SIZE, CAPTCHA_LEN), dtype=np.uint8)

    position = 0
    train_img_len = len(img_list)

    while True:
        for i in range(BATCH_SIZE):
            index = int(position % train_img_len)
            file_name = img_list[index]

            y_label = file_name.split('_')[0].upper()
            img = os.path.join(IMG_TRAIN_FOLDER, file_name)
            img_data = Image.open(img)

            X[i] = np.array(img_data).transpose((1, 0, 2))
            Y[i] = [CHARACTERS.find(x) for x in y_label]

        yield [X, Y, np.ones(BATCH_SIZE) * int(conv_shape[1] - 2),
               np.ones(BATCH_SIZE) * CAPTCHA_LEN], np.ones(BATCH_SIZE)


def train():
    """模型训练"""
    conv_shape, base_model, model = get_model()
    model_parameter = os.path.join(MODEL_PARAMETERS_FOLDER, 'weight_first.{epoch:02d}.hdf5')
    check_pointer = ModelCheckpoint(filepath=model_parameter)
    # model.load_weights(os.path.join(BASE_DIR, 'model', 'model_parameter', 'weights_first.25.hdf5'))

    hist = model.fit_generator(
        generator=gen_img_array(conv_shape),
        steps_per_epoch=512000,
        epochs=100,
        callbacks=[EarlyStopping(patience=10), check_pointer],
    )

    model.save('model.h5')


if __name__ == '__main__':
    train()
