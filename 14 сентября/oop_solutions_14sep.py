# Решения задач от 14 сентября
# Часть 1: магический метод __new__ (5 задач; задачи 1 и 2 решены без __new__, через метакласс)
# Часть 2: classmethod и staticmethod (6 задач)
# Каждая задача независима: копируйте нужный блок целиком.


# ===== __new__: задача 1 =====
# Без __new__: перехватываем сам вызов AbstractClass() через метакласс
class AbstractMeta(type):
    def __call__(cls, *args, **kwargs):
        return "Ошибка: нельзя создавать объекты абстрактного класса"


class AbstractClass(metaclass=AbstractMeta):
    pass


obj = AbstractClass()


# ===== __new__: задача 2 =====
# Без __new__: через метакласс считаем созданные объекты
class SingletonFiveMeta(type):
    def __call__(cls, *args, **kwargs):
        if cls._count < 5:
            cls._last = super().__call__(*args, **kwargs)
            cls._count += 1
        return cls._last


class SingletonFive(metaclass=SingletonFiveMeta):
    _count = 0
    _last = None

    def __init__(self, name):
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]


# ===== __new__: задача 3 =====
TYPE_OS = 1  # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:
    def __new__(cls, *args, **kwargs):
        # TYPE_OS читается в момент создания объекта, поэтому смена переменной учитывается
        target = DialogWindows if TYPE_OS == 1 else DialogLinux
        obj = super().__new__(target)
        # __init__ у Dialog не вызовется (объект другого класса), поэтому name задаём здесь
        obj.name = args[0]
        return obj


# ===== __new__: задача 4 =====
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):
        return Point(self.x, self.y)


pt = Point(3, 4)
pt_clone = pt.clone()


# ===== __new__: задача 5 =====
class Factory:
    def build_sequence(self):
        return []

    def build_number(self, string):
        return float(string)


# ===== classmethod/staticmethod: задача 1 =====
class Factory:
    @staticmethod
    def build_sequence():
        return []

    @staticmethod
    def build_number(string):
        return int(string)


# ===== classmethod/staticmethod: задача 2 =====
from string import ascii_lowercase, digits


class TextInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size=10):
        self.check_name(name)
        self.name = name
        self.size = size

    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"

    @classmethod
    def check_name(cls, name):
        if not (3 <= len(name) <= 50) or not all(ch in cls.CHARS_CORRECT for ch in name):
            raise ValueError("некорректное поле name")


class PasswordInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size=10):
        self.check_name(name)
        self.name = name
        self.size = size

    def get_html(self):
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"

    @classmethod
    def check_name(cls, name):
        if not (3 <= len(name) <= 50) or not all(ch in cls.CHARS_CORRECT for ch in name):
            raise ValueError("некорректное поле name")


# ===== classmethod/staticmethod: задача 3 =====
from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(number):
        if not isinstance(number, str):
            return False
        parts = number.split('-')
        return len(parts) == 4 and all(len(p) == 4 and all(ch in digits for ch in p) for p in parts)

    @classmethod
    def check_name(cls, name):
        if not isinstance(name, str):
            return False
        words = name.split(' ')
        return len(words) == 2 and all(w and all(ch in cls.CHARS_FOR_NAME for ch in w) for w in words)


# ===== classmethod/staticmethod: задача 4 =====
class Video:
    def create(self, name):
        self.name = name

    def play(self):
        print(f"воспроизведение видео {self.name}")


class YouTube:
    videos = []

    @classmethod
    def add_video(cls, video):
        cls.videos.append(video)

    @classmethod
    def play(cls, video_indx):
        cls.videos[video_indx].play()


v1 = Video()
v2 = Video()
v1.create("Python")
v2.create("Python ООП")

YouTube.add_video(v1)
YouTube.add_video(v2)
YouTube.play(0)
YouTube.play(1)


# ===== classmethod/staticmethod: задача 5 =====
class Application:
    def __init__(self, name):
        self.name = name
        self.blocked = False


class AppStore:
    def __init__(self):
        self.apps = []

    def add_application(self, app):
        self.apps.append(app)

    def remove_application(self, app):
        if app in self.apps:
            self.apps.remove(app)

    def block_application(self, app):
        app.blocked = True

    def total_apps(self):
        return len(self.apps)


# ===== classmethod/staticmethod: задача 6 =====
class Message:
    def __init__(self, text):
        self.text = text
        self.fl_like = False


class Viber:
    msgs = {}

    @classmethod
    def add_message(cls, msg):
        cls.msgs[id(msg)] = msg

    @classmethod
    def remove_message(cls, msg):
        cls.msgs.pop(id(msg), None)

    @classmethod
    def set_like(cls, msg):
        msg.fl_like = not msg.fl_like

    @classmethod
    def total_messages(cls):
        return len(cls.msgs)
