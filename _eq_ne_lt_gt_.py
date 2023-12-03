import re

# TASK 1
class Track:

    def __init__(self, start_x=0, start_y=0):
        self.start_x = start_x
        self.start_y = start_y
        self.route = []

    def add_track(self, tr):
        self.route.append(tr)

    def get_tracks(self):
        return self.route

    def __len__(self):
        x1, y1 = self.start_x, self.start_y
        distance = 0
        for i in self.route:
            x2, y2 = self.route[0].to_x, self.route[0].to_y
            distance += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            x1, y1 = x2, y2
        return distance
class TrackLine:

    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed

# TASK 2
class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
        self.volume = self.__a * self.__b * self.__c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if self.MIN_DIMENSION <= self.__a <= self.MAX_DIMENSION:
            self.__a = value
            self.volume = self.__a * self.__b * self.__c
        else:
            pass

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if self.MIN_DIMENSION <= self.__b <= self.MAX_DIMENSION:
            self.__b = value
            self.volume = self.__a * self.__b * self.__c
        else:
            pass

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        if self.MIN_DIMENSION <= self.__c <= self.MAX_DIMENSION:
            self.__c = value
            self.volume = self.__a * self.__b * self.__c
        else:
            pass

    def __lt__(self, other):
        return other.volume > self.volume

    def __le__(self, other):
        return other.volume >= self.volume
class ShopItem:

    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.dim = dim

# TASK 3
class StringText:
    def __init__(self, lst):
        self.lst_words = lst

    def __len__(self):
        return len(self.lst_words)

    def __lt__(self, other):
        return len(self) < len(other)

    def __le__(self, other):
        return len(self) <= len(other)

# TASK 4
class Morph:

    def __init__(self, *args):
        self.words = [i for i in args]

    def add_word(self, word):
        self.words.append(word)

    def get_words(self):
        return self.words

    def __eq__(self, other):
        print(other.lower(), self.words[0].lower())
        return other.lower() in self.words[0].lower()

# TASK 5
class FileAcceptor:
    def __init__(self, *extensions):
        if len(extensions) == 1 and isinstance(extensions[0], (tuple, list)):
            self.extensions = extensions[0]
        else:
            self.extensions = extensions

    def __call__(self, name, *args, **kwargs):
        start = name.rfind('.')
        ext = "" if start == -1 else name[start+1:]
        return ext in self.extensions

    def __add__(self, other):
        unique_extensions = set(self.extensions).union(set(other.extensions))
        return FileAcceptor(*unique_extensions)

# TASK 6
class MoneyD:

    def __init__(self, volume=0, cb=None):
        self.cb = cb
        self.volume = volume

    @property
    def cb_pr(self):
        return self.cb

    @cb_pr.setter
    def cb_pr(self, value):
        self.cb = value

    @property
    def volume_pr(self):
        return self.volume

    @volume_pr.setter
    def volume_pr(self, value):
        self.volume = value

    def convert(self, value):
        if self.cb is None or value.cb is None:
            raise ValueError("Неизвестен курс валют.")
        if isinstance(value, MoneyR):
            return value.volume / self.cb.rates['rub']
        elif isinstance(value, MoneyD):
            return value.volume
        elif isinstance(value, MoneyE):
            return value.volume / self.cb.rates['euro']

    def __lt__(self, other):
        return self.convert(other) > self.volume

    def __le__(self, other):
        return self.convert(other) >= self.volume

    def __eq__(self, other):
        return self.convert(other) == self.volume
class MoneyE:

    def __init__(self, volume=0, cb=None):
        self.cb = cb
        self.volume = volume

    @property
    def cb_pr(self):
        return self.cb

    @cb_pr.setter
    def cb_pr(self, value):
        self.cb = value

    @property
    def volume_pr(self):
        return self.volume

    @volume_pr.setter
    def volume_pr(self, value):
        self.volume = value

    def convert(self, value):
        if self.cb is None or value.cb is None:
            raise ValueError("Неизвестен курс валют.")
        if isinstance(value, MoneyR):
            return value.volume / self.cb.rates['rub'] * self.cb.rates['euro']
        elif isinstance(value, MoneyD):
            return value.volume * self.cb.rates['euro']
        elif isinstance(value, MoneyE):
            return value.volume

    def __lt__(self, other):
        return self.convert(other) > self.volume

    def __le__(self, other):
        return self.convert(other) >= self.volume

    def __eq__(self, other):
        return self.convert(other) == self.volume
class MoneyR:

    def __init__(self, volume=0, cb=None):
        self.cb = cb
        self.volume = volume

    @property
    def cb_pr(self):
        return self.cb

    @cb_pr.setter
    def cb_pr(self, value):
        self.cb = value

    @property
    def volume_pr(self):
        return self.volume

    @volume_pr.setter
    def volume_pr(self, value):
        self.volume = value

    def convert(self, value):
        if self.cb is None or value.cb is None:
            raise ValueError("Неизвестен курс валют.")
        if isinstance(value, MoneyR):
            return value.volume
        elif isinstance(value, MoneyD):
            return value.volume * self.cb.rates['rub']
        elif isinstance(value, MoneyE):
            return value.volume * self.cb.rates['rub'] / self.cb.rates['euro']

    def __lt__(self, other):
        return self.convert(other) > self.volume

    def __le__(self, other):
        return self.convert(other) >= self.volume

    def __eq__(self, other):
        return self.convert(other) == self.volume
class CentralBank:

    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def register(cls, money):
        money.cb = cls

# TASK 7
class Body:

    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume

    def check(self, value):
        if isinstance(value, (int, float)):
            return self.ro * self.volume < value
        elif isinstance(value, Body):
            return self.ro * self.volume < value.ro * value.volume

    def __gt__(self, other):
        if isinstance(other, (int, float)):
            return (self.ro * self.volume) > other
        elif isinstance(other, Body):
            return (self.ro * self.volume) > (other.ro * other.volume)

    def __lt__(self, other):
        return self.check(other)

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            return (self.ro * self.volume) == other
        elif isinstance(other, Body):
            return (self.ro * self.volume) == (other.ro * other.volume)

# TASK 8
class Thing:

    def __init__(self, name, mass):
        self.name = name
        if isinstance(mass, (int, float)):
            self.mass = mass
        else:
            pass

    def __eq__(self, other):
        return self.name.lower() == other.name.lower() and self.mass == other.mass
class Box:

    def __init__(self):
        self.box = []

    def add_thing(self, obj):
        self.box.append(obj)

    def get_things(self):
        return self.box

    def __eq__(self, other):
        sorted_self = sorted([(i.name, i.mass) for i in self.box])
        sorted_other = sorted([(i.name, i.mass) for i in other.box])
        return sorted_self == sorted_other


