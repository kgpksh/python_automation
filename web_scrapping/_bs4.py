import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import requests
from bs4 import BeautifulSoup

url = 'https://www.naver.com/'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
res = requests.get(url=url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
print(soup.title)
print(soup.title.get_text())
print(soup.a)
print(soup.a.attrs)
print(soup.a['href'])