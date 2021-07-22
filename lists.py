"""

Lists behave as other languages ARRAYS, but they're DYNAMIC,
and also it can contain ANY variable type.

"""

myList = [2, 2, 4, 6, 8, 0];
myList2 = [1, 3, 5, 7, 9];
myListStr = ['A', 'E', 'H', 'D'];
myListStr2 = ['B', 'F', 'G', 'C'];
type(myList);

""" Self-generated Lists """

myList3 = list(range(10))
myListStr3 = list('This will be transformed into a list');

""" What can I do with lists anyways? """

# here i'll be checking lists content

if 8 in myList:
    print('myList contains 8');

if 'A' in myListStr:
    print('myListStr contains "A"');

#  a dir(myList) will show you EVERY method available for this 

myList += myList2;

print('\nmyList before sorting:');
print(myList);

myList.sort(); #  easy af omg

print('\nmyList after sorting:');
print(myList);

myListStr += myListStr2;

print('\nmyListStr before sorting:');
print(myListStr);

myListStr.sort(); #  it also works with strings!!

print('\nmyListStr after sorting:');
print(myListStr);

# you can count how many times the item appears in a list

print(myList.count(0)) # will print 1
print(myList.count(2)) # will print 2 (bc it appears twice ofc)