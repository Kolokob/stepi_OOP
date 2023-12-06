
class Factory:
    @staticmethod
    def build_sequence():
        empty_string = []
        return empty_string

    @staticmethod
    def build_number(string):
        return float(string)



class Loader:
    @staticmethod
    def parse_format(string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq

res = Loader.parse_format("1, 2, 3, -5, 10", Factory)





import re
from string import ascii_lowercase, digits

CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
CHARS_CORRECT = CHARS + CHARS.upper() + digits

class TextInput:
    def __init__(self, name, size = 10):
        self.check_name(name)
        self.name = name
        self.size = size

    def get_html(self):
         return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"




    @classmethod
    def check_name(cls, name):
        for x in name:
            if x not in CHARS_CORRECT or 3 > len(name) or len(name) > 50:
                raise ValueError('некорректное имя поля')


class PasswordInput:
    def __init__(self, name, size = 10):
        self.check_name(name)
        self.name = name
        self.size = size
    def get_html(self):
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"

    @classmethod
    def check_name(cls, name):
        for x in name:
            if x not in CHARS_CORRECT or 3 > len(name) or len(name) > 50:
                raise ValueError('некорректное имя поля')

class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])



login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()

# CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
# CHARS_CORRECT = CHARS + CHARS.upper() + digits

# import re
# from string import ascii_lowercase, digits
# ascii_lowercase = "qwertyuiopasdfghjklzxcvbnm "
# CHARS_FOR_NAME = ascii_lowercase.upper() + digits
#
# class CardCheck:
#
#     @classmethod
#     def check_card_number(cls, number):
#         if re.match(r'\d{4}-\d{4}-\d{4}-\d{4}$', number):
#             return True
#         else:
#             return False
#
#     @staticmethod
#     def check_name(name):
#         if re.match(r'[A-Z]+\s[A-Z]+$', name):
#             return True
#         else:
#             return False
#
#
# is_name = CardCheck.check_name("SERGEI BALAKIREV NAM")
# print(is_name)

# class Video:
#
#     def create(self, name):
#         self.name = name
#
#     def play(self, name):
#         return f"воспроизведение видео {name}"
#
# class YouTube:
#
#     videos = []
#
#     @classmethod
#     def add_video(cls, video):
#         cls.videos.append(video)
#
#     @classmethod
#     def play(cls, video_indx):
#         cls.videos[video_indx].play()
#
#
#
# v1 = Video()
# v1.create('Python')
# v1.create(v1.name)
# print(v1.play())



# class AppStore:
#
#     store = {}
#
#     def add_application(self, app):
#         self.store[id(app)] = app
#
#     def remove_application(self, app):
#         self.store.pop(id(app))
#
#     def block_application(self, app):
#         obj = self.store.get(id(app), False)
#         if not obj:
#             return False
#         obj.bloked = True
#         return True
#
#     def total_apps(self):
#         return len(self.store)
#
#
# class Application:
#     def __init__(self, name):
#         self.name = name
#         self.blocked = False

# class Viber:
#
#     message = {}
#
#     @classmethod
#     def add_message(cls, msg):
#         cls.message[id(msg)] = msg
#
#     @classmethod
#     def remove_message(cls, msg):
#         cls.message.pop(id(msg))
#
#     @classmethod
#     def set_like(cls, msg):
#         msg.fl_like = not msg.fl_like
#
#     @classmethod
#     def show_last_message(cls, number):
#         for i in tuple(cls.message.values()[-number:]):
#             return i
#
#     @classmethod
#     def total_messages(self):
#         return self.message
#
# class Message:
#     def __init__(self, text):
#         self.text = text
#         self.fl_like = False

# class Viber:
#
#     message = {}
#
#     @classmethod
#     def add_message(cls, msg):
#         cls.message[id(msg)] = msg
#
#     @classmethod
#     def remove_message(cls, msg):
#         if id(msg) in cls.message:
#             cls.message.pop(id(msg))
#
#     @classmethod
#     def set_like(cls, msg):
#         msg.fl_like = not msg.fl_like
#
#     @classmethod
#     def show_last_message(cls, number):
#         for i in tuple(cls.message[-number:]):
#             print(i)
#
#
#     @classmethod
#     def total_messages(cls):
#         return len(cls.message)
#
# class Message:
#     def __init__(self, text):
#         self.text = text
#         self.fl_like = False
