Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Variables

a = 2
print(a)
2
b = 5
print(5)
5
print(b)
5
x=90
print(X)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(X)
NameError: name 'X' is not defined. Did you mean: 'x'?
print(x)
90
z=50
print(z)
50
print(Z)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(Z)
NameError: name 'Z' is not defined. Did you mean: 'z'?
Z = 50
print(z)
50
del z
print(z)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(z)
NameError: name 'z' is not defined. Did you mean: 'Z'?

9 = 20
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
a9 = 20
print(a9)
20
9a=20
SyntaxError: invalid decimal literal
a0123 = 43
print(a0123)
43
print(a012)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print(a012)
NameError: name 'a012' is not defined. Did you mean: 'a0123'?
print(a0123)
43

name = "Mani"
print(name)
Mani
print("name")
name
city="snd"
print(city)
snd
country = "India"; print(country)
India

@=90
SyntaxError: invalid syntax
$=90
SyntaxError: invalid syntax
_=90
print(_)
90
_a=30; print(_a)
30
 a=90
 
SyntaxError: unexpected indent


#keywords
if = 30
SyntaxError: invalid syntax
else=90
SyntaxError: invalid syntax

#Build-in
int=80
print(int)
80
float=90;print(float)
90

#single line, Multiple variables
a = 5, b = 6
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=5, b=7
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=5;b=4
print(a+b)
9
a,b=4,5
print(a,b)
4 5
print(a+b)
9

# Single variable, Multiple values
a = 2, 3, 4, 5, 6, 7
print(a)
(2, 3, 4, 5, 6, 7)
a, b, c = 2, 3, 4, 5, 6, 7, 8
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a, b, c = 2, 3, 4, 5, 6, 7, 8
ValueError: too many values to unpack (expected 3, got 7)
a,b,c=(3,4,5)
print(a,b,c)
3 4 5
#above one is known as unpack of values


first name = "Pooja"
SyntaxError: invalid syntax
first_name = "Pooja"
print(first_name)
Pooja
fname = "Mani"
>>> lname = "B"
>>> print(fname+lname)
ManiB
>>> print(fname+" "+lname)
Mani B
>>> print(fname,lname)
Mani B
>>> 
>>> 
>>> NAME = "Pooja"
>>> print(NAME)
Pooja
>>> Name = "Pooja"
>>> print(Name)
Pooja
>>> name = "Mani" ; print(name)
Mani
... 
>>> 
>>> a,b,c = 100
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    a,b,c = 100
TypeError: cannot unpack non-iterable int object
>>> a=b=c=10
>>> print(a,b,c)
10 10 10
>>> 
>>> a=10
>>> print(10)
10
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined. Did you mean: 'a9'?
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined. Did you mean: 'a9'?
