def sum(nbr_a, nbr_b) :
    
    return nbr_a + nbr_b # Text indented for four spaces

nbr_a = 4
nbr_b = 5

result = sum(nbr_a, nbr_b)
print(result)

print('________________________')

print("Number_a")
print("Number_b")

nbr_b=-5

if nbr_b < 0 :
    print("Number_b is negative!")
    
print('----------------------')

x = [1, 2, 3, 4, 5, 6]
result = [(element * 2) for element in x]
print(result)

print('---------------------')

a = float (-10.14)
print(a)

print('-------------------------')

b = 1 + 2j

print(b)
d = complex(1,2)
print(d)

print('-------------------------')

s = 'test'
print(s)
s_one = 'te\'st'
print(s_one)
s_two = "te\"st"
print(s_two)
s_three = """te\"""st"""
print(s_three)

print('-------------------------')

lst = ['element1', 'element2', 3] # liste
lst.append('element3') # append dodava nov element na krajot od listata
lst.insert(0,'element0') # insert dodava nov element na zadadeniot indeks i taka gi pomestuva site elementi (od toj element) ze edno mesto na desno
lst.extend(['element4', 'element5'])
lst.index(3)
lst.reverse()
print(lst)
print(lst[0])
print(lst[1:])
print(lst[-1])
print(lst[3])

print('-------------------------')

new_tuple = ('element1', 'element2', 'element3') # n torka
print(new_tuple)

print('-------------------------')

my_set = {1, 2, 3} # setovi
print(my_set)

print('-------------------------')

dictionary = {"key1":'element1', "key2":'element2', "key3":3} # recnici
print(dictionary)
print(dictionary['key1'])
print(dictionary['key3'])
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
print(dictionary.pop('key1'))
print(dictionary.clear())
print(type(dictionary))

print('-------------------------')

a, b = 1, 2
print(a, b)
a, b = b, a
print(a, b)
a = 5
b = a
print(a, b)
a = 6
print(a, b)

print('-------------------------')

a = 5            # ternarni operator
print("Positive number." if a >= 0 else "Negative number.")

print('-------------------------')

nbr_1 = 1    # primeri za prioritet i asocijativnost na opretorite
nbr_2 = 2 
nbr_3 = 3 
nbr_4 = 4 

print ((nbr_1 + nbr_2) * nbr_3)
print (nbr_1 ** nbr_2 - nbr_3)
print (~nbr_1 - nbr_2)
print(nbr_1 ** nbr_2 ** nbr_3)
nbr_3 = nbr_2 = nbr_1
print(nbr_3)

print('-------------------------')

