# Решения заданий по ООП (классы, атрибуты, методы, __init__)
# Каждое задание независимо: копируйте нужный блок целиком.


# ===== Задание 1 =====
class DataBase:
    pk = 1
    title = "Классы и объекты"
    author = "Сергей Балакирев"
    views = 14356
    comments = 12


# ===== Задание 2 =====
class Goods:
    title = "Мороженое"
    weight = 154
    tp = "Еда"
    price = 1024


Goods.price = 2048
Goods.inflation = 100


# ===== Задание 3 =====
class Car:
    pass


setattr(Car, 'model', "Тойота")
setattr(Car, 'color', "Розовый")
setattr(Car, 'number', "П111УУ77")

print(Car.__dict__['color'])


# ===== Задание 4 =====
class Notes:
    uid = 1005435
    title = "Шутка"
    author = "И.С. Бах"
    pages = 2


print(getattr(Notes, 'author'))


# ===== Задание 5 =====
class Dictionary:
    rus = "Питон"
    eng = "Python"


print(getattr(Dictionary, 'rus_word', False))


# ===== Задание 6 =====
class TravelBlog:
    total_blogs = 0


tb1 = TravelBlog()
tb1.name = 'Франция'
tb1.days = 6
TravelBlog.total_blogs += 1

tb2 = TravelBlog()
tb2.name = 'Италия'
tb2.days = 5
TravelBlog.total_blogs += 1


# ===== Задание 7 =====
class Figure:
    type_fig = 'ellipse'
    color = 'red'


fig1 = Figure()
fig1.start_pt = (10, 5)
fig1.end_pt = (100, 20)
fig1.color = 'blue'

del fig1.color
print(*fig1.__dict__)


# ===== Задание 8 =====
class Person:
    name = 'Сергей Балакирев'
    job = 'Программист'
    city = 'Москва'


p1 = Person()
print('job' in p1.__dict__)


# ===== Задание 9 =====
class MediaPlayer:
    def open(self, file):
        self.filename = file

    def play(self):
        print(f"Воспроизведение {self.filename}")


media1 = MediaPlayer()
media2 = MediaPlayer()
media1.open("filemedia1")
media2.open("filemedia2")
media1.play()
media2.play()


# ===== Задание 10 =====
class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data):
        self.data = data

    def draw(self):
        print(*[x for x in self.data
                if self.LIMIT_Y[0] <= x <= self.LIMIT_Y[1]])


graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()


# ===== Задание 11 =====
import sys


class StreamData:
    def create(self, fields, lst_values):
        if len(fields) != len(lst_values):
            return False
        for name, value in zip(fields, lst_values):
            setattr(self, name, value)
        return True


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()


# ===== Задание 12 =====
class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        for line in data:
            self.lst_data.append(dict(zip(self.FIELDS, line.split())))

    def select(self, a, b):
        return self.lst_data[a:b + 1]


# ===== Задание 13 =====
class Translator:
    def add(self, eng, rus):
        if 'tr' not in self.__dict__:
            self.tr = {}

        self.tr.setdefault(eng, [])
        if rus not in self.tr[eng]:
            self.tr[eng].append(rus)

    def remove(self, eng):
        if eng in self.tr:
            del self.tr[eng]

    def translate(self, eng):
        return self.tr.get(eng, False)


tr = Translator()
tr.add('tree', 'дерево')
tr.add('car', 'машина')
tr.add('car', 'автомобиль')
tr.add('leaf', 'лист')
tr.add('river', 'река')
tr.add('go', 'идти')
tr.add('go', 'ехать')
tr.add('go', 'ходить')
tr.add('milk', 'молоко')

tr.remove('car')
print(*tr.translate('go'))


# ===== Задание 14 =====
class Money:
    def __init__(self, money):
        self.money = money


my_money = Money(100)
your_money = Money(1000)


# ===== Задание 15 =====
class Point:
    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color


points = [Point(i, i) for i in range(1, 2000, 2)]  # 1, 3, 5, ... (1000 точек)
points[1].color = 'yellow'


# ===== Задание 16 =====
import random


class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


elements = [random.choice((Line, Rect, Ellipse))(*[random.randint(-100, 100) for _ in range(4)])
            for _ in range(217)]

for obj in elements:
    if isinstance(obj, Line):
        obj.sp = (0, 0)
        obj.ep = (0, 0)


# ===== Задание 17 =====
class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        sides = (self.a, self.b, self.c)
        if not all(isinstance(s, (int, float)) for s in sides) or any(s <= 0 for s in sides):
            return 1
        a, b, c = sides
        if a >= b + c or b >= a + c or c >= a + b:
            return 2
        return 3


a, b, c = map(int, input().split())
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())


# ===== Задание 18 =====
class Graph:
    def __init__(self, data):
        self.data = data[:]
        self.is_show = True

    def set_data(self, data):
        self.data = data[:]

    def show_table(self):
        if self.is_show:
            print(*self.data)
        else:
            print("Отображение данных закрыто")

    def show_graph(self):
        if self.is_show:
            print("Графическое отображение данных:", *self.data)
        else:
            print("Отображение данных закрыто")

    def show_bar(self):
        if self.is_show:
            print("Столбчатая диаграмма:", *self.data)
        else:
            print("Отображение данных закрыто")

    def set_show(self, fl_show):
        self.is_show = fl_show


# считывание списка из входного потока (эту строку не менять)
data_graph = list(map(int, input().split()))

gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()


# ===== Задание 19 =====
class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    total_mem_slots = 4

    def __init__(self, name, cpu, *mem_slots):
        self.name = name
        self.cpu = cpu
        self.mem_slots = list(mem_slots)[:self.total_mem_slots]

    def get_config(self):
        mem = '; '.join(f"{m.name} - {m.volume}" for m in self.mem_slots)
        return [f"Материнская плата: {self.name}",
                f"Центральный процессор: {self.cpu.name}, {self.cpu.fr}",
                f"Слотов памяти: {self.total_mem_slots}",
                f"Память: {mem}"]


mb = MotherBoard("Gigabyte B550", CPU("Ryzen 5 5600", 3500),
                 Memory("Kingston", 8192), Memory("Corsair", 16384))
print(*mb.get_config(), sep='\n')


# ===== Задание 20 =====
class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return [f"{g.name}: {g.price}" for g in self.goods]


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()
cart.add(TV("Samsung", 45000))
cart.add(TV("LG", 38000))
cart.add(Table("IKEA Lack", 3500))
cart.add(Notebook("Lenovo IdeaPad", 55000))
cart.add(Notebook("ASUS VivoBook", 62000))
cart.add(Cup("Кружка белая", 300))
print(*cart.get_list(), sep='\n')
