# TASK 1
class Animal:

    def __init__(self, name, kind, old):
        self.__name = name
        self.__kind = kind
        self.__old = old

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, value):
        self.__kind = value

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, value):
        self.__old = value


# TASK 2
class Furniture:
    def __init__(self, name, weight):
        self._name = self.__verify_name(name)
        self._weight = self.__verify_weight(weight)

    def __verify_name(self, name):
        if not isinstance(name, str):
            raise TypeError('название должно быть строкой')
        return name

    def __verify_weight(self, weight):
        if weight < 0:
            raise TypeError('вес должен быть положительным числом')
        return weight


class Closet(Furniture):

    def __init__(self, name, weight, tp, doors):
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors

    def get_attrs(self):
        return self._name, self._weight, self._tp, self._doors


class Chair(Furniture):
    def __init__(self, name, weight, height):
        super().__init__(name, weight)
        self._height = height

    def get_attrs(self):
        return self._name, self._weight, self._height


class Table(Furniture):

    def __init__(self, name, weight, height, square):
        super().__init__(name, weight)
        self._height = height
        self._square = square

    def get_attrs(self):
        return self._name, self._weight, self._height, self._square


# TASK 3
class Observer:
    def update(self, data):
        pass

    def __hash__(self):
        return hash(id(self))


class Subject:
    def __init__(self):
        self.__observers = {}
        self.__data = None

    def add_observer(self, observer):
        self.__observers[observer] = observer

    def remove_observer(self, observer):
        if observer in self.__observers:
            self.__observers.pop(observer)

    def __notify_observer(self):
        for ob in self.__observers:
            ob.update(self.__data)

    def change_data(self, data):
        self.__data = data
        self.__notify_observer()


class Data:
    def __init__(self, temp, press, wet):
        self.temp = temp  # температура
        self.press = press  # давление
        self.wet = wet  # влажность


class TemperatureView(Observer):

    def update(self, data):
        if data:
            print(f'Текущая температура {data.temp}')


class PressureView(Observer):

    def update(self, data):
        if data:
            print(f'Текущая давление {data.press}')


class WetView(Observer):

    def update(self, data):
        if data:
            print(f'Текущая влажность {data.wet}')


# TASK 4
class Aircraft:

    def __init__(self, model, mass, speed, top):
        if not isinstance(model, str):
            raise TypeError('неверный тип аргумента')
        for i in [mass, speed, top]:
            if not isinstance(i, int) or i <= 0:
                raise TypeError('неверный тип аргумента')
        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top


class PassengerAircraft(Aircraft):

    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        if not isinstance(chairs, int) or chairs <= 0:
            raise TypeError('неверный тип аргумента')
        self._chairs = chairs


class WarPlane(Aircraft):

    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        if not isinstance(weapons, dict):
            raise TypeError('неверный тип аргумента')
        self._weapons = weapons


# TASK 5
def class_log(lst):
    def wrapper(cls):
        methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
        for k, v in methods.items():
            setattr(cls, k, some_funk(v))
        return cls

    def some_funk(method):
        def wrapper2(*args, **kwargs):
            lst.append(method.__name__)
            return method(*args, **kwargs)
        return wrapper2
    return wrapper

vector_log = []
@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value

    def get_coords(self):
        return self.__coords


# TASK 6
CURRENT_OS = 'windows'   # 'windows', 'linux'
class WindowsFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов

    def get_title(self):
        return self.__title
class LinuxFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов
class FileDialogFactory:
    __instance = None

    def __new__(cls, title, path, exts):
        if CURRENT_OS == 'windows':
            return WindowsFileDialog(title, path, exts)
        elif CURRENT_OS == 'linux':
             return LinuxFileDialog(title, path, exts)

    def __init__(self, title, path, exts):
        self.__title = title
        self.__path = path
        self.__exts = exts

    @staticmethod
    def create_windows_filedialog(title, path, exts):
        return WindowsFileDialog(title, path, exts)

    @staticmethod
    def create_linux_filedialog(title, path, exts):
        return LinuxFileDialog(title, path, exts)

