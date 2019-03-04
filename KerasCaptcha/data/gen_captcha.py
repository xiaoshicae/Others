#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 14:51
# @Email   : Zhuangshui@qiyi.com
# @Desc    :  
import uuid
import random

from captcha.image import ImageCaptcha

from config import *

# 字体
FONTS = [r'F:\WorkSpace\others-master\KerasCaptcha\data\consola.ttf']


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


def gen_train_captcha(num=50000):
    """生成train符验证码"""
    train_dir = r'F:\WorkSpace\others-master\KerasCaptcha\data\captchas\train'
    gen_captcha(train_dir, num)


def gen_test_captcha(num=5000):
    """生成test符验证码"""
    test_dir = r'F:\WorkSpace\others-master\KerasCaptcha\data\captchas\test'
    gen_captcha(test_dir, num)


if __name__ == '__main__':
    gen_train_captcha()
    gen_test_captcha()
