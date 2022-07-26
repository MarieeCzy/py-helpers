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

                

