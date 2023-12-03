class Clock:
    def __init__(self, time):
        self.__time = 10
        if self.__check_time(self.__time):
            self.__time = time

    @classmethod
    def __check_time(cls, tm):
        return type(tm) == int and 0 <= tm < 100000

    def get_time(self):
        return self.__time

    def set_time(self, tm):
        if self.__check_time(tm) == True:
            self.__time = tm


clock = Clock(4530)
clock.set_time(15)
print(clock.get_time())  #15
clock.set_time(100000)
clock.set_time(-1)
clock.set_time('2')
clock.set_time(0.1)
print(clock.get_time())  #15


class Money():
    def __init__(self, money):
        self.money = money

    def set_money(self, money):
        if  self.check_money(money) == True:
            self.money = money

    def get_money(self):
        return self.money

    def add_money(self, mn):
        self.money = self.money + mn.get_money()

    @classmethod
    def __check_money(self, money):
        if int(money) and money >= 0:
            return True
        else:
            return False


mn_1 = Money(10)
mn_2 = Money(20)
mn_1.set_money(100)
mn_2.add_money(mn_1)
m1 = mn_1.get_money()    # 100
m2 = mn_2.get_money()    # 120
print(m2)


class Book:

    def __init__(self, __author, __title, __price):
        self.__author = __author
        self.__title = __title
        self.__price = __price


    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_price(self, price):
        self.__price = price

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price


book = Book('50 Cent', 'Aboba', 999)
book.set_title('Amogus')
book.set_author('NLE Choppa')
book.set_price(123)
book.get_title()
book.get_author()
book.get_price()


class Line:

    def __init__(self, __x1, __y1, __x2, __y2):
        self.__x1 = __x1
        self.__y1 = __y1
        self.__x2 = __x2
        self.__y2 = __y2

    def set_coords(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def draw(self):
        print(
            self.__x1,
        self.__y1,
        self.__x2,
        self.__y2
        )


class Point:
    def __init__(self, __x, __y):
        self.__x = __x
        self.__y = __y

    def get_coords(self):
        return self.__x, self.__y


class Rectangle:
    def __init__(self, *args):
        if len(args) == 2:
            self.__sp = args[0]
            self.__ep = args[1]

        else:
            self.__sp = args[0], args[1]
            self.__ep = args[2], args[3]

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        print(self.__sp.get_coords(), self.__ep.get_coords())

rect = Rectangle(Point(0,0), Point(20, 34))



correct_let = 'qwertyuiopasdfghjklzxcvbnm1234567890_.@'

import string, random

class EmailValidator:
    # def __new__(cls, *args, **kwargs):
    #     return None

    @classmethod
    def get_random_email(cls):
        letters = string.ascii_lowercase
        rand_mail =  f"{''.join(random.choice(letters) for i in range(random.randint(7, 100)))}@gmail.com"
        return rand_mail

    @classmethod
    def check_email(cls, email):
        # a = list(map(lambda v: '..' in v, [email]))
        # if a:
        #     list(map(lambda v: '..' in v, [email]))
        pass
        #     if len(email.split('@'[0])) <= 100:
        #         if len(email.split('@')[1]) <= 50:
        #             if '.' in email.split('@')[1]:
        #                 return True
        # else:
        #     return '__False__'

    @staticmethod
    def __is_email_str(email):
        if isinstance(str, email):
            return True
        else:
            return False



a = EmailValidator
b = a.get_random_email()
# print(a.check_email(b))

s = "text text : one two three"
a = list(map(lambda v: '..' in v, [s]))
for x in a:
    pass

#ПОЧТИ ГОТОВО




