Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Format methods
>>> a="motu"
>>> b="pathlu"
>>> #format()
>>> print("hello {}{}".format(a,b))
hello motupathlu
>>> print("hello {} {}".format(a,b))
hello motu pathlu
>>> print("hello {} hello {}".format(a,b))
hello motu hello pathlu
>>> 
>>> #f-string
>>> a="sweety"
>>> b="cuty"
>>> print(f"hello {a} {b}")
hello sweety cuty
>>> print(f"hello {a} hello {b}")
hello sweety hello cuty
>>> 
>>> a=10
>>> b=20
>>> print("the multiplication of a and b", a*b)
the multiplication of a and b 200
>>> print("the multiplication of {} and {} is".format(a*b))
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print("the multiplication of {} and {} is".format(a*b))
IndexError: Replacement index 1 out of range for positional args tuple
>>> print("the multiplication of {} * {} is".format(a,b))
the multiplication of 10 * 20 is
>>> print("the multiplication of {} * {} is {}".format(a,b, (a*b)))
the multiplication of 10 * 20 is 200
>>> print(f"the multiplication of {a} and {b} is {a*b}")
the multiplication of 10 and 20 is 200
>>> print("the multiplication of a * b is {}".format((a*b)))
the multiplication of a * b is 200
