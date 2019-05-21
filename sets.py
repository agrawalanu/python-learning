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
