a = [0,1,2,3,4,5,6,]
b= (0,1,2,3,4,5)
c = '0123456789'
x = slice(0,5)
a[x]
[0, 1, 2, 3, 4]
b[x]
(0, 1, 2, 3, 4)
c(x)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: 'str' object is not callable
c[x]
'01234'
a[0,5]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: list indices must be integers or slices, not tuple
a[0:5]
[0, 1, 2, 3, 4]
b[4:]
(4, 5)
c[:]
'0123456789'
a
[0, 1, 2, 3, 4, 5, 6]
a{0:7:2}
  File "<input>", line 1
    a{0:7:2}
     ^
SyntaxError: invalid syntax
a[0:7:2]
[0, 2, 4, 6]
 a[::4]
  File "<input>", line 1
    a[::4]
    ^
IndentationError: unexpected indent
a[::4]
[0, 4]
c[-1]
'9'
c[-2]
'8'
c[::-1]
'9876543210'
c[::-2]
'97531'
a[1::-1]
[1, 0]
a[:-3:-1]
[6, 5]
a[-3::-1]
[4, 3, 2, 1, 0]
