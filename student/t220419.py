import json
import ipaddress
import httpx
from lxml import etree

s = '[{"port": 80, "score": 150.549, "update_time": 1652509227.0, "anonymous": 1, "download_speed_average": 56917.2, "response_time_average": 6.10687, "country_code": "US", "ip": "162.214.202.170", "working_average": 87.8431, "country_name": "United States"}]'


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


def demo(s):
    infos = json.loads(s)
    items = []
    for info in infos:
        try:
            ip = info.get('ip')
            port = info.get('port')
            if not proxy_check(ip, port):
                continue
            items.append(f'http://{ip}:{port}')
            items.append(f'https://{ip}:{port}')
        except Exception as ex:  # pylint: disable=broad-except
            print('Parse info error %s.%s' % ex, info)
    return items


def parse(rows_rule, row_start, row_end):
    url = 'http://www.66ip.cn/'
    response = httpx.get(url)
    html = etree.HTML(response.text)
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


def parse_row(row) -> list[str] | None:
    """
    parse a row
    :param row:
    :return: 127.0.0.1:1080 / ''
    """
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
    # I'm not sure if it's going to cause anything else.
    # But I want to avoid a problem that could cause a program to fail
    except Exception as ex:  # pylint: disable=broad-except
        print('Parse row error %s. \n%s', ex, row_html)
    return None


print(parse('//tr', 1, None))
# print(demo(s))
