Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# Logical
a, b = 3, 4
a<b and a>b
False
a<=b and a>=b
False
a!=b and a==b
False
a<b or a>b
True
a<=b or a>=b
True
a!=b or a==b
True

not True
False
not False
True

# Identify
a=3
type(3) is int
True
type(3) is not int
False
b = 3.4
type(3.4) is float
True
type(3.4)is not float
False
c = 3+9j
c
(3+9j)
type(c) is complex
True
type(c) is not complex
False
a = "Python"
type(a) is str
True
type(a) is not str
False

#membership
a2, 3, 4, 5, 6, 7, 8, 9
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a2, 3, 4, 5, 6, 7, 8, 9
NameError: name 'a2' is not defined. Did you mean: 'a'?
a = 2, 3, 4, 5, 6, 7, 8, 9
9 in a
True
10 in a
False
10 not in a
True


# Bit-wise
a=3
b=4
bin(a)
'0b11'
bin(b)
'0b100'
a&b
0
a|b
7
~a
-4
a=5
b=7
a&b
5

a=4
b=8
a|b
12
>>> a&b
0
>>> ~a
-5
>>> a=3
>>> b=8
>>> a|b
11
>>> 
>>> a=5
>>> ~a
-6
>>> a=-4
>>> ~a
3
>>> -(a+1)
3
>>> # ~ formaula is -(a+1)
>>> a=4
>>> ~a
-5
>>> ~b
-9
>>> 
>>> # xor
>>> a=4
>>> b=5
>>> a^b
1
>>> a=5
>>> b=10
>>> a^b
15
>>> 
>>> a=9
>>> a<<2
36
>>> a>>3
1
>>> a=2
>>> a>>3
0
