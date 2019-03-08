# /usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'zhuangshui'
__time__ = '2019-03-08'

from flask import Flask, request, jsonify

from keras_model.predict import predict

app = Flask(__name__)


@app.route('/captcha/crack')
def crack_captcha():
    """验证码破解"""
    captcha_base64 = request.values.get('captcha_base64')
    if not captcha_base64:
        return jsonify({'code': 1, 'data': None, 'msg': '参数有误'})

    crack_ret = predict(captcha_base64)

    return jsonify({'code': 0, 'data': crack_ret, 'msg': ''})
