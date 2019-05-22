D = {'name': 'max', 'age':14, 'class':12}
d['name']
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'd' is not defined
 D
  File "<input>", line 1
    D
    ^
IndentationError: unexpected indent
D
{'name': 'max', 'age': 14, 'class': 12}
D['name']
'max'
e = {'name':'tom', 15:15, 15.1:15.1, True:True, (2,3):5}
e
{'name': 'tom', 15: 15, 15.1: 15.1, True: True, (2, 3): 5}
e = {'name':'tom', 15:15, 15.1:15.1, True:true, (2,3):5}
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'true' is not defined
e[(2,3)]
5
len(e)
5
e.get('name')
'tom'
 D = {'name':"max", 'age': 14, 'year':2004}
  File "<input>", line 1
    D = {'name':"max", 'age': 14, 'year':2004}
    ^
IndentationError: unexpected indent
D = {'name':"max", 'age': 14, 'year':2004}
d
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'd' is not defined
D
{'name': 'max', 'age': 14, 'year': 2004}
D['surname'] = 'tesaer'
D
{'name': 'max', 'age': 14, 'year': 2004, 'surname': 'tesaer'}
D.pop('surname')
'tesaer'
D
{'name': 'max', 'age': 14, 'year': 2004}
e.clear()
e
{}
del e
e
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'e' is not defined
D['name']= 'tom'
D
{'name': 'tom', 'age': 14, 'year': 2004}
D.update({'name': 'max'})
D
{'name': 'max', 'age': 14, 'year': 2004}
D.keys()
dict_keys(['name', 'age', 'year'])
D.values()
dict_values(['max', 14, 2004])
d.items()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'd' is not defined
D.items()
dict_items([('name', 'max'), ('age', 14), ('year', 2004)])
D.popitem()
('year', 2004)
D
{'name': 'max', 'age': 14}
D = {'name':"max", 'age': 14, 'year':2004,'class':12}
D.popitem()
('class', 12)
