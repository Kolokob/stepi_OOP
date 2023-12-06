class Money:
    def __init__(self, money):
        self.money = money


class Point:
    def __init__(self, x, y, color = 'black'):
        self.x = x
        self.y = y
        self.color = color


points = [Point(i, i) for i in range(1, 1000, 2)]
points[1].color = 'yellow'
p1 = Point(10, 20)
p2 = Point(12, 5, 'red')

import random

class  Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)



a = 'qwertyuiopasdfghjklzxcvbnm'
for items in a:
    for e in range(217):
        el = items + str(e)
        el = list(el)
        el.append(random.choice([Line(0, 0, 0, 0), Rect(1, 2, 3, 4), Ellipse(5, 6, 7, 8)] ))
        print()



class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if type(self.a) not in (int, float) or self.a <= 0:
            return 1

        if  self.a + self.b < self.c or self.b + self.c < self.a or self.a + self.c < self.b :
            return 2

        else:
            return 3

a, b, c = map(int, input().split())

tr = TriangleChecker(a, b, c)
print(tr.is_triangle())

class Graph:
    def __init__(self, data : list):
        self.data = data.copy()
        self.is_show = True

    def set_data(self, data):
        self.data = data


    def show_table(self):
        if self.is_show == True:
            return self.data
        else:
            print("Отображение данных закрыто")

    def show_graph(self):
        if self.is_show == True:
            for i in self.data:
                print("Графическое отображение данных: ", i, end='')
                print()
        else:
            print("Отображение данных закрыто")

    def show_bar(self):
        if self.is_show == True:
            print('Столбчатая диаграмма:', *self.data)

        else:
            print("Отображение данных закрыто")

    def set_show(self, fl_show):
         self.is_show = fl_show

data_graph = list(map(int, input().split()))
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()


class CPU:

    def __init__(self, name,  fr):
        self.name = name
        self.fr =  fr

class Memory:

    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

class MotherBoard:

    def __init__(self, name, cpu, *mems):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = mems[:self.total_mem_slots]

    def get_config(self):

        return [f'Материнская плата: {self.name}',
                f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
                f'Слотов памяти: {self.total_mem_slots}',
                'Память: ' + ";".join(map(lambda x: f'{x.name} + {x.volume}', self.mem_slots))]




emp = MotherBoard('Gigabyte', CPU('Intel', 2000), Memory('Kingston', 1000), Memory('Kingston', 2000))
print(emp.get_config())


class Cart:

    goods = []

    def add(self, gd):
        self.gd = gd
        self.goods.append(self.gd)

    def remove(self, indx):
        self.indx = indx

    def get_list(self):
        return [f"{i.name}: {i.prise}" for i in self.goods]


class Table(Cart):
    def __init__(self, name, prise):
        self.name = name
        self.prise = prise

class TV(Cart):
    def __init__(self, name, prise):
        self.name = name
        self.prise = prise

class Notebook(Cart):
    def __init__(self, name, prise):
        self.name = name
        self.prise = prise

class Cup(Cart):
    def __init__(self, name, prise):
        self.name = name
        self.prise = prise

cart = Cart()

tv1 = TV("samsung", 1111)
tv2 = TV("LG", 1234)
table = Table("ikea", 2345)
n1= Notebook("msi", 5433)
n2 = Notebook("apple", 542)
c = Cup("keepcup", 43)

cart.add(tv1)
cart.add(tv2)
cart.add(table)
cart.add(n1)
cart.add(n2)
cart.add(c)

import sys

class ListObject:


    def __init__(self, data):
        next_obj = None
        self.data = data


    def link(self, obj):
        self.next_obj = obj

lst_in = list(map(str.strip, sys.stdin.readlines()))

head_obj = ListObject(lst_in[0])
obj = head_obj
for i in range(1, len(lst_in)):
    obj_new = ListObject(lst_in[i])
    obj.link(obj_new)
    obj = obj_new

import random

class Cell:
    def __init__(self, around_mines, mine):
        self.around_mines = 0
        self.mine = False
        self.fl_open = False


class GamePole:

    star = '*'
    count = 0
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.data = [[random.randint(0, 9) for _ in range(self.N)] for _ in range(self.N)]

    def init(self):
        for i in self.data:
            print(i)
            mines = random.sample(i, random.randint(10, 10))
            for emp in mines:
                del i[emp]
                i.insert(emp, self.star)
                print(' '.join(map(str, i)))
                break
            self.count += 1


    def show(self):
        b = [['#' for _ in range(self.N)] for _ in range(self.N)]
        for i in self.data:
            mines = random.sample(i, random.randint(10, 10)) #ЕБАНЫЕ МИНЫ ЗА ДОНБАСС БЛЯ!!!
            for emp in mines:
                del i[emp]
                i.insert(emp, self.star)
                # print(' '.join(map(str, i)))
                break
                
        return len(i.intersection(value))


        # ЗДЕСЬ НАПИСАННАЯ ФУНКЦИЯ С ДВУМЕРНЫМ МАССИВОМ 10x10

        # В ПЕРЕМЕННУЮ pole МЫ ЗАПИСЫВАЕМ ЭТОТ МАССИВ

        # ЗДЕСЬ МЫ ПРОСТО ВЫВОДИМ ЭТО ПОЛЕ







a = GamePole(10, 5)
a.gg(5)




star = '*'
count = 0
def __init__(self, N, M):
    self.N = N
    self.M = M
    self.data = [[random.randint(1, 10) for _ in range(self.N)] for _ in range(self.N)]
    print(self.data)
    for i in self.data:
        mines = random.sample(i, random.randint(1, 10)) #ЕБАНЫЕ МИНЫ ЗА ДОНБАСС БЛЯ!!!
        for emp in mines:
            if 1 <= self.count <= 10:
                del i[emp]
                i.insert(emp, self.star)
                print(i)
            self.count += 1


            self.data.append(self.star[emp])

