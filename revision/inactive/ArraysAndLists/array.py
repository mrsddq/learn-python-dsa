''''
there are several classes defined in built-ins module

built-ins: int ,float, str ,lists, dict, set, range, bytes, object, exception

array is not a built in data structure and therefore need to be imported

'''

from array import *

a1=array('i',[1,2,3,4,5,6])
type(a1)
print(a1)

for x in a1:
    print(x)

for i in range(3):
    print(a1[i], end=' ')

'''
array methods
append
count
extend
fromlist
index
pop
remove
reverse
tolist

'''

a1.append(30)
print(a1, end='\n')


a1.count(30)
a1.count(10)
a1.index(1)
a1.remove(30)

print(a1, end='\n')

'''

list is a class
list is mutable
list elements are indexed
list are iterable
list can contain different type of elements
list can grow

'''

