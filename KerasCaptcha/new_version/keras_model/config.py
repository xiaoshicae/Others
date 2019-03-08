# /usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'zhuangshui'
__time__ = '2019-03-08'

import string

CHARACTERS = string.digits + string.ascii_uppercase

BATCH_SIZE = 128
IMG_WIDTH = 160
IMG_HEIGHT = 60
CHANNEL = 3
CAPTCHA_LEN = 4
CATEGORY_LEN = len(CHARACTERS) + 1
