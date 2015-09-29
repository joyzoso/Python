__author__ = 'joy'

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin



URL = 'https://portland.craigslist.org/search/eng?sort=rel&query=jobs'
BASE = 'http://portland.craigslist.org/cpg/'
response = requests.get(URL)

soup = BeautifulSoup(response.content)
for listing in soup.find_all('p',{'class':'row'}):
    if listing.find('span',{'class':'pl'}) != None:
        job = listing.text[2:6]
        job = str('developer')
        print (job)
        link_end = listing.a['href']
        url = urljoin(BASE, link_end)
        print (url)
        print ("\n")
