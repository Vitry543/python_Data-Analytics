Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# strig methods
#upper()
a="code"
b="python"
a.upper()
'CODE'
b.upper()
'PYTHON'

#lower()
a="PYTHON"
b="SAI"
a.lower()
'python'
b.lower()
'sai'

a="python"
a.upper("p")
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a.upper("p")
TypeError: str.upper() takes no arguments (1 given)
a[0].upper()
'P'

# capitalize()
a.capitalize()
'Python'
b.capitalize()
'Sai'
#title
a="python course"
a.title()
'Python Course'
a="i am in class"
a.title()
'I Am In Class'
a.capitalize()
'I am in class'


#isupper()
a="PYTHON"
a.isupper()
True
b="Python COURSE"
b.isupper()
False

# islower()
a="python"
a.islower()
True
b="pYTHON course"
b.islower()
False

#isalpha()
a="hello"
a.isalpha()
True
a="Hello world"
a.isalpha()
False
a="Helloworld"
a.isalpha()
True

#isdigit
a="1234"
a.isdigit()
True
a="123ad"
a.isdigit()
False

#startswith()
a="python course"
a.startswith("p")
True
#endswith()
a.endswith("e")
True

#isalnum()
a="sai123"
a.isalnum()
True
a="1234"
a.isalnum()
True
a="hello"
a.isalnum()
True
b="hello32#hg"
b.isalnum()
False

#strip()
#rstrip() lstrip()
a="       sai      "
a.strip()
'sai'
a.lstrip()
'sai      '
a.rstrip()
'       sai'


#split()
a="python java C  C++"
a.split()
['python', 'java', 'C', 'C++']
b="I am learning Python"
b.split()
['I', 'am', 'learning', 'Python']

c=b.split()
c
['I', 'am', 'learning', 'Python']
c[1].upper()
'AM'
c[0].lower()
'i'
c[2].capitalize()
'Learning'

#join()
a="apple","banana","grapes"
"".join(a)
'applebananagrapes'
" ".join(a)
'apple banana grapes'
"s".join(a)
'applesbananasgrapes'

b="hello"
"k".join(b)
'hkeklklko'
>>> 

>>> #concatenation()
>>> a="code"
>>> b="gnan"
>>> print(a+b)
codegnan
>>> a="python"
>>> b="course"
>>> print(a+" "+b)
python course
>>> 
>>> a="sai"
>>> b="b"
>>> print(a+b)
saib
>>> 
>>> fname="sai"
>>> lname="b"
>>> print(fname+" "+lname)
sai b
>>> print(fname.title()+" "+lname.title())
Sai B
>>> print((fname+" "+lname).title())
Sai B
>>> print((fname+" "+lname).capitalize())
Sai b
>>> 
>>> #formatting
>>> a=5
>>> b=7
>>> print(a+b)
12
>>> print("the sum of", a+b)
the sum of 12
>>> 
>>> city=vja"
SyntaxError: unterminated string literal (detected at line 1)
>>> city="vja"
>>> print("city is" ,city)
city is vja
>>> 
