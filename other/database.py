class DataBase:
    def __init__(self, title, author, views, comments, pk = 1, ):
        self.pk = pk
        self.title = title
        self.author = author
        self.views = views
        self.comments = comments

    def __init__(self, title, author, views, comments,  pk = 1):
        self.title = title
        self.author = author
        self.views = views
        self.comments = comments
        self.pk = pk

emp = DataBase("Классы и объекты", "Сергей Балакирев", 14356, 12)
print(emp)

class Goods:
    title = "Мороженое"
    weight =  154
    tp =  "Еда"
    price =  1024



getattr(Goods, 'price', 2048)
setattr(Goods, "inflation", 100)

class Car:
    pass

setattr(Car, 'model', "Тойота")
setattr(Car, 'color', "Розовый")
setattr(Car, 'number', "П111УУ77")

print(Car.__dict__['color'])

class Goods:

    uid =  1005435
    title = "Шутка"
    author = "И.С. Бах"
    pages = 2

print(getattr(Goods, 'author'))

class Dictionary:
    rus = "Питон"
    eng = "Python"

print(getattr(Dictionary, 'rus_word', False))

class TravelBlog:
    total_blogs = 0

tb1 = TravelBlog
tb1.name = 'Франция'
tb1.days = 6
TravelBlog.total_blogs += 1

tb2 = TravelBlog()
tb2.name = 'Италия'
tb2.days = 5
TravelBlog.total_blogs += 1

class Figure:
    type_fig = 'ellipse'
    color = 'red'

fig1 = Figure()
fig1.start_pt = (10, 5)
fig1.end_pt = (100, 20)
fig1.color = 'blue'

del fig1.color
print(*fig1.__dict__)

class Person:
    name = 'Сергей Балакирев'
    job = 'Программист'
    city = 'Москва'

p1 = Person
print(hasattr(p1.__dict__, 'job'))
