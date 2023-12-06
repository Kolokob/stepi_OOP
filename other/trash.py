# #      1
# #     121
# #    12321
# #   1234321
# #  123454321
# #      |
# def palindrome_xmas_tree(lst):
#     counter = len(lst) + 1
#     for i in range(1, counter):
#         up = ''.join(map(str, lst[:i]))
#         down = ''.join(map(str, lst[i-2::-1])) if i > 1 else ''
#         line = up + down
#
#         print(' ' * (counter - i) + line)
#
#     print(' ' * (counter-1) + '|')
#
# a = palindrome_xmas_tree([1, 2, 3, 4, 5, 6, 7])


class PersonDescriptors:

    def __init__(self, data_type):
        self.data_type = data_type

    def __set_name__(self, owner, name):
        self.name = '_' + owner.__name__ + '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


    def __set__(self, instance, value):
        if not isinstance(value, self.data_type):
            raise TypeError(f"Expected {self.data_type}, got {type(value)}")

        setattr(instance, self.name, value)

class Person:
    name = PersonDescriptors(str)
    age = PersonDescriptors(int)

    def __init__(self, name, age):
        self.name = name
        self.age = age

sp = Person('nick', 18)


