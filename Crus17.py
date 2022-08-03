"""
Jefuesti o banca, dar nu iei tot. Cauti un obiect specific din cutiile cu valori.Va trebui
sa cauti in feicare pentru a gasi obiectul ce vrei sa il iei, dar cat timp iti va lua
procedura?
Task:
\Determina timpul de a gasi obiectul cautat stiind ca iti ia 5 minute sa cauti
in fiecare cutie cu valori
Input :
Un string ce reprezinta obiectele din fiecare cutie care va fi cautata(obiectele sunt separate de o virgula),iar al doilea string obiectul ce vrei sa il gasesti
Output :
Un numar ce reprezinta timpul ce iti va lua sa gasesti obiectu
ex:
Input:
aur,diamante,documente,tablou picasso,chei
tablou picasso
Output:
20
"""
inputStringCutii = "aur,diamante,documente,tablou picasso,chei"
obiectCautat = "tablou picasso"
# pasul 1: spargem string-ul intr-o lista de obiecte(cutii)
lista_obiecte = inputStringCutii.split(",")
#var1
if obiectCautat in lista_obiecte:
    index = lista_obiecte.index(obiectCautat)
    print(5 * (index + 1))
else:
    print("Obiectul nu este in lista")

#var2
# pasul 2 : iteram lista de obiecte si cautam obect cautat
contor = 0
for object in lista_obiecte:
    # pasul 2.1: contorizam cat nea luat pana la obiectul cautat
    contor = contor + 1
    if object == obiectCautat:
        break
print(contor*5)

#Continuare (pt acasa): inputul sa fie dinamic (populati lista de obiecte de la consola)



#Screti un program ce va scoate duplicatele dintr-o lista

numbers = [2, 2, 4, 6, 3, 4, 6, 1]
#var 1:
# mai creem o lista in care se facem append la ce iteram
# verificam ca numarul nu se afla in new list si facem append
new_list = []

for i in numbers:
    if i not in new_list:
        new_list.append(i)

print(new_list)

#var 2:
# tranformam lista din lista in set

new_numbers_list = set(numbers)
print(new_numbers_list)

"""
Esti pe un vas de croaziera care ancoreaza langa o plaja superba.Exita o barcuta
mica ce va duce pasageri pe plaja.Te pui la rand .
Cat timp trebuie sa astepti stiind ca pe barcuta intra 20 de oameni iar un drum dureaza 10 minute.
Task:
Determina timpul de astptare daca stii numarul de persoane in fata ta
Input :
un numar intreg ce reprezinta numarul total de perosane aflate in fata ta
Output:
un numar intreg ce reprezinta numarul de minute ce trebuie sa astepti
ex:
Input:25
Ouptut:10
"""


"""
Ai 2 prieteni ce vorbesc orca intre ei.Limba orca sunt aceleasi cuvinte 
ca in limba romana doar ca se ia prima litera a fiecarui cuvant si se pune 
la sfarsitul cuvantului in urma caruia se adauga un ay
drum = rumday
Input:
Un string ce reprezinta o propozite in limba romana
Output:
Un string ce reprezinta traducerea in limba orca
"""

"""
In jungla:
Esti cu cortul in jungla singur si auzi niste animale in intuneric prin apropiere
Bazat pe sunet determina ce animale sunt
Task:
Ti se da sunetele facute de animalele din intuneric, evalueaza fiecare sunet 
pentru a determina ce animal este:
Leii fac "Grr" , Tigri fac "Rawr", Serpii fac "Sss" iar pasarile fac "Cirip"
 
Input:
Un string ce reprezinta sunetele ce le auzi cu spatiu intre ele
Output:
Un string ce reprezinta animalele ce le auzi cu spatiu intre ele 
(nota sunetele se pot repeta)

Ex:
Rawr Cirip Sss Sss
Tigru Pasare Sarpe Sarpe

"""