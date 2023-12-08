# TASK 1
class Book:

    def __init__(self, title, author, pages, year):
        self.title = title
        self.authorr = author
        self.pages = pages
        self.year = year


class DigitBook(Book):

    def __init__(self, title, author, pages, year, size, frm):
        super().__init__(title, author, pages, year)
        self.size = size
        self.frm = frm


# TASK 2
class Thing:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class ArtObject(Thing):
    def __init__(self, name, weight, author, date):
        super().__init__(name, weight)
        self.author = author
        self.date = date


class Computer(Thing):
    def __init__(self, name, weight, memory, cpu):
        super().__init__(name, weight)
        self.memory = memory
        self.cpu = cpu


class Auto(Thing):
    def __init__(self, name, weight, dims):
        super().__init__(name, weight)
        self.dims = dims


class Mercedes(Auto):

    def __init__(self, name, weight, dims, model, old):
        super().__init__(name, weight, dims)
        self.model = model
        self.old = old


class Toyota(Auto):
    def __init__(self, name, weight, dims, model, wheel):
        super().__init__(name, weight, dims)
        self.model = model
        self.wheel = wheel


# TASK 3
class SellItem:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class House(SellItem):

    def __init__(self, name, price, material, square):
        super().__init__(name, price)
        self.material = material
        self.square = square


class Flat(SellItem):
    def __init__(self, name, price, size, rooms):
        super().__init__(name, price)
        self.size = size
        self.rooms = rooms


class Land(SellItem):

    def __init__(self, name, price, square):
        super().__init__(name, price)
        self.square = square


class Agency:

    def __init__(self, name):
        self.name = name
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

    def remove_object(self, obj):
        del self.objects[self.objects.index(obj)]

    def get_objects(self):
        return self.objects


# TASK 4
class Router:
    app = {}

    @classmethod
    def get(cls, path):
        return cls.app.get(path)

    @classmethod
    def add_callback(cls, path, func):
        cls.app[path] = func


class Callback:

    def __init__(self, path, router_cls):
        self.path = path
        self.router_cls = router_cls

    def __call__(self, *args, **kwargs):
        Router.add_callback(self.path, args[0])


# @Callback('/', Router)
# def index():
#     return '<h1>Главная</h1>'
# route = Router.get('/')
# if route:
#     ret = route()
#     print(ret)


# TASK 5

# def integer_params_decorated(func):
#     def wrapper(self, *args, **kwargs):
#         if not all(type(x) == int for x in args):
#             raise TypeError("аргументы должны быть целыми числами")
#         if not all(type(x) == int for x in kwargs.values()):
#             raise TypeError("аргументы должны быть целыми числами")
#         return func(self, *args, **kwargs)
#     return wrapper
# def integer_params(cls):
#     methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
#     for k, v in methods.items():
#         print(v)
#         setattr(cls, k, integer_params_decorated(v))
#
#     return cls
# @integer_params
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value

    def set_coords(self, *coords, reverse=False):
        c = list(coords)
        self.__coords = c if not reverse else c[::-1]


# TASK 6
class SoftList(list):

    def __init__(self, lst):
        super().__init__(lst)

    def __getitem__(self, item):
        try:
            return super().__getitem__(item)
        except IndexError:
            return False


# TASK 7
class StringDigit:

    def __init__(self, string):
        for i in string:
            try:
                int(i)
            except ValueError:
                raise ValueError("в строке должны быть только цифры")
        self.string = string

    def __str__(self):
        return self.string

    def __add__(self, other):
        if isinstance(other, str):
            return StringDigit(self.string + other)

    def __radd__(self, other):
        if isinstance(other, str):
            return StringDigit(other + self.string)

    def __eq__(self, other):
        return self.string == other


# TASK 8

class ItemAttrs:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xy = [self.x, self.y]

    def __getitem__(self, item):
        return self.xy[item]

    def __setitem__(self, key, value):
        self.xy[key] = value


class Point(ItemAttrs):
    pass


pt = Point(1, 2.5)
x = pt[0]  # 1
y = pt[1]  # 2.5
pt[0] = 10
