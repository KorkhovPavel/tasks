# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

# TODO здесь ваш код

sd.pause()

# -*- coding: utf-8 -*-
import simple_draw as sd

geometric_figures = {3: {0:'Треугольник'},4:{1:'Квадрат'}, 5:{2:'Пятиугольник'},6:{3:'Шестиугольник'}}
sd.set_screen_size(width=1200, height=800)


def polygon(x, y, angle_of_rotation, length, figur_number):
    point = sd.get_point(x, y)
    for _ in range(figur_number):
        angle = 360 / figur_number
        vektor = sd.get_vector(start_point=point, angle=angle_of_rotation, length=length, width=3)
        vektor.draw()
        angle_of_rotation += angle
        point = vektor.end_point


print('Geometric figures:')
for number in geometric_figures.values():
    for value,key in number.items():
        print(value,key)

while True:
    figur_number = int(input('Enter the desired shape (number):'))

    if 0 <= figur_number <= 6 :
        color = list(geometric_figures)[figur_number]
        polygon(400, 150, 0, 50, 4)
        sd.pause()
        break
    else:
        print('You entered an invalid number')
