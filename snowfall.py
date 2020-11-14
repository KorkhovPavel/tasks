# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

# TODO здесь ваш код
while True:
    sd.clear_screen()
    pass
    pass
    pass
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg

import simple_draw as sd

sd.resolution = (1400, 800)

x_list = [sd.random_number(100, 1000), sd.random_number(100, 1000), sd.random_number(700, 1200),
          sd.random_number(700, 1200),
          sd.random_number(100, 1000), sd.random_number(100, 1000), sd.random_number(700, 1200),
          sd.random_number(700, 1200),
          sd.random_number(100, 1000), sd.random_number(100, 1000), sd.random_number(700, 1200),
          sd.random_number(700, 1200),
          sd.random_number(100, 1000), sd.random_number(100, 1000), sd.random_number(700, 1200),
          sd.random_number(700, 1200),
          sd.random_number(100, 1000), sd.random_number(100, 1000), sd.random_number(700, 1200),
          sd.random_number(700, 1200)]
y_list = [sd.random_number(700, 1200), sd.random_number(700, 1200), sd.random_number(700, 1200),
          sd.random_number(700, 1200),
          sd.random_number(700, 1200), sd.random_number(700, 1200), sd.random_number(700, 1200),
          sd.random_number(700, 1200),
          sd.random_number(700, 1200), sd.random_number(700, 1200), sd.random_number(700, 1200),
          sd.random_number(700, 1200),
          sd.random_number(700, 1200), sd.random_number(700, 1200), sd.random_number(700, 1200),
          sd.random_number(700, 1200),
          sd.random_number(700, 1200), sd.random_number(700, 1200), sd.random_number(700, 1200),
          sd.random_number(700, 1200),
          sd.random_number(700, 1200), sd.random_number(700, 1200), sd.random_number(700, 1200),
          sd.random_number(700, 1200)]
length_list = [sd.random_number(10, 40), sd.random_number(10, 40), sd.random_number(10, 40), sd.random_number(10, 40),
               sd.random_number(10, 40), sd.random_number(10, 40), sd.random_number(10, 40), sd.random_number(10, 40),
               sd.random_number(10, 40), sd.random_number(10, 40), sd.random_number(10, 40), sd.random_number(10, 40),
               sd.random_number(10, 40), sd.random_number(10, 40), sd.random_number(10, 40), sd.random_number(10, 40),
               sd.random_number(10, 40), sd.random_number(10, 40), sd.random_number(10, 40), sd.random_number(10, 40)]


while True:
    for i in range(20):
        point = sd.get_point(x_list[i], y_list[i])
        sd.start_drawing()
        sd.snowflake(center=point, length=length_list[i], color=sd.background_color, factor_a=0.6, factor_b=0.35,
                     factor_c=60)
        y_list[i] -= 55
        x_list[i] += sd.random_number(-10, +10)
        if y_list[i] < 10:
            y_list[i] = 10

        point1 = sd.get_point(x_list[i], y_list[i])
        sd.snowflake(center=point1, length=length_list[i], color=sd.COLOR_WHITE, factor_a=0.6, factor_b=0.35,
                     factor_c=60)
        sd.finish_drawing()
        sd.sleep(0.01)  # таймаут
        if sd.user_want_exit():
            break
    # sd.clear_screen()
sd.pause()

# зачет!


