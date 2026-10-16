Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# Datatype Conversions

#int
int(7)
7
int(7.9)
7
int("hi")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int("hi")
ValueError: invalid literal for int() with base 10: 'hi'
int(8+7j)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    int(8+7j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0

#Float
float(7)
7.0
float(7.9)
7.9
float("hi")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    float("hi")
ValueError: could not convert string to float: 'hi'
float(6+8j)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    float(6+8j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0

#String
str(7)
'7'
str(7.9)
'7.9'
str("hi")
'hi'
str(6+7j)
'(6+7j)'
str(True)
'True'
str(False)
'False'
>>> 
>>> #complex
>>> complex(7)
(7+0j)
>>> complex(7.9)
(7.9+0j)
>>> complex("hi")
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    complex("hi")
ValueError: complex() arg is a malformed string
>>> complex(6+8j)
(6+8j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> 
>>> #Boolaen
>>> Bool(4)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    Bool(4)
NameError: name 'Bool' is not defined. Did you mean: 'bool'?
>>> bool(6)
True
>>> bool(7.9)
True
>>> bool("hi")
True
>>> bool(6+7j)
True
>>> bool(True)
True
>>> bool(False)
False
