#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  @desc:
  @author: dvvd8899
  @contact: dvvd8899@gmail.com
"""

import requests
from lxml import html


#get main page list
def getPage():
    baseUrl = 'https://www.beeg.com/'
    selector = html.fromstring(requests.get(baseUrl).content)

    urls = []
    for i in selector.xpath('//ul[@id="pins"]/li/a/@href'):
        urls.append(i)
    return

if __name__ == '__main__'
    urls = getPage()
    for url in urls:
        print(url)

