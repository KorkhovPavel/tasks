import requests
import csv
from multiprocessing import Pool

def get_text(url):
    res = requests.get(url)
    return res.text

def csv_writer(data):
    with  open('data.csv', 'a') as ff:
        headers = ['name','url','description','traffic','percent']
        writer = csv.DictWriter(ff,fieldnames=headers)
        writer.writerow(data)

def get_page_data(text):
        dataw = text.strip().split('\n')[1:]
        for line in dataw:
            line_list = line.strip().split('\t')
            name = line_list[0]
            url = line_list[1]
            description = line_list[2]
            traffic = line_list[3]
            percent = line_list[4]
            data = {'name': name,
                    'url': url,
                    'description': description,
                    'traffic': traffic,
                    'percent': percent}
            csv_writer(data)

def make_all(url):
    text = get_text(url)
    return get_page_data(text)

def main():

        url = 'https://www.liveinternet.ru/rating/ru//today.tsv?page={}'
        urls=[url.format(str(i)) for i in range(1,10)]
        with Pool(2) as p:
            p.map(make_all,urls)


if __name__ == '__main__':
    main()
