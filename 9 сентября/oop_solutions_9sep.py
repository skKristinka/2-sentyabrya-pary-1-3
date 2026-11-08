# Решения задач от 9 сентября (пара 11:50-13:20, группы 1, 2, 3)
# Каждая задача независима: копируйте нужный блок целиком.


# ===== Задача 1 =====
class Goods:
    title = "Мороженое"
    weight = 150
    tp = "Еда"
    price = 100


Goods.price = 2048
setattr(Goods, 'inflation', 100)


# ===== Задача 2 =====
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

print(TravelBlog.total_blogs)


# ===== Задача 3 =====
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


# ===== Задача 4 =====
class Money:
    def __init__(self, money):
        self.money = money


my_money = Money(100)


# ===== Задача 5 =====
class Point:
    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color


p1 = Point(10, 20)
p2 = Point(12, 5, 'red')
p3 = Point(7, 3, 'green')
points = [p1, p2, p3]


# ===== Задача 6 =====
class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        for line in data:
            self.lst_data.append(dict(zip(self.FIELDS, line.split())))

    def select(self, a, b):
        return self.lst_data[a:b + 1]


# ===== Задача 7 =====
class Graph:
    def __init__(self, data):
        self.data = data[:]
        self.is_show = True

    def show_table(self):
        if self.is_show:
            print(*self.data)
        else:
            print("Отображение данных закрыто")

    def set_show(self, fl_show):
        self.is_show = fl_show


# ===== Задача 8 =====
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


# ===== Задача 9 =====
class Figure:
    def __init__(self, coords, width, color):
        self.coords = coords
        self.width = width
        self.color = color

    def draw(self):
        print("Рисуется фигура")


class Line(Figure):
    def draw(self):
        print("Рисуется линия")


class Rect(Figure):
    def draw(self):
        print("Рисуется прямоугольник")


class Ellipse(Figure):
    def draw(self):
        print("Рисуется эллипс")


figures = [Line((0, 0, 10, 10), 2, 'red'),
           Rect((5, 5, 20, 15), 1, 'blue'),
           Ellipse((0, 0, 30, 20), 3, 'green')]

for fig in figures:
    fig.draw()


# Новый класс: цикл выше менять не нужно, полиморфизм всё сделает сам
class Triangle(Figure):
    def draw(self):
        print("Рисуется треугольник")


figures.append(Triangle(((0, 0), (10, 0), (5, 8)), 2, 'black'))

for fig in figures:
    fig.draw()
