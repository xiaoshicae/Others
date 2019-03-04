#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 15:11
# @Email   : Zhuangshui@qiyi.com
# @Desc    :

import random
import logging

import numpy as np
from PIL import Image
from keras.callbacks import EarlyStopping, ModelCheckpoint

from model.keras_model import get_ssd_model
from config import *

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    filename=os.path.join(BASE_DIR, 'status.log'),
    filemode='w'
)


def train(model):
    img_train_folder = os.path.join(BASE_DIR, 'data', 'captchas', 'train')

    # callbacks 回调函数,用于记录过程量
    model_parameter = os.path.join(BASE_DIR, 'model', 'model_parameter', 'weight_first.{epoch:02d}.hdf5')
    check_pointer = ModelCheckpoint(filepath=model_parameter)
    # model.load_weights(os.path.join(BASE_DIR, 'model', 'model_parameter', 'weights_first.25.hdf5'))
    hist = model.fit_generator(
        generator=generate_arrays_from_img(img_train_folder),
        steps_per_epoch=800,
        epochs=25,
        callbacks=[EarlyStopping(patience=10), check_pointer],
    )

    # model.save('model.h5')

    loss = hist.history
    logging.info('Loss: ' + str(loss))


def generate_arrays_from_img(folder):
    img_list = os.listdir(folder)
    random.shuffle(img_list)

    X = np.zeros((BATCH_SIZE, IMG_WIDTH, IMG_HEIGHT, 3), dtype=np.uint8)
    Y = np.zeros((BATCH_SIZE, CAPTCHA_LEN), dtype=np.uint8)

    flag = 0
    length = len(img_list)
    while True:
        for i in range(BATCH_SIZE):
            index = int(flag % length)
            file_name = img_list[index]

            y_label = file_name.split('_')[0].upper()
            img = os.path.join(folder, file_name)
            img_data = Image.open(img)
            X[i] = np.array(img_data).transpose((1, 0, 2))
            Y[i] = [CHARACTERS.find(x) for x in y_label]

            flag += 1

        yield [X, Y, np.ones(BATCH_SIZE) * 8,
               np.ones(BATCH_SIZE) * CAPTCHA_LEN], np.ones(BATCH_SIZE)


def main():
    logging.info('Task begin')

    base_model, model = get_ssd_model()
    train(model)

    logging.info('Task down')


if __name__ == '__main__':
    main()
