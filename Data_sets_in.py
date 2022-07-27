from curses.ascii import isupper
import random
from re import X
import sys

# LISTS - MUTABLE DATA TYPES

# konstruktor listy zwraca None
list()                                                 
color_list = list()            
# zwraca pustą listę przypisaną do zmiennej                                   
print(color_list)                                      

# metoda dodaje item do listy
color_list.append('blue')                               
color_list.append('orange')                            
color_list.append('green')                              
color_list.append('pink')                               
print(color_list)

# zwraca item o indexie 1
print(color_list[1])     

#usuwa ostatni element listy
color_list.pop()
print(color_list)

#sortuje listę
color_list.sort() 
print(color_list)   

#odwraca kolejnosc w liscie
color_list.reverse() 
print(color_list)  

#dodaje item w okreslone miejsce index
color_list.insert(2, 'black')
print(color_list)

#dodaje listę do listy na koncu
numbers = [2,3,5,6,7,8,1]    
color_list.extend(numbers)
print(color_list)    

#zwraca index danego itemu
print(numbers.index(6))


#list comprehensions przykłady:
lista = [x*2 for x in (3,2,4,5,6)]
print(lista)

#(stworz liste dla wartosci randomowych z przedzialow: (0,10)...(1,10)...(4,10)...(9,10))
scores = [random.randint(i,10) for i in range(10)]
print(scores)

#(przyklad nested conditional:)
caps = []

for letter in 'Henry Honey':
    if letter.isupper():
        caps.append(letter)
print(caps)

caps = [letter for letter in 'Henry Honey' if letter.isupper()]
print(caps)

#flat list:
list_of_lists = [['a','b','c'],['d','e','f']]
flat = []

for sub_list in list_of_lists:
    for item in sub_list:
        flat.append(item)
        
print(flat)

flat = [item for sub_list in list_of_lists for item in sub_list]
print(flat)
# sprawdzanie rozmiaru zmiennej (bajty) 
print(sys.getsizeof(flat))

#GENERATOR EXPRESSIONS ()

flat = (item for sub_list in list_of_lists for item in sub_list)
print(sys.getsizeof(flat))

#get size of:
print(sys.getsizeof([score+1 for score in range(10)]))
print(sys.getsizeof((score+1 for score in range(10))))
print(flat)

#GENERATOR FUNCTIONS

def counter(x):
    while x<50:
        yield x
        x+=1
        
get_number = counter(12)

cycle = [count for count in get_number]
print(cycle)

#
def foo_moo(i):
    while True:
        if i%5 ==0:
            yield 'foo'
            print(i)
            i += 1
      
        else:
            yield 'moo'
            print(i)
            i += 1
            
fm = foo_moo(5)

for _ in range(11):
    print(next(fm))
