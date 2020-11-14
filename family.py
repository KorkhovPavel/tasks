# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        pass


class Husband:

    def __init__(self):
        pass

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def eat(self):
        pass

    def work(self):
        pass

    def gaming(self):
        pass


class Wife:

    def __init__(self):
        pass

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def eat(self):
        pass

    def shopping(self):
        pass

    def buy_fur_coat(self):
        pass

    def clean_house(self):
        pass


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(home, color='cyan')

# TODO после реализации первой части - отдать на проверку учителю

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self):
        pass

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

    def soil(self):
        pass


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child:

    def __init__(self):
        pass

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass


# TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
kolya = Child(name='Коля')
murzik = Cat(name='Мурзик')

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolya.act()
    murzik.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(murzik, color='cyan')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


class Man:
    def __init__(self, name):
        self.house = None
        self.name = name
        self.satiety = 30
        self.degree_of_happiness = 100
        self.total_eat = 0

    def __str__(self):
        return 'Я - {}, сытость {},степень счастья {}'.format(self.name, self.satiety, self.degree_of_happiness)

    def eat(self):
        number = randint(0, 30)
        self.satiety += number
        self.total_eat += number
        self.house.food_in_the_fridge -= number
        cprint('{} покушал(a)'.format(self.name), color='yellow')

    def go_to_the_house(self, house):
        self.house = house
        self.satiety -= 10
        cprint('{} Вьехал(а) в дом'.format(self.name), color='yellow')

    def pet_the_cat(self):
        cprint('{} погладил(а) кота'.format(self.name), color='yellow')
        self.satiety -= 10
        self.degree_of_happiness -= 5


class House:

    def __init__(self):
        self.money_in_the_nightstand = 100
        self.food_in_the_fridge = 50
        self.dirt_in_the_house = 10
        self.total_mony = 0
        self.cat_food = 30

    def __str__(self):
        return 'В доме денег {}, еды {} ,осталось грязи {} ,еда коту {}'.format(self.money_in_the_nightstand,
                                                                    self.food_in_the_fridge, self.dirt_in_the_house,self.cat_food)


class Husband(Man):

    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.satiety <= 20:
            self.eat()
        elif self.house.money_in_the_nightstand < 100:
            self.work()
        elif self.degree_of_happiness <= 20:
            self.gaming()
        elif self.house.dirt_in_the_house >= 90:
            self.degree_of_happiness -= 10
            cprint('Счастье {} '.format(self.degree_of_happiness), color='green')
        elif self.degree_of_happiness < 10 or self.satiety <= 0:
            cprint('{} умер'.format(self.name), color='green')
        else:
            self.work()

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='green')
        self.house.money_in_the_nightstand += 150
        self.satiety -= 10
        self.house.total_mony += 150

    def gaming(self):
        cprint('{} играет в ПК'.format(self.name), color='green')
        self.degree_of_happiness += 20
        self.satiety -= 10


class Wife(Man):

    def __init__(self, name):
        super().__init__(name=name)
        self.fur_coat = 0

    def __str__(self):
        res = super().__str__()
        return res + ' количество шуб {}'.format(self.fur_coat)

    def act(self):
        self.house.dirt_in_the_house += 5
        if self.satiety <= 20:
            self.eat()
        elif self.house.food_in_the_fridge < 100:
            self.shopping()
        elif self.house.cat_food <= 100:
            self.cat_shopping()
        elif self.degree_of_happiness < 10 or self.satiety <= 0:
            cprint('{} умерла'.format(self.name), color='blue')
        elif self.house.dirt_in_the_house >= 100:
            self.clean_house()
        elif self.house.dirt_in_the_house >= 90:
            self.degree_of_happiness -= 10
            cprint('Счастье {} '.format(self.degree_of_happiness), color='blue')

        elif self.degree_of_happiness<40 and self.house.money_in_the_nightstand > 350:
            self.buy_fur_coat()

        else:
            self.pet_the_cat()

    def shopping(self):
        if self.house.money_in_the_nightstand >= 30:
            cprint('{} сходил в магазин за едой'.format(self.name), color='blue')
            self.house.money_in_the_nightstand -= 30
            self.house.food_in_the_fridge += 30


        else:
            cprint('{} деньги кончились!'.format(self.name), color='blue')
        self.satiety -= 10

    def buy_fur_coat(self):
        if self.house.money_in_the_nightstand > 350:
            cprint('{} сходил в магазин за шубой'.format(self.name), color='blue')
            self.house.money_in_the_nightstand -= 350
            self.degree_of_happiness += 60
            self.fur_coat += 1

        else:
            cprint('{} деньги кончились!'.format(self.name), color='blue')
        self.satiety -= 10

    def clean_house(self):
        print('{} убрала дом'.format(self.name))
        self.house.dirt_in_the_house -= 100
        self.satiety -= 10

    def cat_shopping(self):
        if self.house.money_in_the_nightstand >= 30:
            cprint('{} сходил в магазин за едой коту'.format(self.name), color='magenta')
            self.house.money_in_the_nightstand -= 30
            self.house.cat_food += 30
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

class Child(Man):

    def __init__(self, name):
        super().__init__(name=name)

    def eat(self):

        number = randint(1,10)
        self.satiety += number
        self.total_eat += number
        self.house.food_in_the_fridge -= number
        cprint('{} покушал(a)'.format(self.name), color='yellow')

    def go_to_the_house(self, house):
        self.house = house
        self.satiety -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='yellow')

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.degree_of_happiness < 10 or self.satiety <= 0:
            cprint('{} умерла'.format(self.name), color='blue')
        if self.satiety<20:
            self.eat()
        else:
            self.sleep()

    def sleep(self):
        self.satiety -= 10
        cprint('{} поспал'.format(self.name), color='yellow')






class Cat:

    def __init__(self, name):
        self.house = None
        self.name = name
        self.cat_satiety = 30

    def __str__(self):
        return 'Я {} ,сытость, {} '.format(self.name, self.cat_satiety)

    def act(self):
        if self.cat_satiety <= 20:
            self.eat()
        elif self.cat_satiety <= 0:
            cprint('{} умер'.format(self.name), color='blue')
        else:
            dice = randint(1, 4)
            if dice == 1:
                self.sleep()
            else:
                self.soil()

    def eat(self):
        if self.house.cat_food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.cat_satiety += 20
            self.house.cat_food -= 10
            return self.house.cat_food
        else:
            cprint('{} нет еды'.format(self.name), color='red')
            self.cat_satiety -= 10

    def sleep(self):
        self.cat_satiety -= 10
        print('Кот', self.name, 'поспал, сытость=', self.cat_satiety)

    def soil(self):
        self.house.dirt_in_the_house += 5
        self.cat_satiety -= 10
        print('Кот', self.name, 'драл обои, грязь =', self.house.dirt_in_the_house)

    def go_to_the_house(self, house):
        self.house = house
        self.cat_satiety -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='yellow')


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
kolya = Child(name='Коля')
murzik = Cat(name='Мурзик')
serge.go_to_the_house(home)
masha.go_to_the_house(home)
kolya.go_to_the_house(home)
murzik.go_to_the_house(home)
for day in range(366):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolya.act()
    murzik.act()
    cprint(serge, color='grey')
    cprint(masha, color='grey')
    cprint(kolya, color='cyan')
    cprint(murzik, color='grey')
    cprint(home, color='grey')

cprint('================== Ресурсы за 365 дней ==================', color='red')
print('Сережа и Маша счастья ', serge.degree_of_happiness + masha.degree_of_happiness+kolya.degree_of_happiness, 'куплено шуб '
      , masha.fur_coat, 'заработано денег', home.total_mony, 'рабочих дней', home.total_mony // 150,
      'скушали еды', masha.total_eat + serge.total_eat+ kolya.total_eat)
