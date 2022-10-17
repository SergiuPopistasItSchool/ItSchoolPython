class Persons:
    numer_of_persons = 0
    def __init__(self, name):
        self.name = name
        self.addPersonNumer()
    @classmethod
    def addPersonNumer(cls):
        Persons.numer_of_persons += 1

p = Persons("Sergiu")
p1 = Persons("Stefan")
print(p.numer_of_persons)

a = [1, 2, 3, 4]
b = a[::-1]
c = b[::-2]

x = 1
for i in range(5):
    x = 0
    #x = x + 1
    x += 1
print(x)



