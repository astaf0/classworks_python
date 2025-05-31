class Animal():
    def __init__(self, age, name):
        self.age = age
        self.name = name
        self.health = 100

    def walk(self):
        self.health += 10
        return f'{self.name} гуляет, здоровье - {self.health}'

class Dog(Animal):

    def speak(self):
        return 'гав'

    def eat(self, food):
        allowed_food = ['корм', 'мясо', 'кость']
        if food in allowed_food:
            self.health += 10
        return f'{self.name} поел, здоровье - {self.health}'


class Cat(Animal):
    def speak(self):
        return 'мяу, мрр'

    def eat(self, food):
        allowed_food = ['корм', 'мясо', 'молоко']
        if food in allowed_food:
            self.health += 10
        return f'{self.name} поел, здоровье - {self.health}'


dog1 = Dog(2, 'Рекс')
print(dog1.walk())
print(dog1.speak())
print(dog1.eat('трава'))
print(dog1.eat('корм'))