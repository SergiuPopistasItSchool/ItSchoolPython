def foo():
    print("foo")
print(type(foo))

x = 1
y = "hello"
#x + y erroare deoarece avem un obiect de tip int si un obiect de tip string

y.upper() #chemam metoda upper a obiectului y de tip string

#x.upper# error deoarece nu avem metoda upper la obiectul x de tip int

class Dog:
    #self = o referitna catre obiectul Dog
    def __init__(self, dogName): #init + metode cu care instantiem obiectul
        self.nume = dogName
        self.varsta = 0
    def setVarsta(self, varsta):
        if(varsta < 0):
            print("Varsta nu poate fi negativa")
        else:
            self.varsta = varsta

    def add_one(self, x):
        return x+1
    def bark(self):
        print("HAM")

d = Dog("Athos") #am creat un obiect d de tip Dog si am setat atributul nume = Athos
print(type(d))
d.bark()
print(d.add_one(2))
print(d.nume)
print(d.varsta)
d.varsta = 2
print(d.varsta)

class PensiuneCaini:
    def __init__(self):
        self.caini = []

    def add_Caine(self, caine):
        self.caini.append(caine)

pensiune = PensiuneCaini()
pensiune.add_Caine(d)
print(len(pensiune.caini))
#Teme:
#modelam o clasa ce reprezinta un student, dupa care
#o grupa ce reprezita mai multi studenti , iar aceste grupe apartin unui curs

# un mic ex: Modelam o clasa ce reprezinta un angajat,
	#ce are un nume, varsta, salariu
	#un departament ce contiune mai multi angjati
	#pentru departament sa avem optiunea sa adaugam sau
#sa scoatem angajati
#sa vedem cat cheltuie departemantul pe salarii


