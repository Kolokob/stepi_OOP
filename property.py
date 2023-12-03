# class Car:
#     def __init__(self):
#         self.__model = self
#
#     def set_money(self, value):
#         if str(value):
#             if 2 < len(value) < 100:
#                 self.__model = value
#         else:
#             pass
#
#
#     def get_money(self):
#         return self.__model
#
#     model = property(get_money, set_money)
#
# car = Car()
# car.model = "Toyota"





# class Person:
#     def __init__(self, name):
#         self._name = name
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, value):
#         self._name = value
# nick = Person('Nick')


# class RadiusVector2D:
#
#     MIN_COORD = -100
#     MAX_COORD = 1024
#
#     def __init__(self, x = 0, y = 0):
#         self.__x = x
#         self.__y = y
#         self.x = x
#         self.y = y
#
#     @classmethod
#     def __check(cls, value):
#         if cls.MIN_COORD < value < cls.MAX_COORD:
#             return True
#         else:
#             return False
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, value):
#         if self.__check(value):
#             self.__x = value
#         else:
#             raise ValueError
#     @property
#     def y(self):
#         return self.__x
#
#     @y.setter
#     def y(self, value):
#         self.__y = value
#
#     @staticmethod
#     def norm2(vector):
#         return vector.x * vector.x + vector.y * vector.y
#
# r = RadiusVector2D()
# r.x = -4
# r.y = 2
# print(r.norm2(RadiusVector2D(r.x, r.y)))


# class DecisionTree:
#
#     @classmethod
#     def predict(cls, root, x):
#         """для построения прогноза (прохода по решающему дереву) для вектора x из корневого узла дерева root"""
#         for x in root:
#             print(x)
#
#     @classmethod
#     def add_obj(cls, obj, node=None, left=True):
#         cls.head = None
#         """для добавления вершин в решающее дерево (метод должен возвращать добавленную вершину - объект класса TreeObj);
#
#         В методе add_obj параметры имеют, следующие значения:
#
#         obj - ссылка на новый (добавляемый) объект решающего дерева (объект класса TreeObj);
#         node - ссылка на объект дерева, к которому присоединяется вершина obj;
#         left - флаг, определяющий ветвь дерева (объекта node), к которой присоединяется объект obj (True - к левой ветви; False - к правой)."""
#         if left == True:
#             node.left = obj
#         else:
#             node.right = obj
#         return obj
#
# class TreeObj:
#     def __init__(self, indx, value=None):
#         self.indx = indx
#         self.value = value
#         self.__left = None
#         self.__right = None
#
#
#     @property
#     def left(self):
#         return self.__left
#
#     @left.setter
#     def left(self, left):
#         self.__left = left
#
#     @property
#     def right(self):
#         return self.__right
#
#     @right.setter
#     def right(self, right):
#         self.__right = right
import math


class LineTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PathLines:

    def __init__(self, *args):
        self.coords = list((LineTo(0, 0), ) + args)


    def get_path(self):
        return self.coords

    def get_length(self):
        return self.coords[1]


pl = PathLines(LineTo(10, 20), LineTo(10, 30))

print(pl.get_length())





















class PhoneNumber:

    def __init__(self, number, fio):
        self.number = number
        self.fio = fio


class PhoneBook:


    def __init__(self):
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, indx):
        del self.phones[indx]

    def get_phone_list(self):
        return self.phones

























