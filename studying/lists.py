"""
Python lists are other compilers arrays

C example:
If you declare an integer array sized 8 bytes they are all 
integers, that is not a problem in python since you can declare
just the list and input literally any data into it

- It is dynamic-sized: You can create a list and simply 
keep adding elements to it.

PYTHON LISTS ARE ALWAYS REPRESENTED WITH []

"""

#Declaring lists

list1 = [64, 234, 623, 75, 53, 643, 25, 74, 84, 26]
list2 = ['S', 'a', 'm', 'u', 'e', 'l', ' ', 'C', 'e', 'z', 'a', 'r']
list3 = []
list4 = list(range(10))
list5 = list('Samuel Cezar') # list5 = ['S', 'a', 'm', 'u', 'e', 'l', ' ', 'C', 'e', 'z', 'a', 'r']

#Searching something in the list

if 1 in list1:
    print('found 1.\n')
else:
    print('did not found 1.\n')

#Sorting a list

list1.sort() #will sort the list, dont know what else to say

#Counting occurrence

print('how many times int 1 appears on list1:', list1.count(1))

print("how many times char 'a' appears on list5:", list5.count('a'))

list1.append(5)
#appending can only add single variables

list1.append([5, 6, 7, 8])
#appending a list will create a sublist within the original one
#after creating a sublist a list cannot be sorted

list1.extend([64, 128, 256])
#will add 3 elements to list1 (cannot add single value)

list1.insert(2, 42) 
#inserts number 42 on the third position of list1
#It does not substitute the original value only adds it to the 
#list moving everything else next position

list6 = list1 + list2
#you can also do this as list1.extend(list2)
#you can operate with lists

list1.reverse()
#will reverse the string
list1.reverse()
#just reversing it back

list6 = list2.copy()
#list6 will receive list2

print('len(list1):', len(list1))

list1.append(42)
#appending element 42

list1.pop()
#removing element 42
#pop function removes last element and returns it
#you can remove at any index with list1.pop(index)

list6.clear()
#removes all the elements

"""
newList = [1, 2, 3]
newList = newList * 3 = [1, 2, 3, 1, 2, 3, 1, 2, 3]
"""

name = 'Samuel Cezar dos Santos'
name = name.split()
#name = [Samuel, Cezar, dos, Santos]
#split parenthesis should have your separator.
#default is list.split(pretent this is a space between quotes)

name = ' '.join(name)
#this means name is now every element on list name separated by spacebar

anotherList = ['A', 'B', 'C', 'D', 'E', 'C']
print('anotherList[-1] =',anotherList[-1]) # will print last character 'E'

print('Generating an index for a list:')
for index, letter in enumerate(anotherList):
    print(index, letter)

#search variable index using it's content
print("anotherList.index('C') =", anotherList.index('C'))
#if it has more than one 'C' it will return the first one it finds

#search setting an range
print("anotherList.index('C', 3)", anotherList.index('C', 3))