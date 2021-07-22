"""

Lists behave as other languages ARRAYS, but they're DYNAMIC,
and also it can contain ANY variable type.

"""

myList = [2, 4, 6, 8, 0];
myList2 = [1, 3, 5, 7, 9];
myListStr = ['A', 'B', 'C', 'D'];
myListStr2 = ['E', 'F', 'G', 'H'];
type(myList);

""" Self-generated Lists """

myList3 = list(range(10))
myListStr3 = list('This will be transformed into a list');

""" What can I do with lists anyways? """

if 8 in myList:
    print('myList contains 8');

if 'A' in myListStr:
    print('myListStr contains "A"');
