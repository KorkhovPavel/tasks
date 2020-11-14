# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

# TODO здесь ваш код
s = "1A3BCF 2BNKLOPY5T"
for i in filter( str.isdigit , s) : print(i)

class NotNameError(Exception):
    pass
    # def __str__(self):
    #     return 'ошибка в имени'


class NotEmailError(Exception):
    pass
    # def __str__(self):
    #     return 'ошибка в имейле'


with open('registrations.txt', 'r') as ff:
    for line in ff:
        line = line[:-1]
        list_line = line.split(' ')
        try:
            if len(list_line) == 3 and list_line[0].isalpha() and list_line[1].find("@") and list_line[1].find(".") and \
                    9 < int(list_line[2]) < 100:
                file = open('registrations_good.log', 'a', encoding='utf8')
                file.write(line)
                file.write('\n')
                file.close()
            elif len(list_line) != 3:
                raise ValueError(f'НЕ присутсвуют все три поля, строка {list_line}')
            elif not list_line[0].isalpha():
                raise NotNameError(f'поле имени содержит НЕ только буквы {list_line}')
            elif int != list_line[1].find("@") and int != list_line[1].find("."):
                raise NotEmailError(f'поле емейл НЕ содержит @ и .(точку) {list_line}')
            elif 9 > int(list_line[2]) > 100:
                raise ValueError(f'поле возраст НЕ является числом от 10 до 99 {list_line}')

        except (ValueError, NotNameError, NotEmailError, IndexError) as exc:
            file = open('registrations_bad.log', 'a', encoding='utf8')
            print(values := f'Поймано исключение {exc}')
            file.write(line + "  " + values)
            file.write('\n')
            file.close()
