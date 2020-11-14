# -*- coding: utf-8 -*-

import os, time, shutil

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk обходит дерево каталогов и возвращает генератор кортежей, каждый из которых содержит имя каталога, списки вложенных каталогов
#   os.path.dirname- возвращает имя директории пути path.
#   os.path.join- соединяет пути с учётом особенностей операционной системы.
#   os.path.normpath - нормализует путь, убирая избыточные разделители и ссылки на предыдущие директории. На Windows преобразует прямые слеши в обратные.
#   os.path.getmtime  время последнего изменения файла, в секундах
#   time.gmtime  преобразует время, выраженное в секундах с начала эпохи в struct_time, где DST флаг всегда равен нулю.
#   os.makedirs - создаёт директорию, создавая при этом промежуточные директории.
#   shutil.copy2 - но пытается копировать все метаданные.
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
import zipfile
from abc import ABCMeta, abstractmethod


class Files_arrange(metaclass=ABCMeta):
    def __init__(self, path, path_finish):
        self.path = path
        self.list_dirpath = []
        self.path_finish = path_finish


    @abstractmethod
    def getting_directories_and_creation_time_of_files(self):
        self.path_norm = os.path.normpath(self.path)
        for dirpath, dirnames, filenames in os.walk(self.path_norm):
            for file in filenames:
                self.file_path = os.path.join(dirpath, file)
                secs = os.path.getmtime(self.file_path)
                self.time_file = time.gmtime(secs)
                self.creating_folders_and_copying_files()

    def creating_folders_and_copying_files(self):
        path_1 = f'{self.path_finish}/{self.time_file[0]}/{self.time_file[1]}/{self.time_file[2]}'
        if path_1 in self.list_dirpath:
            shutil.copy2(self.file_path, path_1)
        else:
            os.makedirs(path_1)
            self.list_dirpath.append(path_1)
            shutil.copy2(self.file_path, path_1)


# f1 = Files_arrange(path='icons', path_finish='icons_by_year')
# f1.getting_directories_and_creation_time_of_files()

class Files_arrange_zip(Files_arrange):

    def unzip(self):
        path = self.path
        patht = os.path.dirname(path)
        f = zipfile.ZipFile(path, 'r')
        for file in f.infolist():
            d = file.date_time
            gettime = "%s/%s/%s %s:%s" % (d[0], d[1], d[2], d[3], d[4])
            f.extract(file, patht)
            filep = os.path.join(patht, file.filename)
            timearry = time.mktime(time.strptime(gettime, '%Y/%m/%d %H:%M'))
            os.utime(filep, (timearry, timearry))
        self.path=(str(self.path))[:-4]

    def getting_directories_and_creation_time_of_files(self):
        if self.path.endswith('.zip'):
            self.unzip()
        self.path_norm = os.path.normpath(self.path)
        for dirpath, dirnames, filenames in os.walk(self.path_norm):
            for file in filenames:
                self.file_path = os.path.join(dirpath, file)
                secs = os.path.getmtime(self.file_path)
                self.time_file = time.gmtime(secs)
                self.creating_folders_and_copying_files()


f1 = Files_arrange_zip(path='icons.zip', path_finish='icons_by_year')
f1.getting_directories_and_creation_time_of_files()
