# TASK 1
class ListInteger(list):

    def __init__(self, *args):
        for i in args:
            if not isinstance(i, int):
                raise TypeError('можно передавать только целочисленные значения')
        super().__init__(args)

        self.lst = [i for i in args[0]]

    def __getitem__(self, item):
        return self.lst[self.lst.index(item)]

    def __setitem__(self, key, value):
        if not isinstance(value, int):
            raise TypeError('можно передавать только целочисленные значения')

        self.lst[self.lst.index(key)] = value

    def append(self, data):
        if not isinstance(data, int):
            raise TypeError('можно передавать только целочисленные значения')
        self.lst.append(data)


# TASK 2
class Thing:
    __counter = 1

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __setitem__(self, key, value):
        self.key = value
class DictShop(dict):

    def __init__(self, **kwargs):
        for i in kwargs.keys():
            if not isinstance(i, Thing):
                raise TypeError('ключами могут быть только объекты класса Thing')
        super().__init__()
        for i, k in kwargs.items():
            self[i] = k



    def __setitem__(self, key, value):
        if not isinstance(key, Thing):
            raise TypeError('ключами могут быть только объекты класса Thing')
        super().__setitem__(key, value)

    def __iter__(self):
        for i in self:
            yield i


# TASK 3
class Protists:
    pass
class Plants(Protists):
    pass
class Animals(Protists):
    pass
class Mosses(Plants):
    pass
class Flowering(Plants):
    pass
class Worms(Animals):
    pass
class Mammals(Animals):
    pass
class Human(Mammals):
    pass
class Monkeys(Mammals):
    pass
class Monkey(Monkeys):

    def __init__(self, name, weight, old):
        self.name = name
        self.weight = weight
        self.old = old
class Person(Human):

    def __init__(self, name, weight, old):
        self.name = name
        self.weight = weight
        self.old = old
class Flower(Flowering):

    def __init__(self, name, weight, old):
        self.name = name
        self.weight = weight
        self.old = old
class Worm(Worms):

    def __init__(self, name, weight, old):
        self.name = name
        self.weight = weight
        self.old = old
# lst_objs = [Monkey("мартышка", 30.4, 7), Monkey("шимпанзе", 24.6, 8),
#             Person("Балакирев", 88, 34), Person("Верховный жрец", 67.5, 45),
#             Flower("Тюльпан", 0.2, 1), Flower("Роза", 0.1, 2),
#             Worm("червь", 0.01, 1), Worm("червь 2", 0.02, 1)]
# lst_animals = [i for i in lst_objs if isinstance(i, Animals)]
# lst_plants = [i for i in lst_objs if isinstance(i, Plants)]
# lst_mammals = [i for i in lst_objs if isinstance(i, Mammals)]


# TASK 4
class Tuple(tuple):

    def __add__(self, other):
        if isinstance(other, tuple):
            return Tuple(super().__add__(other))
        else:
            return Tuple(list(self) + list(other))


# TASK 5
class VideoItem:

    def __init__(self, title, descr, path):
        self.title = title
        self.descr = descr
        self.path = path
        self.rating = VideoRating()
class VideoRating:

    def __init__(self):
        self.__rating = 0

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if value < 0 or value >= 5:
            raise ValueError('неверное присваиваемое значение')
        self.__rating = value


# TASK 6
class IteratorAttrs:

    def __iter__(self):
        for i in self.__dict__.items():
            yield i
class SmartPhone(IteratorAttrs):

    def __init__(self, model, size, memory):
        self.model = model
        self.size = size
        self.memory = memory






