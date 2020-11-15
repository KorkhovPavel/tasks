import requests
import csv
from peewee import *


# db = PostgresqlDatabase(database='database', user='user',password='password',host='host' )

# class Coin(Model):
#     name = TextField()
#     url = TextField()
#     description = TextField()
#     traffic = TextField()
#     percent = TextField()
#
#     class Meta:
#         database = db


def get_text(url):
    res = requests.get(url)
    return res.text

def csv_writer(data):
    with open('data.csv', 'a') as ff:
        headers = ['name', 'url', 'description', 'traffic', 'percent']
        writer = csv.DictWriter(ff,fieldnames=headers)
        writer.writerow(data)

def main():
    # db.connect()
    # db.create_tables([Coin])
    for i in range(0,10):
        url = f'https://www.liveinternet.ru/rating/ru//today.tsv?page={str(i)}'
        resp_data = get_text(url)
        dataw = resp_data.strip().split('\n')[1:]
        # в cvs
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

        # в db
        #     coin = Coin(name = data['name'], url=data['url'], percent = data['percent'], traffic = data['traffic'], description=data['description'])
        #     coin.save()

if __name__ == '__main__':
    main()
