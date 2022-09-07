# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def Shout(param):
    return  param + "!"
message = "Hello"
for caracter in message:
    if caracter == "H":
        print("STOP")
        break
    print(caracter)

print(bool(-100))
print("This is a new test")

"""
@param_in THis
is a
multi c
omment
"""

print((2**3)**2)

def update():
    table = ['a', 'd']
print("table")

my_table = ['h', 'e', 'l', 'l', 'o']
my_var = ""

for l in my_table[1:-1]:
    my_var += l

print(my_var)
print(my_table)

my_data = [0, 1, 2, 3, 4, 5, 6, 7]
my_data_var = 0
for i in my_data:
    if not i % 2:
        print(i)
        my_data_var += i

print(my_data_var)


def divideByTwo(param):
    #print(bool(bool)) #bool-uri by default sunt egale cu True
    if param == 0:
        raise ZeroDivisionError
    elif param < 0:
        raise Exception
    else:
        return param/2

data = 0

#divideByTwo(data)

def calc(x):
    if x < 0:
        raise Exception
    elif x is not type(int):
        raise TypeError

var = 'c'
try:
    calc(var)
    print("Printed")
except TypeError:
    print("Var is not a int")
except:
    print("Not calculated")

else:
    print("Was caluclated")




