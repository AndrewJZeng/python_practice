class Animal(object):
    def __init__(self, age):
        self.age = age

    def speak(self):
        print('not defined')

    def __str__(self):
        return f'Animal: age ({self.age})'

obj_animal = Animal(1)
print(obj_animal)
obj_animal.speak()

class Cat(Animal):
    def __init__(self, age, color='BW'):
        super().__init__(age)
        self.color = color

    def speak(self):
        print('Meow')

    def __str__(self):
        return f'Cat: age ({self.age}), color ({self.color})'

obj_cat = Cat(2, 'Brown')
print(obj_cat)
obj_cat.speak()

class Rabbit(Animal):
    def __init__(self, age, weight):
        super().__init__(age)
        self.weight = weight

    def speak(self):
        print('Squeak')

    def __str__(self):
        return f'Rabbit: age ({self.age}), weight ({self.weight})'

obj_rabbit = Rabbit(1, '2LB')
print(obj_rabbit)
obj_rabbit.speak()

class Num(object):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f'Num: {self.data}'

    def __add__(self, other):
        sum = self.data + other.data
        return Num(sum)
    

x = Num(3)
print(x)
y = Num(5)
print(y)
sum = x + y
print(sum)
print(type(sum))

            		
                        




