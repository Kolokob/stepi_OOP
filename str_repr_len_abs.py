import math


# TASK 1
class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Книга: {self.title}; {self.author}; {self.pages}"


lst_in = ['Python ООП', 'Балакирев С.М.', '1024']
book = Book(lst_in[0], lst_in[1], lst_in[2])


# TASK 2
class Model:

    def __init__(self):
        self.data = "Model"

    def query(self, **kwargs):
        if kwargs:
            self.data = "Model:"
            items = [f'{key} = {item}' for key, item in kwargs.items()]
            self.data += ' ' + ', '.join(items)

    def __str__(self):
        return f'{self.data}'


# model = Model()
# model.query(id=1, fio='Sergey', old=33)
# print(model)

# TASK 3
class WordString:

    def __init__(self, string=None):
        self.__sentence = string

    def __call__(self, *args, **kwargs):
        return self.__sentence.split()[args[0]]

    def __len__(self):
        return len(self.__sentence.split())

    @property
    def string(self):
        return self.__sentence

    @string.setter
    def string(self, strs):
        self.__sentence = strs


# words = WordString()
# words.string = "Курс по Python ООП"
# n = len(words)
# first = "" if n == 0 else words(0)
# print(words.string)
# print(f"Число слов: {n}; первое слово: {first}")


# TASK 4
class ObjList:
    def __init__(self, data):
        self.data = data
        self.__next = None
        self.__prev = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, value):
        self.__prev = value

class LinkedList:

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def add_obj(self, obj):
        if self.head is None:
            new_node = obj
            self.head = new_node
            self.tail = new_node
        elif self.head is not None:
            new_node = obj
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def remove_obj(self, indx):
        counter = 0
        n = self.head
        self.stop = False
        while n.next is not None and counter < indx:
            n = n.next
            counter += 1
        if indx > counter:
            self.stop = True
        else:
            if n.prev and n.next:
                left = n.prev
                right = n.next
                left.next = right
                right.prev = left
            elif not n.prev and n.next:
                ptr = self.head.next
                ptr.prev = None
                self.head = ptr
            elif not n.next and n.prev:
                ptr = self.tail.prev
                ptr.next = None
                self.tail = ptr
            elif not n.prev and not n.next:
                self.head = None
                self.tail = None

    def get_data(self):
        result = []
        if self.head is None:
            return []
        else:
            n = self.head
            while n.next is not None:
                result.append(n.data)
                n = n.next
            result.append(n.data)
            return result

    def get_by_index(self, indx):
        counter = 0
        n = self.head
        while n.next is not None and counter < indx:
            n = n.next
            counter += 1
        return n.data

    def __len__(self):
        return len(self.get_data())

    def __call__(self, *args, **kwargs):
        return self.get_by_index(args[0])


# ln = LinkedList()
# ln.add_obj(ObjList("Сергей"))
# ln.add_obj(ObjList("Балакирев"))
# ln.add_obj(ObjList("Python ООП"))
# ln.remove_obj(2)
# ln.remove_obj(0)
# ln.remove_obj(0)
# print(ln.get_data())

# TASK 5
class Complex:

    def __init__(self, real, img):
        self._real = real
        self._img = img

    @property
    def real(self):
        return self._real

    @real.setter
    def real(self, value):
        if isinstance(value, (int, float)):
            self._real = value
        else:
            raise ValueError("Неверный тип данных.")

    @property
    def img(self):
        return self._img

    @img.setter
    def img(self, value):
        if isinstance(value, (int, float)):
            self._img = value
        else:
            raise ValueError("Неверный тип данных.")

    def __abs__(self):
        return math.sqrt(self._real * self._real + self._img * self._img)


# cmp = Complex(7, 8)
# cmp.real = 3
# cmp.img = 4
# c_abs = abs(cmp)


# TASK 6
class RadiusVector:

    def __init__(self, *coords):
        self.coords = coords
        if len(coords) == 1:
            self.coords = [0 for i in range(coords[0])]
        elif len(coords) > 1:
            self.coords = coords

    def get_coords(self):
        return tuple(self.coords)

    def set_coords(self, *args):
        self.coords = [i for i in self.coords]
        for i in range(len(self.coords)):
            if len(args) > i:
                self.coords[i] = args[i]

    def __len__(self):
        return len(self.coords)

    def __abs__(self):
        return math.sqrt(sum([i * i for i in self.coords]))


# TASK 7
class DeltaClock:

    def __init__(self, clock1, clock2):
        self.clock1 = clock1
        self.clock2 = clock2

    def __len__(self):
        return self.clock1.get_time() - self.clock2.get_time()

    def __str__(self):
        res = [self.clock1.hours - self.clock2.hours, self.clock1.minutes - self.clock2.minutes,
               self.clock1.seconds - self.clock2.seconds]
        for i in range(len(res)):
            if res[i] <= 0:
                res[i] = '00'
            res[i] = str(res[i]).zfill(2)
        return f"{':'.join(list(map(str, res)))}"


class Clock:

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return (self.hours * 3600) + (self.minutes * 60) + self.seconds

# dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
# print(dt) # 01: 30: 00
# len_dt = len(dt) # 5400


# TASK 8
class Recipe:

    def __init__(self, *args):
        self.ingredients = []
        for arg in args:
            self.ingredients.append(arg)
    def add_ingredient(self, ing):
        print(self.ingredients)
        self.ingredients.append(ing)

    def remove_ingredient(self, ing):
        self.ingredients.remove(ing)

    def get_ingredients(self):
        return self.ingredients

    def __len__(self):
        return len(self.get_ingredients())
class Ingredient:

    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self):
        return f"{self.name}: {self.volume}, {self.measure}"

# i1 = Ingredient("Соль", 1, "столовая ложка")
# i2 = Ingredient("Мука", 1, "кг")
# i3 = Ingredient("Мясо баранины", 10, "кг")
# i4 = Ingredient("Масло", 100, "гр")
# recipe = Recipe(i1, i2, i3)
# recipe.add_ingredient(i4)
# recipe.remove_ingredient(i3)

# TASK 9
class PolyLine:

    def __init__(self, start_coord, *args):
        self.start_coord = start_coord
        self.coords = list(args) + [start_coord]

    def add_coord(self, x, y):
        self.coords.append((x, y))

    def remove_coord(self, indx):
        self.coords.pop(indx)

    def get_coords(self):
        return self.coords



mp = MaxPooling(step=(2, 2), size=(2,2))
res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])    # [[6, 8], [9, 7]]


