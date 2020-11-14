# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
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
# TODO Внимание! это задание можно выполнять только после зачета lesson_012/01_volatility.py !!!

# TODO тут ваш код в многопоточном стиле

import os
import threading
from datetime import time
from threading import Thread
import time


class Volatilly(Thread):

    def __init__(self, result, lock, data, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lock = lock
        self.data = data
        self.result = result

    def pars(self):
        with open(file=self.data, mode='r', encoding='utf-8') as ff:
            for st in ff:
                st = st[:-1]
                yield st

    def run(self):
        name_ticket = None
        max_price = 0
        min_price = 264232.5
        for i in self.pars():
            list_line = i.split(',')
            if list_line[0] != 'SECID':
                name_ticket = list_line[0]
                price = float(list_line[2])
                if max_price < price:
                    max_price = price
                if min_price > price:
                    min_price = price
        average_price = (max_price + min_price) / 2
        volatility = ((max_price - min_price) / average_price) * 100
        with self.lock:
            self.result.append([name_ticket, volatility])


class Sorted():
    def __init__(self, result):
        self.result = result

    def sor_print(self):
        vol_noon = []
        vol_not_noon = []
        vol_sort = sorted(self.result, key=lambda vol: vol[1])
        for i in vol_sort:
            if i[1] == 0.0:
                vol_noon.append(i[0])
            if i[1] != 0.0 and i[0] is not None:
                vol_not_noon.append(i)
        vol_noon = ','.join(vol_noon)

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
def funk():
    locks = threading.Lock()
    lst = []
    lst1 = []
    path_normalized = os.path.normpath('trades')
    for dirpath, dirnames, filenames in os.walk(path_normalized):
        for file in filenames:
            full_file_path = os.path.join(dirpath, file)
            vol1 = Volatilly(data=full_file_path, result=lst, lock=locks)
            lst1.append(vol1)

    for i in lst1:
        i.start()

    for i in lst1:
        i.join()

    sor = Sorted(result=lst)
    sor.sor_print()


funk()