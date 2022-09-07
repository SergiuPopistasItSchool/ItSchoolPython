class Animal:
    def __init__(self, name, age):
        #protected data members
        self._name = name
        #private attribute
        self.__age = age
    #protected method
    def _displayAge(self):
        #accesing private age attribute
        print("Age: ", self.__age)

    def ChangeAge(self, age):
        self.__age = age


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    #pulic method
    def printDetails(self):
        #accesing protected attribute from super class
        print("Dog Name: ", self._name)
        super()._displayAge()
    def ChangeDogName(self,name):
        #OK -> we can change protected attrib from chiled class
        self._name = name
    def ChangeDogAge(self, newAge):
        self.__age = newAge


obj = Dog("Ghita", 5)

obj.printDetails()
obj.ChangeDogName("Ion")
#obj._name = "Ion" #NOT RECOMENDED IF WE SEE _ATRIBUTE/METHOD, DEV SHOULD NOT CHANGE
obj.printDetails()
obj.ChangeAge(10)
obj.printDetails()
