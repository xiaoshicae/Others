# /usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'zhuangshui'
__time__ = '2019-03-08'

import os
import uuid
import random

from captcha.image import ImageCaptcha

from keras_model.config import *

# 字体
FONTS = [r'./fonts/consola.ttf']


def gen_single_captcha(captcha_chars, out_dir, fonts):
    """生成单张验证码"""
    image = ImageCaptcha(fonts=fonts)
    # image.generate('1234')
    captcha_file = captcha_chars + '_' + str(uuid.uuid4()) + '.png'
    image.write(captcha_chars, os.path.join(out_dir, captcha_file))


def gen_captcha(captcha_dir, num):
    """生成验证码"""

    for n in range(num):
        captcha_chars = [random.choice(CHARACTERS) for i in range(4)]

        chars = ''.join(captcha_chars)

        gen_single_captcha(chars, captcha_dir, FONTS)


def gen_train_captcha(num=51200):
    """生成train符验证码"""
    train_dir = r'./train'
    gen_captcha(train_dir, num)


def gen_test_captcha(num=5120):
    """生成test符验证码"""
    test_dir = r'./test'
    gen_captcha(test_dir, num)


if __name__ == '__main__':
    gen_train_captcha()
    gen_test_captcha()

