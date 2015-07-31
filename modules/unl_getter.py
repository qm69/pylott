#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

user_agent = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) \
              Ubuntu Chromium/40.0.2214.111 Chrome/40.0.2214.111 Safari/537.36"
head_dict = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "ru,en-US;q=0.8,en;q=0.6,uk;q=0.4",
    "Connection": "keep-alive",
    "Content-Length": "62",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "lottery.com.ua",
    "Origin": "http://lottery.com.ua",
    "User-Agent": user_agent,
    "X-Requested-With": "XMLHttpRequest"}
link = "http://lottery.com.ua/index.php"


def get_keno(draw_num):
    resp = requests.post(
        "http://lottery.com.ua/index.php",
        headers=head_dict,
        data=dict(
            action="show_results_keno",
            module="lottery",
            is_ajax="true",
            draw=draw_num))  # .json()
    """
    del resp["result"]
    if resp["draw"] is not None:
        resp['draw'] = int(resp["draw"])
    """
    return resp.text
"""
apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers',
'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links',
'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url'
"""
# print(get_keno(4800))
