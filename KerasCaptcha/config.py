#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 15:11
# @Email   : Zhuangshui@qiyi.com
# @Desc    :  


import os
import string

# 程序主目录
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

# 字符可选范围
CHARACTERS = string.digits + string.ascii_uppercase

# 验证码字符长度,验证码字符类别数
CAPTCHA_LEN, CAPTCHA_CLASS = 4, len(CHARACTERS) + 1

# 验证码图片宽度,高度
IMG_WIDTH, IMG_HEIGHT = 160, 60

# 训练每批样本大小
BATCH_SIZE = 256
