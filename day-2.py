Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s="sumit"
type(s)
<class 'str'>
s="this is GEC vaishali python workshop."
s[0:4]
'this'
s[6:7
  s[6:8]
  
SyntaxError: '[' was never closed
s="this is GEC vaishali python workshop."
  
s[5:6]
  
'i'
s[5:7]
  
'is'
s[-1:]
  
'.'
s[-1:-4]
  
''
s[-4:-1]
  
'hop'
s[-3:-8]
  
''
s[-8:-3]
  
'orksh'
s[0:-1]
  
'this is GEC vaishali python workshop'
s[7:-2]
  
' GEC vaishali python worksho'
s
  
'this is GEC vaishali python workshop.'
[-5:-1]
  
SyntaxError: invalid syntax
s[-5:-1]
  
'shop'
"GEC" in s
  
True
s*2
  
'this is GEC vaishali python workshop.this is GEC vaishali python workshop.'
print("sumit",s)
  
sumit this is GEC vaishali python workshop.
>>> print("sumit %s"%s)
...   
sumit this is GEC vaishali python workshop.
>>> str="this is sumit's house "
...   
>>> str
...   
"this is sumit's house "
>>> s="{{} is state college".fromat("
...                                 
SyntaxError: unterminated string literal (detected at line 1)
>>> s="{{} is state college".fromat("
... s="{{} is state college".fromat("GEC")
...                                 
SyntaxError: unterminated string literal (detected at line 1)
>>> s="{{} is state college".fromat("gec")
...                                 
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    s="{{} is state college".fromat("gec")
AttributeError: 'str' object has no attribute 'fromat'. Did you mean: 'format'?
>>> s="{} is state college".fromat("gec")
...                                 
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    s="{} is state college".fromat("gec")
AttributeError: 'str' object has no attribute 'fromat'. Did you mean: 'format'?
>>> s="{{} is state college".format("gec")
...                                 
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    s="{{} is state college".format("gec")
ValueError: Single '}' encountered in format string
>>> s="{} is state college".format("gec")
...                                 
>>> l=[7,"sumit",4.6,True]
...                                 
>>> tpye(l)
...                                 
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    tpye(l)
NameError: name 'tpye' is not defined. Did you mean: 'tuple'?
>>> l=[7,"sumit",4.6,True]
...                                 
>>> l=[7,9]
...                                 
>>> s="p"



                                    
