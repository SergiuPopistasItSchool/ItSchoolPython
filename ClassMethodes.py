class Person:
    #class attriubte - > un atribut shareuit de toate obiectele acestei clase
    number_of_persons = 0
    def __init__(self,name):
        self.name = name
        Person.add_number_of_persons()
    @classmethod #decorator
    def get_number_of_persons(cls):
        return cls.number_of_persons

    @classmethod
    def add_number_of_persons(cls):
        cls.number_of_persons += 1


p1 = Person("Sergiu")
print(p1.number_of_persons)
p2 = Person("Andrei")
#Person.number_of_persons = 8
print(Person.add_number_of_persons())
#Person.number_of_persons = 2
print(p2.get_number_of_persons())


class Math:

    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10

    @staticmethod
    def pr(x):
        print(x)

Math.pr("Test")
z = Math.add5(5)

print(z)

"""
tema: creati un static class cu static methods in care sa aveti o metoda (statica) care sa gaseasca cel mai mic elementr dintr-o lista
si o metoda(statica) care sa gasesca cel mai mare dintr-o lista
"""