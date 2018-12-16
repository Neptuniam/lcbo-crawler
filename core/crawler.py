#!/usr/bin/env python3

import requests, bs4
from bs4 import BeautifulSoup
from base64 import b64encode

class Crawler:
    def __init__(self, url):
        self.url = url
        self.load_page(url)

    def load_page(self, url):
        # page_source = Utils.get_HTML('samples/homepage.html')
        page_source = Utils.get_HTML('samples/product_catalog.html')
        # page_source = Utils.fetch_source(self.url)
        self.soup = BeautifulSoup(page_source, 'html.parser')


    def select_one(self, select_string):
        selection = self.soup.select_one(select_string)
        if selection:
            return selection.get_text().strip()
        return selection


    def select(self, select_string):
        return self.soup.select(select_string)



class Utils:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

    def get_HTML(file):
        f = open(file, 'r')
        lines = f.readlines()
        f.close()
        return("".join(lines))


    def fetch_source(url, stream=False):
        request = requests.get(url, headers=Utils.headers, stream=stream)
        if stream:
            return b64encode(request.content)
        return(request.text)


    def bs4_traverse_children(tag):
        for child in tag.contents:
            if type(child) is bs4.element.NavigableString: continue
            yield child
