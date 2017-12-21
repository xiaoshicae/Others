import copy
import base64
import json
import logging
import traceback
from io import BytesIO
from requests_toolbelt import SSLAdapter

import requests
from PIL import Image
# requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':RC4-SHA'
from lxml import etree
from requests.exceptions import Timeout, ReadTimeout, ProxyError, ConnectionError
# from requests.packages.urllib3.exceptions import InsecureRequestWarning

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType

from tm import get_proxies3

# 禁用安全请求警告
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
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

    def __init__(self):
        """
            初始化session, 获取IP代理
        """

        self.session = requests.Session()
        # proxy = get_proxies3()
        # self.proxies = {
        #     'http': 'http://%s' % proxy,
        #     'https': 'http://%s' % proxy
        # }
        "{'http': 'http://115.212.126.201:4399', 'https': 'http://115.212.126.201:4399'}"
        proxy = '49.71.107.134:43281212'
        self.proxies = {'http': 'http://49.71.107.134:4328', 'https': 'http://49.71.107.134:4328'}

        self.cookies = {}
        self.img_data = b''
        proxy2 = Proxy(
            {
                'proxyType': ProxyType.MANUAL,
                'httpProxy': proxy,  # 代理ip和端口
                'sslProxy': proxy,
                'ftpProxy': proxy,
                'noProxy': ''
            }
        )
        # 新建一个“期望技能”,
        desired_capabilities = DesiredCapabilities.CHROME.copy()
        proxy2.add_to_capabilities(desired_capabilities)

        self.driver = webdriver.Chrome(
            executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',
            desired_capabilities=desired_capabilities
            # proxy=proxy
        )
        self.driver.delete_all_cookies()
        # 新建一个会话，并把技能传入
        # self.driver.start_session(desired_capabilities)
        self.driver.maximize_window()

    def get_captcha_code(self):
        """
        获取验证码 & 表单token
        """

        result = {'ua': None, '_form_token': None, 'captcha_code': None, 'failReason': None}

        url = 'https://accounts.alipay.com/console/querypwd/logonIdInputReset.htm?site=1&page_type=fullpage&scene_code=resetQueryPwd'
        try:
            # 获取验证码url & 表单token
            self.driver.get(url)
            cookies = self.driver.get_cookies()

            for item in cookies:
                self.cookies[item['name']] = item['value']
            # print(self.cookies)
            page_source = self.driver.page_source
            content = page_source

            tree = etree.HTML(content)
            _form_token = tree.xpath('//input[@name="_form_token"]/@value')

            if _form_token:
                _form_token = _form_token[0]
                result['_form_token'] = _form_token
            else:
                result['failReason'] = '_form_token未找到'
                return result

            ua = tree.xpath('//*[@id="UA_InputId"]/@value')
            if ua:
                ua = ua[0]
                result['ua'] = ua
            else:
                result['failReason'] = 'ua未找到'
                return result

            # 获取验证码data
            captcha_element = self.driver.find_elements_by_xpath('//img[@title="点击图片刷新验证码"]')[0]
            location = captcha_element.location
            size = captcha_element.size
            left = int(location['x'])
            top = int(location['y'])
            right = left + int(size['width'])
            bottom = top + int(size['height'])

            screen_shot = self.driver.get_screenshot_as_png()

            screen_shot = Image.open(BytesIO(screen_shot))
            im = screen_shot.crop((left, top, right, bottom))

            img_byte_io = BytesIO()
            im.save(img_byte_io, format='png')
            img_data = img_byte_io.getvalue()

            # 第三方验证码接口
            img_b64 = self.img_encoder(img_data)
            if not img_b64:
                result['failReason'] = '图片无法转换为base64'
                return result

            captcha_code = crack_captcha(img_b64)

            if not captcha_code:
                result['failReason'] = '验证码识别错误'
                return result

            result['captcha_code'] = captcha_code
            return result

        except (ProxyError, ConnectionError, Timeout, ReadTimeout) as e:
            print('IP代理错误', e)
            traceback.format_exc()
        except Exception as e:
            err_logger.error('网络请求错误(其它):【%s】' % str(e))
            print('其它错误', traceback.format_exc())

        result['failReason'] = '网络请求错误'
        return result

    def get_check_result(self, ua, _form_token, captcha_code, phone):
        """
        传入ua, _form_token, captcha_code, phone等参数,获取验证信息
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
        # ua = '189BqFYKOYNNcUuXukRErVNJIN+ErdLIZYCAw==|BaFEKYlxHrxGL49+F7tAKeE=|BKNGQfZ8SK8JOMgjU+Qbd8AlW5k5C/pcd5F6e7M=|A6dcLJtqBKBQaZ02WPoGPsowD6JaPsoyXv5SO51hC6gDOZgyDK5QPpg1WPoAacpnA6JfZpA4V6ZcOZhmWKlXbZprBfUKEd4nS/xo|AqZWJugSYsU4XfsecMkiXusAAck=|AaxJN4AU|AKxJN4AU|D6tTI+0GMtNuQu0LeNwnTPcOfNk+U/wAbMkwQ7EdNf9DfsQ1W/8PNsJpB6VZYZVvUP0FYZVtAaENZMI+VPdcZsdtU/EPYcdqB6VfNpU4XP0AOc9nCPkDZsc5B/YIMsU0WqpVToF4FKNGOI8bGg==|DqhNSvIIZsM6Vu8LZMM6VvMWc9QkVPkIbNUtSO8WZsI7X/ofct4lSfAIZMU8PfU=|DaxVOYB5Ca5LJod/D6lVPod7HqdZMIlxHL1YNf0='
        # ua = get_ua()
        data = {
            'ua': ua,
            '_form_token': _form_token,
            'logonId': phone,
            'picCheckCode': captcha_code
        }
        # self.session.headers.update(headers)
        try:
            # 最终验证信息
            account_input = self.driver.find_element_by_id('J-accName')
            captcha_input = self.driver.find_element_by_id('J-checkcode')
            account_input.send_keys(phone)
            captcha_input.send_keys(captcha_code)

            submit_input = self.driver.find_element_by_xpath('//input[@type="submit"]')
            submit_input.click()

            import time
            time.sleep(2)
            content = self.driver.page_source
            # resp = requests.post(url, data=data, proxies=self.proxies, cookies=self.cookies, headers=headers, timeout=(3.1, 15))
            # content = resp.content.decode(encoding='GBK')
        except Exception as e:
            result['statusCode'] = -1
            result['failReason'] = '网络请求错误.'
            print('IP代理请求错误', e)
            return result

        tree = etree.HTML(content)
        check = tree.xpath('//div[@class="ui-form-explain pt-5"]/text()')

        if check:
            check = check[0].strip()

            if check == '请输入正确的验证码':
                result['statusCode'] = -1
                result['failReason'] = '验证码识别错误'

            elif check == '该账户不存在，请重新输入':
                result['statusCode'] = 1
                result['registerStatus'] = '号码未注册'

            else:
                result['statusCode'] = -1
                result['failReason'] = 'check出现未知字符'
                err_logger.error('check 出现未知字符:【%s】' % check)

        elif tree.xpath('//div[@class="ui-tipbox-content"]/h3/text()') == ['您暂时不能访问此页面，请稍后再试']:
            result['statusCode'] = -1
            result['failReason'] = '代理IP被禁'
            # del_proxies(self.proxies)

        elif tree.xpath('//div[@class="ui-tipbox-content"]/h3/text()') == ['对不起，请不要重复提交请求。 请回到原始页面重新刷新']:
            result['statusCode'] = -1
            result['failReason'] = '重复提交'

        elif tree.xpath('//div[@class="container"]/div[@class="content"]/p[@class="ft-14"]/text()') == ['你正在为账户 ',
                                                                                                        ' 重置登录密码，请选择重置方式：']:
            result['statusCode'] = 0
            result['registerStatus'] = '号码已注册'

        else:
            result['statusCode'] = -1
            result['failReason'] = '解析页面有误'
            err_logger.error('页面解析错误,content为:【%s】' % content)

        return result

    def main(self, phone, save_img=False):
        result = {'statusCode': None, 'registerStatus': None, 'failReason': None}
        self.driver.get('http://blog.csdn.net/after_you/article/details/69945550')
        print(self.driver.page_source)
        # 获取并破解验证码
        captcha_result = self.get_captcha_code()
        _form_token = captcha_result.get('_form_token')
        ua = captcha_result.get('ua')
        captcha_code = captcha_result.get('captcha_code')
        fail_reason = captcha_result.get('failReason')

        if not _form_token or not captcha_code:
            result['statusCode'] = -1
            result['failReason'] = fail_reason
            self.driver.close()
            return result

        # 传入ua, _form_token, captcha_code, phone等参数,获取验证信息
        result = self.get_check_result(ua, _form_token, captcha_code, phone)

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
            with open(file, 'wb') as f:
                f.write(self.img_data)
        # --*-- 验证码图片保存end --*--
        self.driver.close()
        return result

    @staticmethod
    def img_encoder(img_data):
        try:
            img_b64 = base64.encodebytes(img_data).decode()
            return img_b64
        except Exception as e:
            err_logger.error('图片base64编码错误【%s】' % str(e))


def get_proxies():
    url = 'http://127.0.0.1:5020/ip/get/'
    proxies = ''
    count = 0
    while count < 5:
        try:
            content = requests.get(url, timeout=3.1).content
            info = json.loads(content)
            proxies = json.loads(info.get('proxies', None))
            ping_url = 'https://www.alipay.com/'
            status_code = requests.get(ping_url, timeout=3.1, proxies=proxies).status_code
            if status_code == 200:
                info_logger.info(json.dumps(proxies) + 'status 200 ok')
                return proxies
            else:
                count += 1
                err_logger.error(json.dumps(proxies) + 'status not 200')
                # del_proxies(proxies)

        except Exception as e:
            count += 1
            # del_proxies(proxies)
            err_logger.error('代理连接测试失败, ' + str(e))

    info_logger.error('请求代理次数大于5次')


# def del_proxies(proxies):
#     url = 'http://127.0.0.1:5020/ip/del/'
#     resp = requests.post(url, data=json.dumps(proxies))
#     return resp


def crack_captcha(img_b64):
    url = 'http://127.0.0.1:5010/captcha/crack/'
    data = {
        "serialNum": 'zfb001',
        "imgBase64": img_b64
    }
    content = requests.post(url, data=json.dumps(data)).content
    return json.loads(content)['captcha']


def get_ua():
    import redis
    conn = redis.Redis(host='localhost', port=6379, db=3)
    ua = conn.keys()
    if not ua:
        err_logger.error("redis无可用UA")
        return
    ua = conn.randomkey()
    conn.delete(ua)
    return ua.decode()


if __name__ == '__main__':

    def tt():
        right = 0
        for i in range(1, 10000):
            prc = PhoneRegisterCheck()
            # res = prc.main(13017202140)
            res = prc.main(13568838680)
            s = res.get('statusCode')
            if s != -1:
                right += 1

            print(res)
            print('第【%d】次, 成功率为:【%.2f%%】' % (i, (right / i * 100)))


    tt()
