# class AbstractClass:
#     def __new__(cls, *args, **kwargs):
#         return "Ошибка: нельзя создавать объекты абстрактного класса"


# class SingletonFive:
#
#     __instance = None
#     count = 0
#
#     def __new__(cls, *args, **kwargs):
#         if cls.count <= 5:
#             cls.__instance = super().__new__(cls)
#             cls.count += 1
#         else:
#             return cls.__instance
#
#     def __init__(self, *name):
#         self.name = name




# TYPE_OS = 1
#
# class DialogWindows:
#     name_class = "DialogWindows"
#
# class DialogLinux:
#     name_class = "DialogLinux"
#
# class Dialog:
#
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if TYPE_OS == 1:
#             cls.__instance = super().__new__(DialogLinux)
#         else:
#             cls.__instance = super().__new__(DialogWindows)
#
#         cls.__instance.name = args
#         return cls.__instance


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def clone(self):
#         return Point(self.x, self.y)
#
#
# pt = Point(3, 4)
# pt_clone = pt.clone()



class Loader:
    def parse_format(self, string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


class Factory:

    def build_sequence(self):
        empty_string = []
        return empty_string

    def build_number(string):
        return float(string)




r = Factory
print(r.build_number(4))

