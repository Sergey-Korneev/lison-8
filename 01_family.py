# -*- coding: utf-8 -*-
import random
from termcolor import cprint


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
#   кол-во денег в тумбочке (в начале - 100)+
#   кол-во еды в холодильнике (в начале - 50)+
#   кол-во грязи (в начале - 0)+
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
        self.money = 100
        self.food = 50
        self.dirt = 0
        self.cat_food = 10

    def __str__(self):
        return "В доме денег {}, еды {}, грязи {}".format(self.money, self.food, self.dirt)

    def dirt_guidance(self):
        self.dirt += 5


class Human:
    def __init__(self, name, home):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = home
        self.alive = True

    def eat(self):
        food_eat = random.randint(10, 30)
        if food_eat <= self.house.food:
            self.fullness += food_eat
            self.house.food -= food_eat
            print("{} поел на {}".format(self.name, food_eat))
        else:
            print("Нет еды")

    def __str__(self):
        return "Моё имя {}, я сыт на {}, я счастлив на {}".format(self.name, self.fullness, self.happiness)

    def bay_food(self):
        if self.house.money >= 60:
            print("{} купил еду 30 шт".format(self.name))
            self.house.food += 60
            self.house.money -= 60
        else:
            print("Нет денег на еду")

    def bay_food_cat(self):
        if self.house.money >= 30:
            print("{} купил еду 30 шт".format(self.name))
            self.house.cat_food += 40
            self.house.money -= 40
        else:
            print("Нет денег на еду для кота")

    def act(self):
        if self.fullness <= 0 or self.happiness < 10:
            print("{} умер...".format(self.name))
            self.alive = False
            return
        if self.house.dirt >= 90:
            self.happiness -= 10
        elif self.fullness < 30:
            self.eat()


class Husband(Human):

    def __init__(self, name, home):
        super().__init__(name, home)

    def __str__(self):
        return super().__str__()

    def act(self):
        super().act()
        if self.alive:
            if self.house.money < 500:
                self.work()
            elif self.happiness < 50:
                self.gaming()
            else:
                print("Смотрит ТВ")

    def work(self):
        print("{} пошл на работу".format(self.name))
        self.house.money += 150
        self.fullness -= 10

    def gaming(self):
        if self.happiness > 80:
            self.happiness = 100
            print("{} играет".format(self.name))
        elif self.happiness < 80:
            print("{} играет".format(self.name))
            self.happiness += 20
        self.fullness -= 10


class Wife(Human):

    def __init__(self, name, home):
        super().__init__(name, home)

    def __str__(self):
        return super().__str__()

    def act(self):
        super().act()
        if self.alive:
            if self.house.food <= 20:
                self.bay_food()
            elif self.house.cat_food <= 15:
                self.bay_food_cat()
            elif self.house.dirt > 95:
                self.clean_house()
            elif self.happiness <= 40:
                self.buy_fur_coat()
            else:
                print("Смотрит ТВ")

    def buy_fur_coat(self):
        if self.house.money >= 350:
            print("{} Купила шубу".format(self.name))
            self.happiness += 60
            self.house.money -= 350
        else:
            print("Нет денег на шубу")

    def clean_house(self):
        print("{} убрала в дома".format(self.name))
        self.house.dirt = 0
        self.fullness -= 10


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

    def __init__(self, name, home):
        self.name = name
        self.fullness = 30
        self.house = home
        self.alive = True

    def __str__(self):
        return "Моё имя {}, я сыт на {}".format(self.name, self.fullness)

    def act(self):
        event = random.randint(4, 9)
        if self.fullness <= 0:
            print("{} умер...".format(self.name))
            if self.alive:
                self.alive = False
            return
        elif self.fullness < 15:
            self.eat()
        elif 4 >= event <= 6:
            self.sleep()
        else:
            self.soil()

    def eat(self):
        food_eat = random.randint(10, 30)
        if food_eat <= self.house.food:
            self.fullness += food_eat
            self.house.cat_food -= food_eat
            print("{} кот поел на {}".format(self.name, food_eat))
        else:
            print("Нет еды для кота")

    def sleep(self):
        print("Кот {} спит".format(self.name))
        self.fullness -= 10

    def soil(self):
        print("Кот {} дерет обои".format(self.name))
        self.fullness -= 10
        self.house.dirt += 5


home = House()
serge = Husband(name='Сережа', home=home)
masha = Wife(name='Маша', home=home)
barsic = Cat(name='Барсик', home=home)

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    barsic.act()
    home.dirt_guidance()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(barsic, color='cyan')
    cprint(home, color='cyan')


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


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')

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
