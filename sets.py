A = {1,2,6,3,9,5}
a
('hi', 'hi', 'hi', 'hi', 'hi')
A
{1, 2, 3, 5, 6, 9}
len(A)
6
x ={2,3,6,8,1}
x
{1, 2, 3, 6, 8}
x.add(10)
x
{1, 2, 3, 6, 8, 10}
x.append(0)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: 'set' object has no attribute 'append'
x.add(10)
x
{1, 2, 3, 6, 8, 10}
x.update([15,18,17,14])
x
{1, 2, 3, 6, 8, 10, 14, 15, 17, 18}
x.remove(18)
x
{1, 2, 3, 6, 8, 10, 14, 15, 17}
x.discard(17)
x
{1, 2, 3, 6, 8, 10, 14, 15}
a = {2,3,6,5,4,9}
a
{2, 3, 4, 5, 6, 9}
a.len()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: 'set' object has no attribute 'len'
len(a)
6
a.add(3)
a
{2, 3, 4, 5, 6, 9}
a.add(7)
a
{2, 3, 4, 5, 6, 7, 9}
a.update({15,18,26,2})
a
{2, 3, 4, 5, 6, 7, 9, 15, 18, 26}
a.remove(15)
a
{2, 3, 4, 5, 6, 7, 9, 18, 26}
a.discard(6)
a
{2, 3, 4, 5, 7, 9, 18, 26}
a.remove(100)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
KeyError: 100
a.discard(100)
a
{2, 3, 4, 5, 7, 9, 18, 26}
a.pop()
2
a
{3, 4, 5, 7, 9, 18, 26}
a.pop()
3
a
{4, 5, 7, 9, 18, 26}
a.pop()
4
a
{5, 7, 9, 18, 26}
a.pop()
5
a
{7, 9, 18, 26}
name = ('max','tom','den')
name.clear()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'clear'
name = {'max','tom','den'}
name.clear()
name
set()
name = set(('max', 'tom', 'den'))
name
{'max', 'den', 'tom'}
z = set(['max', 'tom','den'])
z
{'max', 'den', 'tom'}
a = {2,5,6,9,7}
b= {1,6,3,4,}
a|b
{1, 2, 3, 4, 5, 6, 7, 9}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 9}
a &b
{6}
a.intersection(b)
{6}
a-b
{9, 2, 5, 7}
 b-a
  File "<input>", line 1
    b-a
    ^
IndentationError: unexpected indent
b-a
{1, 3, 4}
a.difference(b)
{9, 2, 5, 7}
  x = [2,3,6,9]
  File "<input>", line 1
    x = [2,3,6,9]
    ^
IndentationError: unexpected indent
x=[2,3,6,9]
x.append('anjhie')
x
[2, 3, 6, 9, 'anjhie']
x.extend('guh')
x
[2, 3, 6, 9, 'anjhie', 'g', 'u', 'h']
a^b
{1, 2, 3, 4, 5, 7, 9}
a = {2,3,5,6}
b={2,3,5,6}
a^b
set()
