Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# string methods
#len()
a="Python"
len(a)
6
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1

#count()
a="twinkle twinkle little star"
a.count("twinkle")
2
a.count("t")
5
a.count("a")
1
a.count(" ")
3
a.count("i")
3
>>> 
>>> a="123456"
>>> a.count("3")
1
>>> a=1,2,3,4,5,6
>>> a.count(3)
1
>>> a=123
>>> a.count(3)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a.count(3)
AttributeError: 'int' object has no attribute 'count'
>>> 
>>> #find a string
>>> a="code"
>>> a[2]
'd'
>>> a.find("d")
2
>>> b="hello"
>>> b.find("l")
2
>>> b[2:4]
'll'
>>> b.find("k")
-1
>>> 
>>> #escape sequence
>>> #\n -> new line
>>> #\t -> tab space
>>> a="name\nmobileno\tmailid\ncollege\tbranch"
>>> print(a)
name
mobileno	mailid
college	branch
>>> a='name:Manikanta\nmobileno:8541234710\tmailid:manikata@codegnan.com\ncollege:AIT\tbranch:ECE'
>>> print(a)
name:Manikanta
mobileno:8541234710	mailid:manikata@codegnan.com
college:AIT	branch:ECE
