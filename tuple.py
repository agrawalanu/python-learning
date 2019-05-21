x = (1,5,3,4,8)
x
(1, 5, 3, 4, 8)
x[0]
1
x[3]
4
x[0]=2
Traceback (most recent call last):                           #no change in value can be done in tuple
  File "<input>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
x.count(8)
1
len(x)
5
y = (1,'max',1.6)
z = x+y                                     #concatination can be done to form a new tuple
z
(1, 5, 3, 4, 8, 1, 'max', 1.6)
a = ('hi',)*5
a
('hi', 'hi', 'hi', 'hi', 'hi')
max(x)
8
min(x)
1
del z
z
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'z' is not defined
x.clear()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'clear'
