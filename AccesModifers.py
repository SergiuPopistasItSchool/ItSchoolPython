class Animal:
    def __init__(self, name, age):
        #public data members
        self.name = name
        self.age = age
    #public method
    def displayAge(self):
        #accesing public age attribute
        print("Age: ", self.age)

obj = Animal("Ghita", 5)
#accesing display age public method
obj.displayAge()
#modivy age public attribute
obj.age = 10
obj.displayAge()