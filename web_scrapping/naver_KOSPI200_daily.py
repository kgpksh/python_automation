from bs4 import BeautifulSoup
import requests
import csv
from urllib.parse import urlparse, parse_qs
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

fileName = '시가총액 1-200.csv'
f = open(fileName, 'w', encoding='utf-8-sig', newline='')
writer = csv.writer(f)
writer.writerow(['날짜', '체결가', '전일비', '등락률', '거래량(천주)', '거래대금(백만)'])

url = 'https://finance.naver.com/sise/sise_index_day.naver?code=KPI200'
res = requests.get(url)
res.raise_for_status()
bs = BeautifulSoup(res.text, 'lxml')

def last_page() :
    url = bs.find('td', attrs=('class', 'pgRR')).find('a').attrs['href']
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    page_value = query_params.get('page', [''])[0]
    return int(page_value)

def checkContainingInList(targets, lst) :
    for l in lst :
        for t in targets :
            if t in l :
                return True
    return False

for i in range(1, int(last_page()) + 1) :
    res = requests.get(url + '&page={}'.format(i))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    result = soup.find('table', attrs={'class' : 'type_1'}).findChildren('tr')

    for row_idx in range (1, len(result)) :
        tmp = result[row_idx]
        if not tmp.find() or any(
                                td.get('class') 
                                and checkContainingInList(['division_line', 'blank'], td.get('class'))
                                for td in tmp.find_all('td')) :
            continue

        singleRow = tmp.find_all('td')
        try :
            data = [singleRow[0].text, singleRow[1].text, singleRow[2].find('span').text.replace('\t', '').replace('\n', ''), singleRow[3].find('span').text.replace('\t', '').replace('\n', ''), singleRow[4].text, singleRow[5].text] 
            if float(data[3][0:-1]) < 0 :
                data[2] = '-' + data[2]
            writer.writerow(data)
        except :
            pass