# -*- coding: utf-8 -*-


# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от средней цены за торговую сессию:
#   средняя цена = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / средняя цена) * 100%
# Например для бумаги №1:
#   average_price = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / average_price) * 100 = 8.7%
# Для бумаги №2:
#   average_price = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / average_price) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base_source/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас
#
# class <Название класса>:
#
#     def __init__(self, <параметры>):
#         <сохранение параметров>
#
#     def run(self):
#         <обработка данных>

# TODO написать код в однопоточном/однопроцессорном стиле
import os
import time


class Volatilly:

    def __init__(self, data):
        self.data = data
        self.result = []

    def pars(self):
        path_normalized = os.path.normpath(self.data)
        for dirpath, dirnames, filenames in os.walk(path_normalized):
            for file in filenames:
                full_file_path = os.path.join(dirpath, file)
                with open(file=full_file_path, mode='r', encoding='utf-8') as ff:
                    for st in ff:
                        st = st[:-1]
                        yield st

    def run(self):
        name_ticket = None
        max_price = 0
        min_price = 264232.5
        for i in self.pars():
            list_line = i.split(',')
            if name_ticket != list_line[0] and list_line[0] != 'SECID':
                average_price = (max_price + min_price) / 2
                volatility = ((max_price - min_price) / average_price) * 100
                self.result.append([name_ticket, volatility])
                max_price = 0
                min_price = 264232.5
            if list_line[0] != 'SECID':
                name_ticket = list_line[0]
                price = float(list_line[2])
                if max_price < price:
                    max_price = price
                if min_price > price:
                    min_price = price

    def sor_print(self):
        self.run()
        vol_noon = []
        vol_not_noon = []
        vol_sort = sorted(self.result, key=lambda vol: vol[1])
        for i in vol_sort:
            if i[1] == 0.0:
                vol_noon.append(i[0])
            if i[1] != 0.0 and i[0] != None:
                vol_not_noon.append(i)
        vol_noon = ','.join(vol_noon)
        vol_sort.clear()

        print(
            f'Максимальная волатильность:\nТИКЕР1 - {vol_not_noon[-1]} %\nТИКЕР2 - {vol_not_noon[-2]} %\nТИКЕР3 - {vol_not_noon[-3]} %\n'
            f'Минимальная волатильность:\nТИКЕР4 - {vol_not_noon[2]} %\nТИКЕР5 - {vol_not_noon[1]} %\nТИКЕР6 - {vol_not_noon[0]} %\n'
            f'Нулевая волатильность:\n{vol_noon}')


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 6)
        print(f'Функция {func.__name__} работала {elapsed} секунд(ы)', )
        return result

    return surrogate


@time_track
def funk(data):
    vol = Volatilly(data='trades')
    vol.sor_print()


funk(data='trades')
