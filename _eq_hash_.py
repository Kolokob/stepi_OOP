import math
from collections import deque, Counter
# TASK 1
class Rect:
    def __init__(self, x, y, width, height):
        for arg in [x, y, width, height]:
            if not isinstance(arg, (int, float)):
                raise ValueError("All arguments must be int or float")
        self.x = x
        self.y = y
        self.width = width
        self.height = height


    def __eq__(self, other):
        return self.width == other.width and self.height == other.height

    def __hash__(self):
        return hash((self.width, self.height))


# TASK 2
class ShopItem:

    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price


    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        return (self.name.lower(), self.weight, self.price) == (other.name.lower(), other.weight, other.price)

# TASK 3
class Record:

    instance_pk = 0

    def __init__(self, fio, descr, old):
        self.fio = fio
        self.descr = descr
        self.old = old
        Record.instance_pk += 1
        self.pk = Record.instance_pk


    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash((self.fio.lower(), self.old))
class DataBase:

    def __init__(self, path):
        self.path = path
        self.dict_db = dict()
        self.lst = []

    def write(self, record):
        self.dict_db.setdefault(record, [])

    def read(self, pk):
        for i in self.dict_db:
            if i.pk == pk:
                return i


# TASK 4
class BookStudy:


    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash((self.name, self.author))

# TASK 5
class Dimensions:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, key, value):
        try:
            value = int(value)  # Try to convert to an int first
        except ValueError:
            try:
                value = float(value)  # Then try to convert to a float
            except ValueError:
                pass

        if value < 0:
            raise ValueError("габаритные размеры должны быть положительными числами")

        super().__setattr__(key, value)

    def __eq__(self, other):
        return (self.a, self.b, self.c) == (other.a, other.b, other.c)

    def __hash__(self):
        return hash((self.a, self.b, self.c))

# TASK 6

class TriangleDescriptor:

    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}_{name}'

    def __get__(self, obj, objtype):
        return getattr(obj, self.name, None)

    def __set__(self, obj, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")
        setattr(obj, self.name, value)

class Triangle:

    a = TriangleDescriptor()
    b = TriangleDescriptor()
    c = TriangleDescriptor()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def __is_triangle(a, b, c):
        if a and b and c:
            return a < b + c and b < a + c and c < a + b
        return True

    def __setattr__(self, key, value):
        if (key == 'a' and not self.__is_triangle(value, self.b, self.c)) or \
                (key == 'b' and not self.__is_triangle(self.a, value, self.c)) or \
                (key == 'c' and not self.__is_triangle(self.a, self.b, value)):
            raise ValueError("С указанными длинами нельзя образовать треугольник")
        super().__setattr__(key, value)

    def __len__(self):
        return int(self.a + self.b + self.c)

    def __call__(self, *args, **kwargs):
        p = float(self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

sp = Triangle(3.4, 4, 5)
print(sp())


