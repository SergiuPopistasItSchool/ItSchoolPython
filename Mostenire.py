class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print("Walk")

    def show(self):
        msg = f"I am {self.name} and I am {self.age} years old"
        return msg

    def speak(self):
        print("I don't know what to say")


class Dog(Pet):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        print("WOOF")

    def show(self):
        print(super().show() + f" and I am {self.breed} breed")


class Cat(Pet):
    def __init__(self, name, age, color):
        self.color = color
        super().__init__(name, age)

    def speak(self):
        print("MIAU")

    def show(self):
        print(super().show() + f" and I am {self.color} color")



#DRY Don't repreat yourself

c = Cat("Fluffy", 2,"RED")
d = Dog("Athos", 3, "Labrador")
p = Pet("Tralal", 5)
c.walk()
d.walk()

c.show()
d.show()
print(p.show())

c.speak()
d.speak()
p.speak()


"""
Tema:
Class Person de baza
O clasa angajat ce mosteste din person
O clasa Manager ce mostenste din person
Ca propietati care sunt la fel (nume, varsta, etc)
Dar au diferit nivelul de acces intr-o applicatie sau companie
"""