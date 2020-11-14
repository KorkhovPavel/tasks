# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
from pprint import pprint

from abc import ABCMeta, abstractmethod


class LogParser(metaclass=ABCMeta):

    def __init__(self, file_name_input, file_name_output):
        self.file_name_input = file_name_input
        self.file_name_output = file_name_output
        self.val = None
        self.dict_count = {}

    @abstractmethod
    def pars(self):
        with open(self.file_name_input, 'r', encoding='cp1251') as file:
            for line in file:
                if 'NOK' in line:
                    self.val = line[0:17]
                    self.counts()


    def counts(self):
        if self.dict_count.get(self.val):
            self.dict_count[self.val] += 1
        else:
            self.dict_count[self.val] = 1

    def output(self):
        file = open(self.file_name_output, 'w', encoding='utf8')
        for k, i in self.dict_count.items():
            values = str(k) + '] ' + str(i)
            file.write(values)
            file.write('\n')
        file.close()

# logparser = LogParser('events.txt', 'out.txt')
# logparser.pars()
# logparser.output()

# class LogParserHour(LogParser):
#     def pars(self):
#         with open(self.file_name_input, 'r', encoding='cp1251') as file:
#             for line in file:
#                 if 'NOK' in line:
#                     self.val = line[0:14]
#                     self.counts()

# class LogParserHour(LogParser):
#     def pars(self):
#         with open(self.file_name_input, 'r', encoding='cp1251') as file:
#             for line in file:
#                 if 'NOK' in line:
#                     self.val = line[0:11]
#                     self.counts()

# class LogParserHour(LogParser):
#     def pars(self):
#         with open(self.file_name_input, 'r', encoding='cp1251') as file:
#             for line in file:
#                 if 'NOK' in line:
#                     self.val = line[0:8]
#                     self.counts()

# class LogParserHour(LogParser):
#     def pars(self):
#         with open(self.file_name_input, 'r', encoding='cp1251') as file:
#             for line in file:
#                 if 'NOK' in line:
#                     self.val = line[0:5]
#                     self.counts()
# logparser = LogParserHour('events.txt', 'out.txt')
# logparser.pars()
# logparser.output()