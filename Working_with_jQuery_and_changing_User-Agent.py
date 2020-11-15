import requests
import csv
from bs4 import BeautifulSoup


def get_html(url):
    user_agent = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    res = requests.get(url, headers=user_agent)
    return res.text


def csv_writer(data):
    with open('data.csv', 'a') as ff:
        headers = ['author', 'with_years']
        writer = csv.DictWriter(ff, headers)
        writer.writerow(data)


def get_article_data(html):
    soup = BeautifulSoup(html, 'lxml')
    ts = soup.find('div', class_="module module-testimonial testimonial-2364-3-0-0 testimonial-container").find_all(
        'article')
    return ts


def get_page_data(ts):
    for t in ts:
        try:
            with_years = t.find('p', class_="traxer-since").text.strip()
        except:
            with_years = ''
        try:
            author = t.find('p', class_="testimonial-author").text.strip()
        except:
            author = ''
        dict_data = {
            'author': author,
            'with_years': with_years
        }
        csv_writer(dict_data)


def main():
    count = 1
    while True:
        url = f'https://catertrax.com/why-catertrax/traxers/page/{str(count)}'
        html = get_html(url)
        counter = get_article_data(html)
        if counter:
            get_page_data(counter)
            count += 1
        else:
            break


if __name__ == '__main__':
    main()
