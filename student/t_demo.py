import ipaddress

from bs4 import BeautifulSoup

with open(r"D:\github\work_submit\crawlerstack-proxypool\tests\common\mock_fixture.html", 'r', encoding='utf-8') as f:
    lines = f.read()
    print(lines)


def proxy_check(ip_address: str, port: int) -> bool:
    """
    check whether the proxy ip and port are valid
    :param ip_address: proxy ip value
    :param port: proxy port value
    :return: True or False
    """
    try:
        ipaddress.ip_address(ip_address)
        _port = int(port)
        if _port > 65535 or _port <= 0:
            raise ValueError(f'Invalid port {port}')
    except ValueError:
        return False
    return True


# def test_proxy_check():
#     """Test proxy check"""
#     assert proxy_check('127.0.0.1', 8080)
#     assert not proxy_check('127.0.0.1', 808080)


text = 'ABCDEFG'


def check_keywords(text):
    checked = []
    keywords = ['A']
    for k in keywords:
        if k in text:
            checked.append(True)
        else:
            checked.append(False)
    return all(checked)


def a():
    with open(r"D:\github\work_submit\crawlerstack-proxypool\tests\common\mock_fixture.html", 'r',
              encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        return soup


import pytest


class Fruit:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name



'''
    def parse():
        html = etree.parse("mock_fixture.html", etree.HTMLParser())
        result = etree.tostring(html)
        response_text = result.decode('utf-8')
        html = etree.HTML(response_text)
        items = []
        rows = html.xpath(rows_rule)[row_start:]
        if row_end is not None:
            rows = rows[:row_end]
        for row in rows:
            row_html = etree.tostring(row).decode()
            if '透明' in row_html or 'transparent' in row_html.lower():
                continue
            proxy_ip = parse_row(row=row)
            if proxy_ip:
                items.extend(proxy_ip)
        return items

    def parse_row(row: Element):
        row_html = etree.tostring(row).decode()
        try:
            proxy_ip = ''
            if columns_rule:
                columns = row.xpath(columns_rule)
                if columns:
                    _ip = columns[ip_position]
                    proxy_ip = _ip.text
                    if ip_rule:
                        proxy_ip = _ip.xpath(ip_rule)[0]
                    if port_position:
                        port = columns[port_position]
                        port_str = port.text
                        if port_rule:
                            port_str = port.xpath(port_rule)[0]
                        proxy_ip = f'{proxy_ip}:{port_str}'
            else:
                proxy_ip = row_html
            if proxy_ip and proxy_check(*proxy_ip.split(':')):
                return [
                    f'http://{proxy_ip}',
                    f'https://{proxy_ip}'
                ]
        except Exception as ex:
            logging.debug('Parse row error %s. \n%s', ex, row_html)
        return None
'''
