# class MediaPlayer:
#
#     def open(self, filename):
#         self.filename = filename
#
#     def play(self):
#         return f"Воспроизведение {self.filename}"
#
# media1 = MediaPlayer()
# media2  = MediaPlayer()
#
# media1.open('filemedia1')
# media2.open('filemedia2')
#
# print(media1.play())
# print(media2.play())

# class Graph:
#
#     def set_data(self, data):
#         self.data = data
#
#     def draw(self):
#         LIMIT_Y = [0, 10]
#         print(' '.join(map(str, filter(lambda x: LIMIT_Y[0] <= x <= LIMIT_Y[1], self.data))))
#
#
# graph_1 = Graph()
# graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
# graph_1.draw()


# import sys
#
# class StreamData:
#     def create(self, fields, lst_values):
#         if len(lst_values) != len(fields):
#             return False
#
#         for i, key in enumerate(fields):
#             setattr(self, key, lst_values[i])
#
#         return True
#
# class StreamReader(StreamData):
#     FIELDS = ('id', 'title', 'pages')
#
#     def readlines(self):
#         lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
#         sd = StreamData()
#         res = sd.create(self.FIELDS, lst_in)
#         return sd, res
#
# sr = StreamReader()
# data, result = sr.readlines()

# import sys
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# class DataBase:
#
#     lst_data = []
#     FIELDS = ('id', 'name', 'old', 'salary')
#
#     def select(self, a, b):
#         return self.lst_data[a : b + 1]
#
#
#     def insert(self, data):
#         for x in data:
#             self.lst_data.append(dict(zip(self.FIELDS, x.split())))
#
# db = DataBase()
# db.insert(lst_in)

class Translator:

    d = {}
    def add(self, eng, rus):
        if eng not in self.d:
            self.d[eng] = []

        self.d[eng].append(rus)


    def remove(self, eng):
        del self.d[eng]

    def translate(self, eng):
        print(*self.d[eng])

tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")

tr.remove('car')

tr.translate('go')

# class Translator:
#
#     def add(self, eng, rus):
#         if 'tr' not in self.__dict__:
#             self.tr = {}
#
#         self.tr.setdefault(eng, [])
#
#         if rus not in:
#             return self.tr[eng].append(rus)
#         else:
#             return False