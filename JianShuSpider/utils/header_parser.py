import pprint


def header_parser(header):
    lines = header.split('\n')
    header_dict = {}
    for line in lines:
        line = line.strip()
        if line:
            k, v = line.split(': ', 1)
            header_dict[k] = v
    return header_dict


def main():
    header_string = """
    Host: www.jianshu.com
    Connection: keep-alive
    Content-Length: 0
    Accept: application/json
    Origin: https://www.jianshu.com
    X-CSRF-Token: qwU7K3IFq+zu56eDz2vGy0rW7clBGWGGIMrg7ezidwH0OZFPTu8jjmbfagxlruO2VAx7ORUOMQVYxOB1C6AHKw==
    User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36
    Referer: https://www.jianshu.com/search?q=%E6%97%85%E8%A1%8C%E9%9D%92%E8%9B%99&page=1&type=note
    Accept-Encoding: gzip, deflate, br
    Accept-Language: zh-CN,zh;q=0.9
    Cookie: remember_user_token=W1s3MzQ1MDIzXSwiJDJhJDEwJGY0UjV6TExLczZIVXVFV3VDaVlqaU8iLCIxNTE2OTM3NDE3LjIzMjA1NzYiXQ%3D%3D--110dc84d34b53ad69d27d2255464f3d1f8e2463d; read_mode=day; default_font=font2; locale=zh-CN; _m7e_session=9e30ec7ba5252443a66f13487fc5ddc3; Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1517385521,1517406920,1517446551,1517446591; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%227345023%22%2C%22%24device_id%22%3A%221613083ab8cab-0517b183f72795-3c60460e-1247616-1613083ab8d372%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22desktop%22%2C%22%24latest_utm_medium%22%3A%22search-trending%22%7D%2C%22first_id%22%3A%221613083ab8cab-0517b183f72795-3c60460e-1247616-1613083ab8d372%22%7D; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1517455695
    """
    res = header_parser(header_string)
    pprint.pprint(res)


if __name__ == '__main__':
    main()