# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
import zipfile
from abc import ABCMeta, abstractmethod

class Char_stat(metaclass=ABCMeta):

    def __init__(self,file_start):
        self.dict_letter = {}
        self.file_start=file_start

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_start, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_start = filename

    def counters(self):
        if self.file_start.endswith('.zip'):
            self.unzip()
        with open(self.file_start, 'r', encoding='cp1251') as files:
            for line in files:
                line1 = [i for i in line if i.isalpha() == True]
                for char in line1:
                    if char in self.dict_letter.keys():
                        self.dict_letter[char] += 1
                    else:
                        self.dict_letter[char] = 1

    @abstractmethod
    def sorted_let_num(self):
        self.list_d = list(self.dict_letter.items())
        self.list_d.sort(key=lambda i: i[1], reverse=True)

    def save_file(self):
        file_w = open('out_file_name.txt', 'w', encoding='utf8')
        print_start = f'|  БУКВА |  ЧАСТОТА  |'
        print_start_1 = f'+--------------------+'
        separator = '\n'
        file_w.write(print_start_1+separator+print_start+separator+print_start_1+separator)
        counter = 0
        for k, r in self.list_d:
            counter += r
            values = f'|    {k}   |  {r:6}   |'
            file_w.write(values)
            file_w.write('\n')
        values_fin = f'|  Итого |  {counter:6}  |'
        file_w.write(print_start_1+separator+values_fin+separator+print_start_1+separator)
        file_w.close()


# book_1=Char_stat(file_start='voyna-i-mir.txt.zip')
# book_1.counters()
# book_1.sorted_let_num()
# book_1.save_file()

# class Po_chastote_po_vozrastaniyu(Char_stat):
#     def sorted_let_num(self):
#         self.list_d = list(self.dict_letter.items())
#         self.list_d.sort(key=lambda i: i[1])
#
# book_1=Po_chastote_po_vozrastaniyu(file_start='voyna-i-mir.txt.zip')
# book_1.counters()
# book_1.sorted_let_num()
# book_1.save_file()

# class Po_chastote_po_vozrastaniyu(Char_stat):
#     def sorted_let_num(self):
#         self.list_d = list(self.dict_letter.items())
#         self.list_d.sort()
#
# book_1=Po_chastote_po_vozrastaniyu(file_start='voyna-i-mir.txt.zip')
# book_1.counters()
# book_1.sorted_let_num()
# book_1.save_file()

# class Po_chastote_po_vozrastaniyu(Char_stat):
#     def sorted_let_num(self):
#         self.list_d = list(self.dict_letter.items())
#         self.list_d.sort(reverse=True)
#
# book_1=Po_chastote_po_vozrastaniyu(file_start='voyna-i-mir.txt.zip')
# book_1.counters()
# book_1.sorted_let_num()
# book_1.save_file()