import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import requests
from bs4 import BeautifulSoup

search = '송파 헬리오시티'
url = 'https://search.daum.net/search?q={}'.format(search)
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
res = requests.get(url=url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
result = soup.findAll('ul', attrs={'class' : 'list_keyword'})
for r in result[1] :
    print(r.text)