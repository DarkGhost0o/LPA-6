class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def make_sound(self):
        return f"{self.name} издает звук."
    
    def move(self):
        return f"{self.name} движется."
    
    def get_info(self):
        return f"{self.name}, возраст: {self.age} лет"


class Mammal(Animal):
    def __init__(self, name, age, hair_color):
        super().__init__(name, age)
        self.hair_color = hair_color
    
    def feed_milk(self):
        return f"{self.name} кормит детенышей молоком."

    def make_sound(self):
        return f"{self.name} рычит/мяукает/лает."
    
    def move(self):
        return f"{self.name} бегает на четырех лапах."
    
    def get_info(self):
        parent_info = super().get_info()
        return f"{parent_info}, цвет шерсти: {self.hair_color}"


class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span
    
    def fly(self):
        return f"{self.name} летит. Размах крыльев: {self.wing_span} м."

    def make_sound(self):
        return f"{self.name} чирикает/щебечет."

    def move(self):
        return f"{self.name} летает по воздуху."
    
    def get_info(self):
        parent_info = super().get_info()
        return f"{parent_info}, размах крыльев: {self.wing_span} м"


class Fish(Animal):
    def __init__(self, name, age, water_type):
        super().__init__(name, age)
        self.water_type = water_type
    
    def swim(self):
        return f"{self.name} плавает в {self.water_type} воде."

    def make_sound(self):
        return f"{self.name} издает булькающие звуки."

    def move(self):
        return f"{self.name} плавает, извиваясь."
    
    def get_info(self):
        parent_info = super().get_info()
        return f"{parent_info}, тип воды: {self.water_type}"


animals = [
    Mammal("Лев", 5, "золотистый"),
    Mammal("Кот", 3, "серый"),
    Bird("Орел", 4, 2.3),
    Bird("Воробей", 1, 0.2),
    Fish("Лосось", 2, "пресная"),
    Fish("Акула", 7, "соленая"),
    Mammal("Собака", 4, "коричневый"),
    Bird("Пингвин", 6, 0.8),
    Fish("Золотая рыбка", 1, "пресная")
]

print("=" * 70)
print("ИНФОРМАЦИЯ О ЖИВОТНЫХ")
print("=" * 70)

for animal in animals:
    print(animal.get_info())
    print("-" * 50)

print("\n" + "=" * 70)
print("ПОЛИМОРФИЗМ: каждый животный издает свой звук и движется по-своему")
print("=" * 70)

for animal in animals:
    print(f"\n{animal.name} (тип: {type(animal).__name__}):")
    print(f"  Звук: {animal.make_sound()}")
    print(f"  Движение: {animal.move()}")

print("\n" + "=" * 70)
print("УНИКАЛЬНЫЕ МЕТОДЫ КАЖДОГО КЛАССА")
print("=" * 70)

for animal in animals:
    if isinstance(animal, Mammal):
        print(f"{animal.name}: {animal.feed_milk()}")
    elif isinstance(animal, Bird):
        print(f"{animal.name}: {animal.fly()}")
    elif isinstance(animal, Fish):
        print(f"{animal.name}: {animal.swim()}")