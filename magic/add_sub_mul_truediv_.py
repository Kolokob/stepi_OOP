import math

# TASK 1
class NewList:

    def __init__(self, initial_list=None):
        self.list = list(map(str, initial_list)) if initial_list is not None else []
        self.lst_copy = self.list[:]

    def get_list(self):
        for i in range(len(self.lst_copy)):
            try:
                self.lst_copy[i] = eval(self.lst_copy[i])
            except (NameError, SyntaxError):
                pass

        return self.lst_copy

    def __sub__(self, other):
        if isinstance(other, NewList):
            other = list(map(str, other.list))
        elif isinstance(other, list):
            other = list(map(str, other))

        for i in self.list:
            for k in other:
                if i == k:
                    self.lst_copy.remove(k)

        return NewList(self.lst_copy).get_list()

    def __rsub__(self, other):
        print('__rsub__')
        return NewList(other) - self

# TASK 2
class ListMath:

    def __init__(self, ini_lst=None):
        self.lst = ini_lst if ini_lst is not None else []
        self.lst_math = []
        for i in self.lst:
            if isinstance(i, (int, float)) and type(i) is not bool:
                self.lst_math.append(i)

    def __add__(self, other):
        new_list = [x + other for x in self.lst_math]
        return ListMath(new_list)

    def __radd__(self, other):
        return ListMath(self.lst_math) + other

    def __sub__(self, other):
        new_list = [x - other for x in self.lst_math]
        return ListMath(new_list)

    def __rsub__(self, other):
        new_list = [other - x for x in self.lst_math]
        return ListMath(new_list)

    def __mul__(self, other):
        new_list = [x * other for x in self.lst_math]
        return ListMath(new_list)

    def __rmul__(self, other):
        return ListMath(self.lst_math) * other

    def __truediv__(self, other):
        new_list = [x / other for x in self.lst_math]
        return ListMath(new_list)

    def __rtruediv__(self, other):
        new_list = [other / x for x in self.lst_math]
        return ListMath(new_list)

# TASK 3
class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value
class Stack:

    def __init__(self):
        self.top = None
        self.tail = None

    def push_back(self, obj):
        if self.top is None:
            self.top = obj
            self.tail = obj
        else:
            self.tail.next = obj
            obj.next = None
            self.tail = obj
        return self

    def get_data(self):
        result = []
        current = self.top
        while current:
            result.append(current.data.data)
            current = current.next
        return result

    def pop_back(self):
        n = self.top
        while n.next.next is not None:
            n = n.next

        self.tail = n
        self.tail.next = None

    def __add__(self, other):
        return self.push_back(other)

    def __mul__(self, other):
        for data in other:
            self.push_back(StackObj(data))
        return self

# TASK 4
class Book:

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
class Lib:

    def __init__(self):
        self.book_list = []

    def __add__(self, other):
        self.book_list.append(other)
        return self

    def __sub__(self, other):
        if isinstance(other, int):
            del self.book_list[other]
        else:
            self.book_list.remove(other)
        return self

    def __len__(self):
        return len(self.book_list)

# TASK 5
class Budget:

    def __init__(self):
        self.items = []

    def add_item(self, it):
        self.items.append(it.money)

    def remove_item(self, indx):
        del self.items[indx]

    def get_items(self):
        return self.items
class Item:

    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __add__(self, other):
        return self.money + other.money

    def __radd__(self, other):
        return self.money + other


# TASK 6
class Box3D:

    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth
        self.bar = [self.width, self.height, self.depth]

    def __add__(self, other):
        if type(other) is int:
            interm = [self.bar[i] + other for i in range(3)]
            return Box3D(interm[0], interm[1], interm[2])
        else:
            interm = [self.bar[i] + other.bar[i] for i in range(3)]
            return Box3D(interm[0], interm[1], interm[2])

    def __mul__(self, other):
        if type(other) is int:
            interm = [self.bar[i] * other for i in range(3)]
            return Box3D(interm[0], interm[1], interm[2])
        else:
            interm = [self.bar[i] * other.bar[i] for i in range(3)]
            return Box3D(interm[0], interm[1], interm[2])

    def __rmul__(self, other):
        return self * other

    def __sub__(self, other):
        if type(other) is int:
            interm = [self.bar[i] - other for i in range(3)]
            return Box3D(interm[0], interm[1], interm[2])
        else:
            interm = [self.bar[i] - other.bar[i] for i in range(3)]
            return Box3D(interm[0], interm[1], interm[2])

    def __floordiv__(self, other):
        if type(other) is int:
            interm = [self.bar[i] // other for i in range(3)]
            return Box3D(interm[0], interm[1], interm[2])
        else:
            interm = [self.bar[i] // other.bar[i] for i in range(3)]
            return Box3D(interm[0], interm[1], interm[2])


    def __mod__(self, other):
        if type(other) is int:
            interm = [self.bar[i] % other for i in range(3)]
            return Box3D(interm[0], interm[1], interm[2])
        else:
            interm = [self.bar[i] % other.bar[i] for i in range(3)]
            return Box3D(interm[0], interm[1], interm[2])

# TASK 7
class MaxPooling:

    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size

    def __call__(self, *args, **kwargs):
        matrix = args[0]
        if not all(len(row) == len(matrix[0]) and all(isinstance(num, (int, float)) for num in row) for row in matrix):
            raise ValueError("Неверный формат для первого параметра matrix.")
        output = []
        for i in range(0, len(matrix) - self.size[0] + 1, self.step[0]):
            row = []
            for j in range(0, len(matrix[0]) - self.size[1] + 1, self.step[1]):
                maximum = float('-inf')
                for di in range(self.size[0]):
                    for dj in range(self.size[1]):
                        if matrix[i + di][j + dj] > maximum:
                            maximum = matrix[i + di][j + dj]
                row.append(maximum)
            output.append(row)
        return output


mp = MaxPooling(step=(2, 2), size=(2, 2))
m1 = [[1, 10, 10], [5, 10, 0], [0, 1, 2]]
m2 = [[1, 10, 10, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
res1 = mp(m1)
res2 = mp(m2)

assert res1 == [[10]], "неверный результат операции MaxPooling"
assert res2 == [[10, 12], [40, 300]], "неверный результат операции MaxPooling"

mp = MaxPooling(step=(3, 3), size=(2, 2))
m3 = [[1, 12, 14, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
res3 = mp(m3)
assert res3 == [[12]], "неверный результат операции при MaxPooling(step=(3, 3), size=(2,2))"

try:
    res = mp([[1, 2], [3, 4, 5]])
except ValueError:
    assert True
else:
    assert False, "некорректо отработала проверка (или она отсутствует) на не прямоугольную матрицу"

try:
    res = mp([[1, 2], [3, '4']])
except ValueError:
    assert True
else:
    assert False, "некорректо отработала проверка (или она отсутствует) на не числовые значения в матрице"

mp = MaxPooling(step=(1, 1), size=(5, 5))
res = mp([[5, 0, 88, 2, 7, 65],
          [1, 33, 7, 45, 0, 1],
          [54, 8, 2, 38, 22, 7],
          [73, 23, 6, 1, 15, 0],
          [4, 12, 9, 1, 76, 6],
          [0, 15, 10, 8, 11, 78]])  # [[88, 88], [76, 78]]

assert res == [[88, 88], [76, 78]], "неверный результат операции MaxPooling(step=(1, 1), size=(5, 5))"


# [1, 2, 3, 4]
# [5, 6, 7, 8]
# [9, 8, 7, 6]
# [5, 4, 3, 2]

# 1 10 10
# 5 10 0
# 0 1  2