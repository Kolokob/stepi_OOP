from string import ascii_lowercase, digits


# TASK 1
class LoginForm:
    def __init__(self, name, validators=None):
        self.name = name
        self.validators = validators
        self.login = ""
        self.password = ""

    def post(self, request):
        self.login = request.get('login', "")
        self.password = request.get('password', "")

    def is_validate(self):
        if not self.validators:
            return True

        for v in self.validators:
            if not v(self.login) or not v(self.password):
                return False

        return True


class LengthValidator:

    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, login, *args, **kwargs):
        if self.min_length <= len(login) <= self.max_length:
            return True
        else:
            return False


class CharsValidator:

    def __init__(self, chars):
        self.chars = chars

    def __call__(self, login, *args, **kwargs):

        if all(char in self.chars for char in login):
            return True
        else:
            return False


lg = LoginForm("Вход на сайт", validators=[LengthValidator(3, 50), CharsValidator(ascii_lowercase + digits)])
lg.post({"login": "root", "password": "panda"})
if lg.is_validate():
    print("Дальнейшая обработка данных формы")

print(lg.is_validate())


# TASK 2
class DigitRetrieve:

    def __call__(self, *args, **kwargs):

        num = args[0]
        try:
            return int(num)
        except ValueError:
            return 'Неверный тип данных'


dg = DigitRetrieve()
assert dg("123") == 123, "объект класса DigitRetrieve вернул неверное значение"


# TASK 3
class RenderList:

    def __init__(self, param):
        self.param = param

    def render(self):
        if self.param == 'ul':
            tag = 'ul'

        elif self.param == 'ol':
            tag = 'ol'

        else:
            tag = 'ul'

        list_items = ''.join([f" <li><{item}></li>\n" for item in self.lst])
        return f"<{tag}>\n{list_items}</tag>"

    def __call__(self, lst, *args, **kwargs):
        self.lst = lst
        return self.render()


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList('ol')
html = render(lst)
print(html)
print(html.replace(' ', '').replace('\n', '').strip())


# TASK 4
class Handler:

    def __init__(self, methods=('GET',)):
        self.methods = methods

    def __call__(self, func, *args, **kwargs):
        def wrapper(request):
            m = request.get('method')
            if m in self.methods:
                method = m.lower()
                return self.__getattribute__(method)(func, request)
            elif m is None:
                return self.__getattribute__('get')(func, request)

        return wrapper

    def get(self, func, request):
        return f"GET: {func(request)}"

    def post(self, func, request):
        return f"POST: {func(request)}"


@Handler(methods=('GET', 'POST'))
def contact2(request):
    return "контакты"


assert contact2({}) == "GET: контакты", "декорированная функция вернула неверные данные при указании пустого словаря"


# TASK 5

class InputDigits:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args)
        result = result.split()
        return [int(i) for i in result]


@InputDigits
def input_dg(prompt=""):
    return input(prompt)


user_input = input_dg("Введите список ")


# TASK 5

class InputValues:
    def __init__(self, render):  # render - ссылка на функцию или объект для преобразования
        self.render = render

    def __call__(self, func):  # func - ссылка на декорируемую функцию
        def wrapper(*args, **kwargs):
            user_input = func(*args, **kwargs)
            return self.render()(user_input)

        return wrapper


class RenderDigit:
    def __call__(self, *args, **kwargs):
        values = args[0].split()
        result = []
        for value in values:
            try:
                result.append(int(value))
            except ValueError:
                result.append(None)
        return result


@InputValues(render=RenderDigit)
def input_dg(prompt=""):
    return input(prompt)


res = input_dg()
print(res)
