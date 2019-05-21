x = [3,5,9,10]                #list
x
[3, 5, 9, 10]
x[0]                          #index value
3
x[4]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
IndexError: list index out of range
y = ['max', 1,15.5,[2,3]]               #any data type can be contained
y
['max', 1, 15.5, [2, 3]]
y[0]
'max'
len(x)                         #built in function to find length of string, list
4
len(y)
4
x.insert(2,'tom')               #(index,object to be inserted)
x
[3, 5, 'tom', 9, 10]
y[3][1]
3
x.remove(9)                       #(value of object to be removed)
x
[3, 5, 'tom', 10]
x.insert(1,3)
x
[3, 3, 5, 'tom', 10 }              #value from left will be removed and only one value will be removed            
x.remove(3)
x
[3, 5, 'tom', 10]
x.insert(1,10)
x
[3, 10, 5, 'tom', 10]
x.remove(10)
x
[3, 5, 'tom', 10]
x.pop()                            #pop is used to delete last element of list
10                                   #will automatically shoe the last element
x
[3, 5, 'tom']
x.pop()
'tom'
x
[3, 5]
z = [1,2,3,4,5]
del z                               # to delete the entire list, even the variable name
z
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'z' is not defined
z = [1,2,3,4,5]
z.clear()                             #to clear the element in the list
z
[]

x = [2,9,3,6,8,4,1,7]
x.sort()                                   #arrange in ascending order
x
[1, 2, 3, 4, 6, 7, 8, 9]                
x.reverse()                             #arrange in reverse order
x
[9, 8, 7, 6, 4, 3, 2, 1]
x.append(0)                               # to add an element, it will be included in last
[9, 8, 7, 6, 4, 3, 2, 1, 0]
s = x.copy()                               #to copy a list to another
s
[9, 8, 7, 6, 4, 3, 2, 1, 0]
x.append(0)
x
[9, 8, 7, 6, 4, 3, 2, 1, 0, 0]
x.count(0)                                  #to count no. of times element in bracket is present in list
2
x.count(3)
1
x.count(100)
0
x.extend(3)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: 'int' object is not iterable
x.extend([3,6])                                     #in the ()iterable(loop) chalana
x
[9, 8, 7, 6, 4, 3, 2, 1, 0, 0, 3, 6]
x.extend('bdiwx')                                   #?
x
[9, 8, 7, 6, 4, 3, 2, 1, 0, 0, 3, 6, 'b', 'd', 'i', 'w', 'x']
x.extend(15.5)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: 'float' object is not iterable
x.__add__(3)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: can only concatenate list (not "int") to list
x.__add__(y)                                                       #concatinate two list
[9, 8, 7, 6, 4, 3, 2, 1, 0, 0, 3, 6, 'b', 'd', 'i', 'w', 'x', 'max', 1, 15.5, [2, 3]]
x.__class__                   #to know thwe type
<class 'list'>
x.__contains__(6)              #to check element
True
