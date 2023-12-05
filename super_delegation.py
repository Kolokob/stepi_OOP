# TASK 1
class Book:

    def __init__(self, title, author, pages, year):
        self.title = title
        self.authorr = author
        self.pages = pages
        self.year = year


class DigitBook(Book):

    def __init__(self, title, author, pages, year, size, frm):
        super().__init__(title, author, pages, year)
        self.size = size
        self.frm = frm


# TASK 2
class Thing:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
class ArtObject(Thing):
    def __init__(self, name, weight, author, date):
        super().__init__(name, weight)
        self.author = author
        self.date = date
class Computer(Thing):
    def __init__(self, name, weight, memory, cpu):
        super().__init__(name, weight)
        self.memory = memory
        self.cpu = cpu
class Auto(Thing):
    def __init__(self, name, weight, dims):
        super().__init__(name, weight)
        self.dims = dims
class Mercedes(Auto):

    def __init__(self, name, weight, dims, model, old):
        super().__init__(name, weight, dims)
        self.model = model
        self.old = old
class Toyota(Auto):
    def __init__(self, name, weight, dims, model, wheel):
        super().__init__(name, weight, dims)
        self.model = model
        self.wheel = wheel

# TASK 3

class SellItem:

    def __init__(self, name, price):
        self.name = name
        self.price = price

class House(SellItem):

    def __init__(self, name, price, material, square):
        super().__init__(name, price)
        self.material = material
        self.square = square

class Flat(SellItem):
    def __init__(self, name, price, size, rooms):
        super().__init__(name, price)
        self.size = size
        self.rooms = rooms

class Land(SellItem):

    def __init__(self, name, price, square):
        super().__init__(name, price)
        self.square = square


class Agency:

    def __init__(self, name):
        self.name = name
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

    def remove_object(self, obj):
        del self.objects[self.objects.index(obj)]


    def get_objects(self):
        return self.objects

