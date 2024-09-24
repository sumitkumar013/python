Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("hii")
hii
str=("Tincle tincle little star \, How I wonder what u are ")
print(str)
Tincle tincle little star \, How I wonder what u are 
s={1,2,3}
s
{1, 2, 3}
s.udate("rt")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    s.udate("rt")
AttributeError: 'set' object has no attribute 'udate'. Did you mean: 'update'?
s.update(2)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    s.update(2)
TypeError: 'int' object is not iterable
s.update("4")
s
{'4', 1, 2, 3}
s.update("rte")
s
{1, 2, 3, 't', '4', 'e', 'r'}
s.discard("r")
s
{1, 2, 3, 't', '4', 'e'}
s.discard("n")
s
{1, 2, 3, 't', '4', 'e'}
s.remove("m")
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    s.remove("m")
KeyError: 'm'
s.remove("t")
s
{1, 2, 3, '4', 'e'}
D={}
type(D)
<class 'dict'>
d={}
type(d)
<class 'dict'>
D={101:"civil",102:"ME",105:"cse"}
D
{101: 'civil', 102: 'ME', 105: 'cse'}
D.keys()
dict_keys([101, 102, 105])
D.values()
dict_values(['civil', 'ME', 'cse'])
D[105}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
D[105]
'cse'
D[105]="cse(iot)"
D
{101: 'civil', 102: 'ME', 105: 'cse(iot)'}
D.pop(102)
'ME'
d
{}
d
{}
D
{101: 'civil', 105: 'cse(iot)'}
D.items()
dict_items([(101, 'civil'), (105, 'cse(iot)')])
D.update({105:["cse ,cse iot"]})
D
{101: 'civil', 105: ['cse ,cse iot']}
D[1]
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    D[1]
KeyError: 1
D(1)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    D(1)
TypeError: 'dict' object is not callable
D[105[1]]
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    D[105[1]]
TypeError: 'int' object is not subscriptable
D[105][1]
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    D[105][1]
IndexError: list index out of range
d
{}
d={105:["cse","cseiot"]}
d[105][0]
'cse'
class car:
    def _init_(self):
        slef.brand="suzuki"
        slef.color="blue"
        slef.top_speed=200

        
car=car()
car
<__main__.car object at 0x0000029F3EFCA3C0>
car.brand
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    car.brand
AttributeError: 'car' object has no attribute 'brand'
car.brand()
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    car.brand()
AttributeError: 'car' object has no attribute 'brand'
car=car()
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    car=car()
TypeError: 'car' object is not callable
car.brand
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    car.brand
AttributeError: 'car' object has no attribute 'brand'
Car=car()
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    Car=car()
TypeError: 'car' object is not callable
class car:
    def __init__(self):
        self.brand="suzuki"
        self.color="blue"
        self.top_speed=200

        
Car=car()
car
<class '__main__.car'>
car.brand
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    car.brand
AttributeError: type object 'car' has no attribute 'brand'
Car.brand
'suzuki'
class car:
    def __init__(self,b,c,ts):
        self.brand=b
        self.color=c
        self.top_speed=ts

        
Car=car()
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    Car=car()
TypeError: car.__init__() missing 3 required positional arguments: 'b', 'c', and 'ts'
Car=car("maruti","red",150)
Car.brand
'maruti'
Car=car("tata","green",300)
Car.brand
'tata'
Car.brand
'suzuki'
class car:
    def __init__(self,b,c,ts):
        self.brand=b
        self.color=c
        self.top_speed=ts
        
SyntaxError: multiple statements found while compiling a single statement
class car:
    def __init__(self,b,c,ts):
        self.brand=b
        self.color=c
        self.top_speed=ts
    def accelerate():
        print("your car top soeed is :",self.top_speed)

        
class car:
    def __init__(self,b,c,ts):
        self.brand=b
        self.color=c
        self.top_speed=ts

        
class car:
    def __init__(self,b,c,ts):
        self.brand=b
        self.color=c
        self.top_speed=ts
    def accelerate(self):
        print("your car top soeed is :",self.top_speed)

        
Car=car()
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    Car=car()
TypeError: car.__init__() missing 3 required positional arguments: 'b', 'c', and 'ts'
Car=car("h","p",7)
Car.acclerate()
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    Car.acclerate()
AttributeError: 'car' object has no attribute 'acclerate'. Did you mean: 'accelerate'?
>>> Car.accelerate()
your car top soeed is : 7
>>> class phone:
...     def __init__(self,c,m):
...         self.color=c
...         self.modle=m
...     def android(self)
...     
SyntaxError: expected ':'
>>> class phone:
...     def __init__(self,c,m):
...         self.color=c
...         self.modle=m
...     def android(self):
...         print("your phone is :",m)
... 
...         
>>> p=phone()
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    p=phone()
TypeError: phone.__init__() missing 2 required positional arguments: 'c' and 'm'
>>> p=phone("red","vivo")
>>> p.android()
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    p.android()
  File "<pyshell#97>", line 6, in android
    print("your phone is :",m)
NameError: name 'm' is not defined
>>> class phone:
...     def __init__(self,c,m):
...         self.color=c
...         self.modle=m
...     def android(self):
...         print("your phone is :",self.modle)
... 
...         
>>> p=phone("red","vivo")
>>> P.android()
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    P.android()
NameError: name 'P' is not defined. Did you mean: 'p'?
>>> p.android()
your phone is : vivo
