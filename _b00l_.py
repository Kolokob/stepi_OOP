# TASK 1
import math
import random


class Player:

    def __init__(self, name, old, score):
        self.name = name
        self.old = old
        self.score = int(score)

    def __bool__(self):
        return True if self.score > 0 else False


# TASK 2
lst_in = []


class MailItem:
    def __init__(self, mail_from, title, content):
        self.mail_from = mail_from
        self.title = title
        self.content = content
        self.is_read = False

    def set_read(self, fl_read):
        self.is_read = fl_read

    def __bool__(self):
        return self.is_read


class MailBox:

    def __init__(self):
        self.inbox_list = []

    def receive(self):
        for i in lst_in:
            args = list(map(str.strip, i.split(';')))
            self.inbox_list.append(MailItem(*args))


# TASK 3
class Line:

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def __len__(self):
        return int(math.sqrt(((self.x2 - self.x1) * 2) + ((self.y2 - self.y1) * 2)))

    def __bool__(self):
        return False if len(self) < 1 else True


# TASK 4
class Ellipse:
    def __init__(self, *args):
        if len(args) == 4:
            self.x1, self.y1, self.x2, self.y2 = args

    def get_coords(self):
        if not self:
            raise AttributeError('нет координат для извлечения')
        return self.x1, self.y1, self.x2, self.y2

    def __bool__(self):
        return all(hasattr(self, attr) for attr in ['x1', 'y1', 'x2', 'y2'])


# BIG TASK 5
# НУ ПОГНАЛИ
from random import randint
class Cell:

    def __init__(self):
        self.__is_mine = False
        self.__number = 0
        self.__is_open = False

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, value):
        if type(value) != bool:
            raise ValueError("недопустимое значение атрибута")
        self.__is_mine = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if type(value) != int or value < 0  or value > 8:
            raise ValueError("недопустимое значение атрибута")
        self.__number = value

    @property
    def is_open(self):
        return self.is_open

    @is_open.setter
    def is_open(self, value):
        if type(value) != bool:
            raise ValueError("недопустимое значение атрибута")
        self.__is_open = value


    def __bool__(self):
        return not self.__is_open
class GamePole:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        GamePole.__instance = None

    @property
    def pole(self):
        return self.__pole_cells

    def __init__(self, N, M, total_mines):
        self.__n = N
        self.__m = M
        self.__total_mines = total_mines
        self.__pole_cells = tuple(tuple(Cell() for _ in range(M)) for _ in range(N))
        self.init_pole()

    def init_pole(self):
        for row in self.__pole_cells:
            for x in row:
                x.is_open = False
                x.is_mine = False

        m = 0
        while m < self.__total_mines:
            i = randint(0, self.__n - 1)
            j = randint(0, self.__m - 1)
            if self.__pole_cells[i][j].is_mine:
                continue
            self.__pole_cells[i][j].is_mine = True
            m += 1

        indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)

        for x in range(self.__n):
            for y in range(self.__m):
                if not self.__pole_cells[x][y].is_mine:
                    mines = sum(self.__pole_cells[x + i][y + j].is_mine for i, j in indx if 0 <= x + i < self.__n and 0 <= y + j < self.__m)
                    self.__pole_cells[x][y].number = mines

    def open_cell(self, i, j):
        if not 0 <= i < self.__n or not 0 <= j < self.__m:
            raise IndexError('некорректные индексы i, j клетки игрового поля')
        self.pole[i][j].is_open = True

    def show_pole(self):
        for row in self.pole:
            print(*map(lambda x: '#' if not x.is_open else x.number if not x.is_mine else '*', row))
class MyGamePole:
    _instance = None
    star = '*'
    count = 0

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self, N, M, total_mines):
        self.N = N
        self.M = M
        self.total_mines = total_mines
        self.__pole_cells = [[Cell(is_mine=False, is_open=True) for i in range(self.M)] for j in range(self.N)]

    @property
    def pole(self):
        return getattr(self, '_GamePole__pole_cells')

    def init_pole(self):
        all_positions = [(i, j) for i in range(self.M) for j in range(self.N)]
        mine_positions = random.sample(all_positions, self.total_mines)

        for i, j in mine_positions:
            self.__pole_cells[i][j].is_mine = True
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    r, c = i + dr, j + dc
                    if 0 <= r < self.M and 0 <= c < self.N and not self.__pole_cells[r][c].is_mine:
                        self.__pole_cells[r][c].number += 1

    def open_cell(self, i, j):
        try:
            self.__pole_cells[i][j].is_open = True
        except IndexError:
            raise IndexError('некорректные индексы i, j клетки игрового поля')

    def show_pole(self):

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        for i in range(self.M):
            for j in range(self.N):
                if self.__pole_cells[i][j].is_mine:
                    for dr, dc in directions:
                        r, c = i + dr, j + dc
                        if 0 <= r < self.N and 0 <= c < self.M and not self.__pole_cells[r][c].is_mine:
                            self.__pole_cells[r][c].number += 1

        for i in range(self.M):
            for j in range(self.N):
                if self.__pole_cells[i][j].number == 0:
                    print('*', end=' ')
                else:
                    print(self.__pole_cells[i][j].number, end=' ')
            print()


# TASK 6

class Vector:

    def __init__(self, *args, coords = []):
        self.coords = coords
        self.vectors = args


    def __add__(self, other):
        # longer_v = len(self.vectors) if len(self.vectors) > len(other.vectors) else len(other.vectors)
        temp = []
        for i in range(3):
            temp.append(self.vectors[i] + other.vectors[i])
        return Vector(coords=temp)


    def __sub__(self, other):
        # longer_v = len(self.vectors) if len(self.vectors) > len(other.vectors) else len(other.vectors)
        temp = []
        for i in range(3):
            temp.append(self.vectors[i] - other.vectors[i])
        return Vector(coords=temp)

    def __mul__(self, other):
        # longer_v = len(self.vectors) if len(self.vectors) > len(other.vectors) else len(other.vectors)
        temp = []
        for i in range(3):
            temp.append(self.vectors[i] * other.vectors[i])
        return Vector(coords=temp)

    def __iadd__(self, other):
        temp = []
        if isinstance(other, Vector):
            for i in range(3):
                temp.append(self.vectors[i] * other.vectors[i])
            return Vector(coords=temp)
        else:
            for i in range(3):
                temp.append(self.vectors[i] + other)
            return Vector(coords=temp)


    def __isub__(self, other):
        temp = []
        if isinstance(other, Vector):
            for i in range(3):
                temp.append(self.vectors[i] * other.vectors[i])
            return Vector(coords=temp)
        else:
            for i in range(3):
                temp.append(self.vectors[i] - other)
            return Vector(coords=temp)

    def __eq__(self, other):
        return self.coords == other.coords

    def __ne__(self, other):
        return self.coords != other.coords

    def __repr__(self):
        return f"Vector({', '.join(map(str, self.coords))})"



v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print((v1 + v2).coords)  # [5, 7, 9]
print((v1 - v2).coords)  # [-3, -3, -3]
print((v1 * v2).coords)  # [4, 10, 18]

v1 += 10
print(v1.coords)  # [11, 12, 13]
v1 -= 10
print(v1.coords)  # [1, 2, 3]
v1 += v2
print(v1.coords)  # [5, 7, 9]
v2 -= v1
print(v2.coords)  # [-1, -2, -3]

print(v1 == v2)  # False
print(v1 != v2)  # True