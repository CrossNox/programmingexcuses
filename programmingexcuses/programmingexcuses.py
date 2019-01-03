import requests
from bs4 import BeautifulSoup

HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

BASE_URL = "http://programmingexcuses.com/"


def get_excuse():
    page = requests.get(BASE_URL, headers=HEADERS)
    tree = BeautifulSoup(page.content, 'html.parser')
    excuse = tree.find('div', attrs={'class': 'wrapper'}).find('a').text
    return excuse


class RandomExcuseError(Exception):
    def __init__(self):
        msg = get_excuse()
        super(RandomExcuseError, self).__init__(msg)
