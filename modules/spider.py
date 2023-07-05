from bs4 import BeautifulSoup
from lxml import etree
import requests


class Spider:
    def __init__(self, url) -> None:
        if t := (type(url)) != str:
            raise Exception(f'URL should be a string, but got {t}')
        self.url = url
        self.html_parse = None
        self.__set_html_parse()

    def __set_html_parse(self):
        request = requests.get(self.url)
        state = request.status_code

        if state != 200:
            print('Something Wrong')
            return

        self.html_parse = BeautifulSoup(request.text, 'html.parser')

    def get_title(self):
        title = self.html_parse.find_all('title')[0].text
        return title[:title.rfind('-')].strip()

    def get_eye(self):
        if self.html_parse is None:
            raise Exception('not html parse yet')
        return int(self.html_parse.find_all('span', class_='ui-viewcount')[0].text)

    def get_heart(self):
        if self.html_parse is None:
            raise Exception('not html parse yet')
        t = self.html_parse.find_all('span', class_='count')[0].text
        try:
            return int(t)
        except:
            return 0
