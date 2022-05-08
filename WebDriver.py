import json
from time import sleep

from bs4 import BeautifulSoup

import requests as requests
from selenium import webdriver


class WebDriver:
    def __init__(self):
        self.word = ""
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("javascript.enabled")
        self.driver = webdriver.Chrome(options=self.options)
        self.baseurl = "https://twitter.com/search?f=live&q="

    def setWord(self, word):
        self.word = word

    def getlinks(self):
        links = []
        self.driver.get(self.baseurl + self.word)
        page_data = self.driver.page_source
        sleep(2)
        soup = BeautifulSoup(page_data)
        html_link = soup.find_all('a')
        for link in html_link:
            if len(link['href'].split('/')) == 3:
                links.append(link['href'])
        sleep(2)


    def getlinkContent(self, url):
        pre_url = 'https://publish.twitter.com/oembed?url='
        rq = requests.get(pre_url + url)
        html = rq.content
        ss = json.loads(html)
        tx = str(ss['html']).replace('<br>', '\n')
        soup = BeautifulSoup(tx, 'html.parser')
        name = ss['author_name']

        text = soup.get_text()
        text = text.replace('#', ' #')
        return name, text
