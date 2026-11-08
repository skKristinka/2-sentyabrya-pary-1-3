class Cat:
    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age

    def draw(self):
        print(f"На экране рисуется кот {self.name}, порода {self.breed}")


cat1 = Cat("Британская", "Барсик", 3)
cat2 = Cat("Сиамская", "Мурка", 2)
cat3 = Cat("Мейн-кун", "Рыжик", 5)

for cat in (cat1, cat2, cat3):
    cat.draw()
