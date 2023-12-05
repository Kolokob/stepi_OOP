import copy
# TASK 1
class Animal:

    def __init__(self, name, old):
        self.name = name
        self.old = old
class Dog(Animal):

    def __init__(self, name, old, breed, size):
        super().__init__(name, old)
        self.breed = breed
        self.size = size

    def get_info(self):
        return f"{self.name}: {self.old}, {self.breed}, {self.size}"
class Cat(Animal):
    def __init__(self, name, old, color, weight):
        super().__init__(name, old)
        self.color = color
        self.weight = weight

    def get_info(self):
        return f"{self.name}: {self.old}, {self.color}, {self.weight}"


# TASK 2
class Thing:
    ID = 1

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.id = self.ID
        Thing.ID += 1
        self.weight = self.dims = self.memory = self.frm = None

    def get_data(self):
        return self.id, self.name, self.price, self.weight, self.dims, self.memory, self.frm
class Table(Thing):
    def __init__(self, name, price, weight=None, dims=None):
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims
class ElBook(Thing):

    def __init__(self, name, price, memory=None, frm=None):
        super().__init__(name, price)
        self.memory = memory
        self.frm = frm


# TASK 3
class GenericView:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass
class DetailView(GenericView):

    def __init__(self, methods=('GET',)):
        super().__init__(methods=methods)

    def render_request(self, request, method):
        if method not in self.methods:
            raise TypeError('данный запрос не может быть выполнен')
        self.get(request)
        return getattr(self, method.lower())(request)

    def get(self, req):
        if not isinstance(req, dict):
            raise TypeError('request не является словарем')
        if 'url' not in req:
            raise TypeError('request не содержит обязательного ключа url')

        return f"{list(req.keys())[0]}: {list(req.values())[0]}"


# TASK 4
class Singleton:
    __instanse = None
    __instanse_base = None

    def __new__(cls, *args, **kwargs):

        if cls == Singleton:
            if cls.__instanse is None:
                cls.__instanse_base = super().__new__(cls)
                return cls.__instanse_base

        if cls.__instanse is None:
            cls.__instanse = super().__new__(cls)
            return cls.__instanse
        return cls.__instanse
class Game(Singleton):

    def __init__(self, name):
        if 'name' not in self.__dict__:
            self.name = name


# TASK 5
class Validator:

    def _is_valid(self, data):
        return True

    def __call__(self, data):
        if not self._is_valid(data):
            raise ValueError('данные не прошли валидацию')
        return True
class IntegerValidator(Validator):

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, num):
        if isinstance(num, int) and self.min_value <= num <= self.max_value:
            return True
        return False
class FloatValidator(Validator):

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, num):
        if isinstance(num, float) and self.min_value <= num <= self.max_value:
            return True
        return False


# TASK 6
# BIG TASK
class Layer:

    def __init__(self):
        self.next_layer = None
        self.name = 'Layer'

    def __call__(self, data):
        self.next_layer = data
        return data
class Input(Layer):

    def __init__(self, inputs):
        super().__init__()
        self.inputs = inputs
        self.name = 'Input'
class Dense(Layer):

    def __init__(self, inputs, outputs, activation):
        super().__init__()
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation
        self.name = 'Dense'
class NetworkIterator:

    def __init__(self, net):
        self.net = net
        self.counter = 0


    def __iter__(self):
        for i in range(4):
            yield self.net.next_layer


# TASK 7
class Vector:

    def __init__(self, *args):
        self.nums = [i for i in args]

    def __add__(self, other):
        if len(self.nums) != len(other.nums):
            raise TypeError('размерности векторов не совпадают')

        temp = copy.deepcopy(self.nums)

        for i in range(len(temp)):
            temp[i] += other.nums[i]

        return Vector(temp)

    def __sub__(self, other):

        if len(self.nums) != len(other.nums):
            raise TypeError('размерности векторов не совпадают')

        temp = copy.deepcopy(self.nums)

        for i in range(len(temp)):
            temp[i] -= other.nums[i]

        return Vector(temp)

    def get_coords(self):
        return tuple(self.nums[0])
class VectorInt(Vector):

    def __init__(self, *args):
        for i in args:
            if not isinstance(i, int):
                raise ValueError('координаты должны быть целыми числами')
        super().__init__(*args)

    def __add__(self, other):
        result = super().__add__(other)
        if all(isinstance(x, int) for x in result.get_coords()):
            return VectorInt(*result.get_coords())
        return result

    def __sub__(self, other):
        result = super().__add__(other)
        if all(isinstance(x, int) for x in result.get_coords()):
            return VectorInt(*result.get_coords())
        return result


