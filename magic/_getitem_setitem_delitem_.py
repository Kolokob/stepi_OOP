# TASK 1
class Record:

    def __init__(self, **kwargs):
        self.attrs = tuple(self.__dict__.keys())

    def __setitem__(self, key, value):
        setattr(self, self.attrs[key], value)

    def __getitem__(self, item):
        try:
            return self.__dict__[item]
        except KeyError:
            raise IndexError('неверный индекс поля')


# TASK 2
class Track:

    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.coords = []

    def add_point(self, x, y, speed):
        self.coords.append([(x, y), speed])

    def check_coords(self, value):
        if isinstance(value, int) and 0 <= value < len(self.coords):
            return True
        else:
            raise IndexError('некорректный индекс')

    def __getitem__(self, item):
        self.check_coords(item)
        return self.coords[item][:2]

    def __setitem__(self, key, value):
        self.check_coords(key)
        self.coords[key][-1] = value


# TASK 3
class Array:

    def __init__(self, max_length, cell):
        self._elements = [cell() for _ in range(max_length)]

    def __getitem__(self, index):
        if not isinstance(index, int) or index < 0 or index >= len(self._elements):
            raise IndexError('неверный индекс для доступа к элементам массива')
        return self._elements[index].value

    def __setitem__(self, index, value):
        if not isinstance(index, int) or index < 0 or index >= len(self._elements):
            raise IndexError('неверный индекс для доступа к элементам массива')
        self._elements[index].value = value

    def __str__(self):
        return ' '.join(str(element.value) for element in self._elements)
class Integer:

    def __init__(self, start_value=0):
        self.integer = start_value

    @property
    def value(self):
        return self.integer

    @value.setter
    def value(self, key):
        if not isinstance(key, int):
            raise ValueError('должно быть целое число')
        self.integer = key


# BIG TASK 4
# НУ ПОГНАЛИ
class IntegerValue:
    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}_{name}'

    def __get__(self, obj, objtype):
        return getattr(obj, self.name, None)

    def __set__(self, obj, value):
        if not isinstance(value, int):
            raise ValueError('возможны только целочисленные значения')
        setattr(obj, self.name, value)
class CellInteger:
    # для операций с целыми числами;
    value = IntegerValue()

    def __init__(self, start_value=0):
        self.value = start_value
class TableValues:
    # для работы с таблицей в целом;
    def __init__(self, rows, cols, cell=CellInteger):
        self.rows = rows
        self.cols = cols
        if not cell:
            raise ValueError('параметр cell не указан')
        else:
            self.cells = tuple(tuple(cell(start_value=0) for _ in range(cols)) for _ in range(rows))

    def __getitem__(self, item):
        row, col = [int(i) for i in item]
        return self.cells[row][col].value

    def __setitem__(self, key, value):
        row, col = [int(i) for i in key]
        self.cells[row][col].value = value


# TASK 5
class StackObj:

    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:

    def __init__(self):
        self.top = None
        self.tail = None

    def push(self, obj):
        if self.top is None:
            self.top = obj
            self.tail = obj
        else:
            self.tail.next = obj
            obj.next = None
            self.tail = obj
        return self

    def pop(self):
        n = self.top
        while n.next.next is not None:
            n = n.next
        removed = n.next
        self.tail = n
        self.tail.next = None
        return removed



    def get_data(self):
        result = []
        current = self.top
        while current:
            result.append(current)
            current = current.next
        return result

    def __getitem__(self, item):
        return self.get_data()[item]

    def __setitem__(self, key, value):
        if key < 0 or not isinstance(key, int) or key > len(self.get_data()):
            raise IndexError('неверный индекс')

        if key == 0:
            node = value
            node.next = self.top
            self.top = node

        n = self.top
        counter = 0
        while counter < key and n.next is not None:
            left = n
            n = n.next
            counter += 1
        right = n.next
        left.next = value
        value.next = right


# TASK 6
class RadiusVector:

    def __init__(self, *args):
        self.coords = list(args)

    def __getitem__(self, item):
        print(item)
        return tuple(self.coords[item]) if type(item) == slice else self.coords[item]

    def __setitem__(self, key, value):
        self.coords[key] = value

# TASK 7
class TicTacToe:

    def __init__(self):
        self.pole = [[Cell(False) for i in range(3)] for j in range(3)]

    def clear(self):
        self.pole = [[Cell(False, 0) for i in range(3)] for j in range(3)]

    def __setitem__(self, key, value):
        r, c = key
        if r > 2 or c > 2:
            raise IndexError('неверный индекс клетки')
        for i in range(3):
            for j in range(3):
                self.pole[r][c] = Cell(True, value)

    def __getitem__(self, item):
        r, c = item
        if type(self.pole[r][c]) is not list:
            return self.pole[r][c].value

        if isinstance(r, slice):
            return tuple(self.pole[i][c].value for i in range(3))

        return tuple(i.value for i in self.pole[r][c])
class Cell:

    def __init__(self, is_free = False, value=0):
        self.is_free = is_free
        self.value = value

    def __bool__(self):
        return True if self.is_free else False


# TASK 8
# RELAX
class Thing:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
class Bag:

    WEIGHT = 0

    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.bag = []

    def add_thing(self, thing):
        self.WEIGHT += thing.weight
        if self.WEIGHT > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')
        self.bag.append(thing)

    def __getitem__(self, item):
        try:
            return self.bag[item]
        except IndexError:
            raise IndexError('неверный индекс')

    def __setitem__(self, key, value):
        try:
            if self.bag[key]:
                self.WEIGHT -= self.bag[key].weight
                self.WEIGHT += value.weight
            if self.WEIGHT > self.max_weight:
                raise ValueError('превышен суммарный вес предметов')
            self.bag[key] = value
        except IndexError:
            raise IndexError('неверный индекс')


    def __delitem__(self, key):
        try:
            self.WEIGHT -= self.bag[key].weight
            del self.bag[key]
        except IndexError:
            raise IndexError('неверный индекс')

# TASK 9
class Cell:

    def __init__(self, value=0):
        self.value = value
class SparseTable:

    def __init__(self, rows=0, cols=0):
        self.rows = rows
        self.cols = cols
        self.value = {}

    def add_data(self, row, col, data):
        self.value[(row, col)] = data
        self.rows = max(row for row, _ in self.value) + 1
        self.cols = max(col for _, col in self.value) + 1

    def remove_data(self, row, col):
        if not (row, col) in self.value:
            raise IndexError('ячейка с указанными индексами не существует')
        del self.value[(row, col)]
        self.rows = max(row for row, _ in self.value) + 1
        self.cols = max(col for _, col in self.value) + 1

    def __getitem__(self, item):
        r, c = item
        if not (r, c) in self.value:
            raise ValueError('данные по указанным индексам отсутствуют')
        return self.value[(r, c)]

    def __setitem__(self, key, value):
        r, c = key
        self.value[(r, c)] = value
        self.rows = max(row for row, _ in self.value) + 1
        self.cols = max(col for _, col in self.value) + 1




