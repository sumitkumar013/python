Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l=[8,"f",8.8]
type(l)
<class 'list'>
l[0]=1
l
[1, 'f', 8.8]
l.append
<built-in method append of list object at 0x00000233626A0D00>
l.append(7)
l
[1, 'f', 8.8, 7]
l.insert(5,3)
l
[1, 'f', 8.8, 7, 3]
l.insert(3,5)
l
[1, 'f', 8.8, 5, 7, 3]
l.insert(4,87)
l
[1, 'f', 8.8, 5, 87, 7, 3]
l.pop()
3
l.remove(3)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    l.remove(3)
ValueError: list.remove(x): x not in list
l.remove(8.8)
l
[1, 'f', 5, 87, 7]
l[1:3]
['f', 5]
l*2
[1, 'f', 5, 87, 7, 1, 'f', 5, 87, 7]
len(l)
5
max(l)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    max(l)
TypeError: '>' not supported between instances of 'str' and 'int'
l=[6,7,8]
max(l)
8
min(l)
6
l
[6, 7, 8]
mid(l)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    mid(l)
NameError: name 'mid' is not defined. Did you mean: 'id'?
t=
SyntaxError: invalid syntax
t=(6,"f",7.7)
type(t)
<class 'tuple'>
t[0]=5
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    t[0]=5
TypeError: 'tuple' object does not support item assignment
t[2]
7.7
t[3]
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    t[3]
IndexError: tuple index out of range
t=5.6,"y",0
type(t)
<class 'tuple'>

t.count(0)
1
day=
SyntaxError: invalid syntax
[day

 flja
 
SyntaxError: '[' was never closed
d={1,2,3,6,7}
 
type
 
<class 'type'>




... 
>>> 

>>> 

>>> 

... 
>>> 

>>> 

... 
>>> 
>>> type
...  
<class 'type'>
>>> type(d)
...  
<class 'set'>
>>> s=set
...  
>>> s=set(["b","h","k"])
...  
>>> type(s)
...  
<class 'set'>
>>> s[1]
...  
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    s[1]
TypeError: 'set' object is not subscriptable
>>> s.add("g")
...  
>>> s
...  
{'g', 'k', 'b', 'h'}
>>> s.update("u")
...  
>>> s
...  
{'b', 'u', 'g', 'k', 'h'}
>>> s.discard("u")
...  
>>> s
...  
{'b', 'g', 'k', 'h'}
