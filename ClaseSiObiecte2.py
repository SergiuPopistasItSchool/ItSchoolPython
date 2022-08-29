class MyClass:
    x = 5
    def foo(self):
        print("Foo")

p1 = MyClass()
print(p1.x)

#putem creea si clase ce sa aibe meteode in ele

class Point:
    def __init__(self):
        pass

    def move(self):
        self.x = 5
        print("move")

    def draw(self):
        print("draw")

point1 = Point()
point1.draw()
point1.move()
point1.x = 10
point1.y = 20
print(point1.x)

point2 = Point()
print(point1)
print(point2)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.weight = 0
    def setWeight(self,weight):
        self.weight = weight

    def printWeight(self):
        print(self.weight)

    def getWeight(self):
        return self.weight

    def Hello(self):
        print(f"My name is {self.name}, and I have {self.age} years")


#o metoda Hello(): Ce sa printeze numele si varsta Persoanei

p1 = Person("Sergiu", 31)
p1.Hello()
p2 = Person("Stefan", 20)
p2.Hello()
p1.height = 10
print(p1.getWeight())
p1.setWeight(85)
p1.printWeight()
print(p1.getWeight())

class Engine:
    def __init__(self, type, cilinders):
        self.tpe = type
        self.cilinders = cilinders

    def turnOn(self):
        print("Engine is On")

class Car:
    def __init__(self, color):
        self.color = color
        self.engine = Engine("Unkown", 0)

    def setEngine(self,type, ciliders):
        self.engine = Engine(type, ciliders)

    def drive(self):
        self.engine.turnOn()
        print("You are driving awaay")

myCar = Car("Red")
myCar.setEngine("Petrol", 16)
myCar.drive()

# modelam o clasa ce reprezinta un student, dupa care
#o grupa ce reprezita mai multi studenti , iar aceste grupe apartin unui curs

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class Group:
    def __init__(self, name, max_number_of_students):
        self.name = name
        self.maxStudents = max_number_of_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.maxStudents:
            self.students.append(student)
            return True
        else:
            return False

    def printStudents(self):
         for studen in self.students:
             print(f"Student name:{studen.name}")


s1 = Student("Sergiu", 31, 5)
s2 = Student("Stefan", 20, 9)
s3 = Student("Alex", 25, 10)

g1 = Group("Grupa1",2)
g1.add_student(s1)
g1.add_student(s2)
g1.add_student(s3)
g1.printStudents()

"""Tema2:

un mic ex: Modelam o clasa ce reprezinta un angajat,
	ce are un nume, varsta, salariu
	un departament ce contiune mai multi angjati
	pentru departament sa avem optiunea sa adaugam sau
sa scoatem angajati
sa vedem cat cheltuie departemantul pe salarii

"""