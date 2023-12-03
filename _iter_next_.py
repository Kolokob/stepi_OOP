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


