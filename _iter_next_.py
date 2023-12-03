# TASK 1
class Person:

    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self.employee = [fio, job, old, salary, year_job]
        self.index = 0

    def check_indx(self, indx):
        if isinstance(indx, int) and 0 <= indx <= 4:
            return True
        else:
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.check_indx(item)
        return self.employee[item]

    def __setitem__(self, key, value):
        self.check_indx(key)
        self.employee[key] = value

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.employee):
            result = self.employee[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

# TASK 2
class TriangleListIterator:
    def __init__(self, lst):
        self._lst = lst

    def __iter__(self):
        for i in range(len(self._lst)):
            for j in range(i + 1):
                yield self._lst[i][j]

# TASK 3
class IterColumn:
    def __init__(self, lst, column):
        self.lst = lst
        self.column = column

    def __iter__(self):
        for i in self.lst:
            yield i[self.column]

# TASK 4
class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:

    def __init__(self):
        self.top = None
        self.tail = None

    def push_front(self, obj):
        if self.top is None:
            self.top = obj
            self.tail = obj
        else:
            node = obj
            node.next = self.top
            self.top = node

    def push_back(self, obj):
        node = obj
        if self.tail is not None:
            self.tail.next = node
            node.next = None
            self.tail = node
        else:
            self.push_front(obj)

    def get_data(self):
        result = []
        current = self.top
        while current:
            result.append(current.data)
            current = current.next
        return result

    def get_data_for_iter(self):
        result = []
        current = self.top
        while current:
            result.append(current)
            current = current.next
        return result

    def __getitem__(self, item):
        return self.get_data()[item]

    def __setitem__(self, key, value):
        value = StackObj(value)
        if key < 0 or not isinstance(key, int) or key > len(self.get_data()):
            raise IndexError('неверный индекс')

        if key == 0:
            node = StackObj(value)
            node.next = self.top
            self.top = node.data
            return

        n = self.top
        counter = 0
        if not isinstance(value, StackObj):
            value = StackObj(value)
        while counter < key and n.next is not None:
            left = n
            n = n.next
            counter += 1
        right = n.next
        left.next = value
        value.next = right

    def __len__(self):
        return len(self.get_data())

    def __iter__(self):
        for i in self.get_data_for_iter():
            yield i

# TASK 5
class Cell:

    def __init__(self, data):
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value
class TableValues:

    def __init__(self, rows=0, cols=0, type_data=int):
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self.cells = [[Cell(0) for i in range(rows)] for j in range(cols)]

    def check_indexes(self, value):
        r, c = value
        if isinstance(value, int):
            if r > self.rows or c > self.cells:
                raise IndexError('неверный индекс')
            else:
                return True
    def __setitem__(self, key, value):
        self.check_indexes(key)
        if type(value) is not self.type_data:
            raise TypeError('неверный тип присваиваемых данных')
        r, c = key
        self.cells[r][c] = value

    def __getitem__(self, item):
        self.check_indexes(item)
        r, c = item
        return self.cells[r][c]

    def __iter__(self):
        for i in self.cells:
            yield (j.data for j in i)


