import os
import json
import logging

from flask import request
from flask import send_from_directory

from . import main
from ..script.PhoneRegisterCheck import PhoneRegisterCheck


info_logger = logging.getLogger("info_log")
err_logger = logging.getLogger("err_log")
detail_logger = logging.getLogger("detail_log")

api_list = {
    'url': 'phone/register/verify/',
    'method': 'POST',
}


@main.route('/')
def index():
    ip = request.remote_addr
    return 'hello, your ip is %s' % ip


@main.route('/phone/register/verify/', methods=['POST'])
def phone_verify():
    ip = request.remote_addr
    detail_logger.info(str(ip) + " call interface")

    result = {'serialNum': None, 'errorCode': 0, 'errorReason': None}

    try:
        data = json.loads(request.get_data())
    except Exception as e:
        result['statusCode'] = -1
        result['failReason'] = 'Data type is not json'
        err_logger.error(json.dumps(result) + ' & Exception: ' + str(e))
        return json.dumps(result)

    if 'serialNum' not in data.keys():
        result['statusCode'] = -1
        result['failReason'] = 'Missing parameter "serialNum"'
        err_logger.error(json.dumps(result))
        return json.dumps(result)

    if 'phone' not in data.keys():
        result['serialNum'] = data.get('serialNum', '')
        result['statusCode'] = -1
        result['failReason'] = 'Missing parameter "phone"'
        err_logger.error(json.dumps(result))
        return json.dumps(result)

    result['serialNum'] = data.get('serialNum', '')
    phone = data.get('phone', '')
    result['phone'] = phone
    prc = PhoneRegisterCheck()
    check_result = prc.check(phone)
    result['checkResult'] = check_result

    info_logger.info(json.dumps(result))
    return json.dumps(result)


@main.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(os.path.abspath('..'), 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
    pass
