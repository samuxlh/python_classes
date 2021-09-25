"""
Python lists are other compilers arrays

C example:
If you declare an integer array sized 8 bytes they are all 
integers, that is not a problem in python since you can declare
just the list and input literally any data into it

FACTS
- It is dynamic-sized: You can create a list and simply 
keep adding elements to it.

PYTHON LISTS ARE ALWAYS REPRESENTED WITH []

"""

#Declaring lists

lista1 = [64, 234, 623, 75, 53, 643, 25, 74, 84, 26]
lista2 = ['S', 'a', 'm', 'u', 'e', 'l', ' ', 'C', 'e', 'z', 'a', 'r']
lista3 = []
lista4 = list(range(10))
lista5 = list('Samuel Cezar')

"""
lista5 == lista2 !!
"""

#Searching something in the list

if 1 in lista1:
    print('achei 1 na lista\n')
else:
    print('não achei 1 na lista\n')

#Sorting a list

lista1.sort() #will sort the list, dont know what else to say

#Counting occurrence

#printing amount of integer 1 ocurrences in list named lista1
print('Amount of 1 on lista1')
print(lista1.count(1))

#printing amount of string a in list name lista5
print('Amount of a on lista5')
print(lista5.count('a'))

#Adding an element to the list
lista1.append(5)
#appending can only add single variables

lista1.append([5, 6, 7, 8])
#appending a list will create a sublist within the original one
#after creating a sublist a list cannot be sorted

lista1.extend([64, 128, 256])
#will add 3 elements to lista1 (cannot add single value)

lista1.insert(2, 69) 
#inserts number 69 on the third position of lista1
#It does not substitute the original value only adds it to the 
#list and moves everything else one position to the left

lista6 = lista1 + lista2
#you can also do this as lista1.extend(lista2)
#you can operate with lists

lista1.reverse()
#will reverse the string
lista1.reverse()
#just reversing it back

lista6 = lista2.copy()
#lista6 will receive lista2
print('Tamanho da lista1')
print(len(lista1))

lista1.append(69)
#appending element 69

lista1.pop()
#removing element 69
#pop function removes last element and returns it
#you can remove at any index with lista1.pop(index)

lista6.clear()
#removes all the elements

"""
nova = [1, 2, 3]
nova = nova * 3 = [1, 2, 3, 1, 2, 3, 1, 2, 3]
"""

nome = 'Samuel Cezar dos Santos'
nome = nome.split()
#nome is now equal to this list >> [Samuel, Cezar, dos, Santos]
#split parenthesis should have your separator.
#default is list.split(pretent this is a space between quotes)

nome = ' '.join(nome)
#this means nome is now every element on list nome separated by spacebar

"""
for elemento in lista1:
    print(elemento)
#printing entire lista1
"""
print('\n\n\n\n\n\n')

carrinho = []
produto = ''
while produto != 'quit':
    print('Add product or type quit to exit.')
    produto = input()
    if produto != 'quit':
        carrinho.append(produto)

print('\n')
for produto in carrinho:
    print(produto)
