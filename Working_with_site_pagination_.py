import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
    resp = requests.get(url)
    if resp.ok:
        return resp.text
    print(resp.status_code)

def csv_writer(data):
    with open('data.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow((data['name_csv'],
                         data['url_csv'],
                         data['price_csv']))

def price_norma(price):
    price_norm = price[1:]
    return price_norm.replace(',','')

def get_page_data(html):
    soup = BeautifulSoup(html,'lxml')
    tr_all = soup.find_all('tr',class_="rc-table-row rc-table-row-level-0 cmc-table-row")
    for tr in tr_all:
        try:
            name_csv = tr.find('div',class_="Box-sc-16r8icm-0 CoinItem__NameArea-sc-1teo54s-1 NqdZD").find('p').text
        except:
            name_csv = ''
        try:
            url_csv = 'https://coinmarketcap.com' + tr.find('a').get('href')
        except:
            url_csv = ''
        try:
            price = tr.find('td', class_="rc-table-cell font_weight_500___2Lmmi").text
            price_csv = price_norma(price)
        except:
            price_csv = ''
        data = {
            'name_csv':name_csv,
            'url_csv': url_csv,
            'price_csv':price_csv
        }
        csv_writer(data)

def main():

    li = "false"
    count = 1
    while li == "false":
        url = f'https://coinmarketcap.com/{count}'
        all_html = get_html(url)
        get_page_data(all_html)
        soup = BeautifulSoup(all_html,'lxml')
        li = soup.find('li',title="下一页").get('aria-disabled')
        count+=1

if __name__ == '__main__':
    main()
