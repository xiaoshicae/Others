import copy
import base64
import time
import json
import logging
import traceback

import requests
from lxml import etree
from selenium import webdriver
from requests.exceptions import Timeout, ReadTimeout, ProxyError, ConnectionError

info_logger = logging.getLogger("info_log")
err_logger = logging.getLogger("err_log")
detail_logger = logging.getLogger("detail_log")


class PhoneRegisterCheck:
    """
    支付宝注册情况检验:
        1. 实例化PhoneRegisterCheck;
        2. 调用check方法;
    检验返回的状态码:
        0 : 号码已注册;
        1 : 号码未注册;
        -1 : 结果异常(验证码错误, 其它错误);
    """
    driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

    def __init__(self):
        """
            初始化session, 获取IP代理
        """
        self.session = requests.session()
        self.proxies = copy.deepcopy(get_proxies())
        print('Get proxies:【%s】' % self.proxies)
        # self.proxies = None
        self.img_data = b''

    def get_captcha_code(self):
        """
        :return:  表单token & 验证码
        """

        result = {'_form_token': None, 'captcha_code': None, 'failReason': None}

        url = 'https://accounts.alipay.com/console/dispatch.htm?scene_code=resetQueryPwd&page_type=fullpage&site=1'
        try:
            resp = self.session.get(url, proxies=self.proxies, timeout=(6.1, 15))
            try:
                content = resp.content.decode(encoding='GBK')
            except:
                content = resp.content.decode(encoding='utf-8')

            tree = etree.HTML(content)
            _form_token = tree.xpath('//input[@name="_form_token"]/@value')

            if _form_token:
                _form_token = _form_token[0]
                result['_form_token'] = _form_token
            else:
                result['failReason'] = '_form_token未找到'
                return result

            captcha_url = tree.xpath('//img[@alt="输入验证码"]/@src')
            if captcha_url:
                captcha_url = captcha_url[0]
            else:
                result['failReason'] = '验证码url未找到'
                return result

            img_data = self.session.get(captcha_url, proxies=self.proxies, timeout=(6.1, 15)).content
            self.img_data = img_data

            # 第三方验证码接口
            img_b64 = self.img_encoder(img_data)
            if not img_b64:
                result['failReason'] = '图片无法转换为base64'
                return result
            begin = time.time()
            captcha_code = crack_captcha(img_b64)
            print('本次验证码请求耗时: 【%.2fs】' % (time.time() - begin))

            # --*-- 手动输入验证码进行测试 --*--
            # from io import BytesIO
            # from PIL import Image
            # img_like = BytesIO(img_data)
            # img = Image.open(img_like)
            # img.show()
            # captcha_code = input('请输入验证码: ')
            # --*-- 手动输入验证码进行测试end --*--

            if not captcha_code:
                result['failReason'] = '验证码识别错误'
                return result
            result['captcha_code'] = captcha_code
            return result

        except ProxyError as e:
            print('IP代理错误', e)
        except ConnectionError as e:
            print('连接错误', e)
        except (Timeout, ReadTimeout) as e:
            print('请求超时', e)
        except Exception as e:
            print('其它错误', traceback.format_exc())

        result['failReason'] = '网络请求错误'
        return result

    def get_check_result(self, _form_token, captcha_code, phone):
        """
        :param _form_token:  表单token
        :param captcha_code:  验证码
        :param phone:   手机号码
        :return: check 结果
        """
        result = {'statusCode': None, 'registerStatus': None, 'failReason': None}

        url = 'https://accounts.alipay.com/console/querypwd/logonIdInputReset.htm?site=1&page_type=fullpage&scene_code=resetQueryPwd&return_url='

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Length': '1764',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'accounts.alipay.com',
            'Origin': 'https://accounts.alipay.com',
            'Referer': 'https://accounts.alipay.com/console/querypwd/logonIdInputReset.htm?site=1&page_type=fullpage&scene_code=resetQueryPwd&return_url=',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
        }

        ua = ''
        try:
            self.driver.get(r"C:\Users\YongHu\Desktop\TMP\tt.html")
            page_source = self.driver.page_source
            ua = etree.HTML(page_source).xpath('//*[@id="UA_InputId"]/@value')[0]
        except Exception as e:
            print(e)

        data = {
            'ua': ua,
            '_form_token': _form_token,
            'logonId': phone,
            'picCheckCode': captcha_code
        }

        try:
            resp = self.session.post(url, proxies=self.proxies, headers=headers, data=data, timeout=(6.1, 15))
            content = resp.content.decode(encoding='GBK')
        except Exception as e:
            print(e)
            result['statusCode'] = -1
            result['failReason'] = '网络请求错误.'
            return result
        tree = etree.HTML(content)
        check = tree.xpath('//div[@class="ui-form-explain pt-5"]/text()')
        if check:
            check = check[0].strip()
            if check == '请输入正确的验证码':
                result['statusCode'] = -1
                result['failReason'] = '验证码识别错误'
                return result
            elif check == '该账户不存在，请重新输入':
                result['statusCode'] = 1
                result['registerStatus'] = '号码未注册'
                return result
            else:
                result['statusCode'] = -1
                result['failReason'] = '页面解析错误,未找到check标志'
                return result

        elif tree.xpath('//div[@class="ui-tipbox-content"]/h3/text()') == ['您暂时不能访问此页面，请稍后再试']:
            result['statusCode'] = -1
            result['failReason'] = '访问频率过快,IP被禁'
            del_proxies(self.proxies)
            return result

        elif tree.xpath('//div[@class="ui-tipbox-content"]/h3/text()') == ['对不起，请不要重复提交请求。 请回到原始页面重新刷新']:
            result['statusCode'] = -1
            result['failReason'] = '重复提交'
            return result

        else:
            result['statusCode'] = 0
            result['registerStatus'] = '号码已注册'
            return result

    def check(self, phone, save_img=False):
        result = {'statusCode': None, 'registerStatus': None, 'failReason': None}

        captcha_result = self.get_captcha_code()
        _form_token = captcha_result.get('_form_token')
        captcha_code = captcha_result.get('captcha_code')
        fail_reason = captcha_result.get('failReason')

        if not _form_token or not captcha_code:
            result['statusCode'] = -1
            result['failReason'] = fail_reason
            return result

        result = self.get_check_result(_form_token, captcha_code, phone)

        # --*-- 验证码图片保存 --*--
        if save_img:
            import os
            import uuid
            u = uuid.uuid1()
            folder = os.path.dirname(os.path.abspath(__file__))
            if result.get('statusCode') != -1:
                file_name = str(captcha_code) + '_' + str(u) + '.png'
                file = os.path.join(folder, 'images', file_name)
            else:
                file_name = 'error_' + str(captcha_code) + '_' + str(u) + '.png'
                file = os.path.join(folder, 'images', 'error', file_name)
                print('error captcha ... ')
            with open(file, 'wb') as f:
                f.write(self.img_data)
        # --*-- 验证码图片保存end --*--

        return result

    @staticmethod
    def img_encoder(img_data):
        try:
            img_b64 = base64.encodebytes(img_data).decode()
            return img_b64
        except Exception as e:
            print(e)
            return None


def get_proxies():
    begin = time.time()
    url = 'http://127.0.0.1:5020/ip/get/'
    # url = 'http://192.168.30.248:8080/get/'
    proxies = ''
    try:
        count = 0
        while count < 5:
            content = requests.get(url, timeout=3.1).content
            info = json.loads(content)
            proxies = json.loads(info.get('proxies', None))
            ping_url = 'https://www.alipay.com/'
            status_code = 404
            try:
                status_code = requests.get(ping_url, timeout=3.1, proxies=proxies).status_code
            except:
                print('代理请求失败')
                del_proxies(proxies)
            # status_code = 200
            if status_code == 200:
                info_logger.info(json.dumps(proxies) + 'status 200 ok')
                print("代理请求成功,耗时:【%.2fs】" % (time.time() - begin))
                return proxies
            else:
                count += 1
                info_logger.warning(json.dumps(proxies) + 'status not 200')
                del_proxies(proxies)
                continue

        info_logger.warning('try count > 5')

    except Exception as e:
        err_logger.error(str(e))
        del_proxies(proxies)
        print("代理请求失败,耗时:【%.2fs】" % (time.time() - begin))
        traceback.print_exc()
        return None


def del_proxies(proxies):
    url = 'http://127.0.0.1:5020/ip/del/'

    resp = requests.post(url, data=json.dumps(proxies))
    print('del proxies:【%s】& resp:' % proxies, resp.content)


def crack_captcha(img_b64):
    url = 'http://127.0.0.1:5010/captcha/crack/'
    data = {
        "serialNum": 'zfb001',
        "imgBase64": img_b64
    }
    content = requests.post(url, data=json.dumps(data)).content

    return json.loads(content)['captcha']


if __name__ == '__main__':
    import threading
    def tt():
        for i in range(1000):
            prc = PhoneRegisterCheck()
            res = prc.check(13017202140)
            print(res)

    def multi():
        for j in range(5):
            t = threading.Thread(target=tt)
            t.start()

    # multi()
    tt()
