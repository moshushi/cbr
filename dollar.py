#!venv/bin/python
#-*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import os


URL = "http://cbr.ru"

def fetch_cbr(url):
    r = requests.get(url)
    return r.text


def parse_dollar_rate(html):
    soup = BeautifulSoup(html, 'html.parser')
    t = soup.find('ins', text='$').find_parent('tr').find_all('td')[-1].text
    result = t.split('\xa0')[-1][1:]
    return result


def send_message(message):
    TITLE = 'Доллар США'
    os.system('notify-send "{}" "{}"'.format(TITLE, message))


def main():
    rate = parse_dollar_rate(fetch_cbr(URL))
    send_message(rate)


if __name__ == '__main__':
    main()
