# Hometask 14_5
# Создать три класса : Dog,Cat,Parrot.
# Атрибуты каждого  класса : name,age,master
# Каждый класс содержит конструктор и  методы:
# run,jump,birthday (увеличивает  age на1),sleep
# Класс Parrot имеет дополнительный метод fly, Cat-meom, Dog-bark

class Dog:
    def __init__(self,name,age,master):
        self.name = name
        self.age = age
        self.master = master

    def run(self,km):
        print(self.name, f'пробежал {km} км. ')

    def jump (self):
        print(self.name,'прыгает')

    def birthday(self):
        print(self.name,f'{self.age+1}года')

    def sleep (self):
        print(self.name,'спит')

    def bark(self):
        print(self.name,f'лает на незнакомых людей')

z = Dog('Бони',2,'Vasya')
print(z.__dict__)
z.run(2)
z.jump()
z.birthday()
z.bark()

class Cat:
    def __init__(self,name,age,master):
        self.name = name
        self.age = age
        self.master = master

    def run(self,km):
        print(self.name, f'пробежал {km} км. ')

    def jump (self):
        print(self.name,'прыгает')

    def birthday(self):
        print(self.name,f'{self.age+1}года')

    def sleep (self):
        print(self.name,'спит')

    def meom(self):
        print(self.name,f'мурчит')

с = Cat('Беня',2,'Vasya')
print(с.__dict__)
с.run(2)
с.jump()
с.birthday()
с.meom()

class Parrot:
    def __init__(self,name,age,master):
        self.name = name
        self.age = age
        self.master = master

    def run(self,km):
        print(self.name, f'пробежал {km} км. ')

    def jump (self):
        print(self.name,'прыгает')

    def birthday(self):
        print(self.name,f'{self.age+1}года')

    def sleep (self):
        print(self.name,'спит')

    def fly(self):
        print(self.name,f'летает')

k = Parrot('Веня',2,'Vasya')
print(k.__dict__)
k.run(0)
k.jump()
k.birthday()
k.fly()

# Hometask 14_6
# Создать родительский класс Pet,содержащий все общие методы классов
# Dog,Cat,Parrot. Унаследовать Dog,Cat,Parrot от Pet.
#Удалить в дочерних классах те методы,которые имеются у родительского класса.
# Создать объект каждого класса и вызвать все его методы.


class Pet:
    def __init__(self,name,age,master):
        self.name = name
        self.age = age
        self.master = master

    def run(self,km):
        print(self.name, f'пробежал {km} км. ')

    def jump (self):
        print(self.name,'прыгает')

    def birthday(self):
        print(self.name,f'{self.age+1}года')

    def sleep (self):
        print(self.name,'спит')

class Dog(Pet):
    def __init__(self,name,age,master):
        super().__init__(name,age,master)

    def bark(self):
        print(self.name,f'лает на незнакомых людей')

class Cat (Pet):
    def __init__(self,name,age,master):
        super().__init__(name,age,master)

    def meom(self):
        print(self.name, f'мурчит')


class Parrot (Pet):
    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def fly(self):
        print(self.name,f'летает')


r= Dog('Бони',5,'Шура')
r.run(2)
r.jump()
r.birthday()
r.bark()
f=Cat('Беня',2,'Шура')
f.run(1)
f.jump()
f.birthday()
f.meom()
q=Parrot('Веня',1,'Шура')
q.run(0.1)
q.jump()
q.birthday()
q.fly()
print(r.__dict__)
print(f.__dict__)
print(q.__dict__)
