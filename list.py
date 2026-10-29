Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# list[]
a=[2, 4.2, "python", 8+6j, True, False]
a
[2, 4.2, 'python', (8+6j), True, False]
type(a)
<class 'list'>
b=4.6
b
4.6
type(b)
<class 'float'>
c=[4.6]
type(c)
<class 'list'>

#methods
#append
a=["python", "ai", "DSA", "java","c"]
a.append("C++")
a
['python', 'ai', 'DSA', 'java', 'c', 'C++']
a.append("ml","R")
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a.append("ml","R")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["ml","R"])
a
['python', 'ai', 'DSA', 'java', 'c', 'C++', ['ml', 'R']]

#extend
a=['python', 'ai', 'DSA', 'java', 'c', 'C++']
a.extend(["ml","R"])
a
['python', 'ai', 'DSA', 'java', 'c', 'C++', 'ml', 'R']
#insert()
a=['python', 'ai', 'DSA', 'java', 'c', 'C++']
a.insert(1,"ML")
a
['python', 'ML', 'ai', 'DSA', 'java', 'c', 'C++']
a.insert(2,"R")
a
['python', 'ML', 'R', 'ai', 'DSA', 'java', 'c', 'C++']
a.insert(0,"R")
a
['R', 'python', 'ML', 'R', 'ai', 'DSA', 'java', 'c', 'C++']


#index
a=["apple","mango","kiwi"]
a.index("kiwi")
2
b=a.copy()
b
['apple', 'mango', 'kiwi']
#copy
a.copy()
['apple', 'mango', 'kiwi']
c=b.copy()
c
['apple', 'mango', 'kiwi']

#pop()
a=["vja","vzg","hyd"]
a.pop()
'hyd'
a.pop(1)
'vzg'
a.pop("vja")
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    a.pop("vja")
TypeError: 'str' object cannot be interpreted as an integer
a.pop()
'vja'
a
[]

#remove()
a=['python', 'ML', 'R', 'ai', 'DSA', 'java', 'c', 'C++']
a.remove("ML")
a
['python', 'R', 'ai', 'DSA', 'java', 'c', 'C++']
a.remove("C++")
a
['python', 'R', 'ai', 'DSA', 'java', 'c']
a.remove()
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    a.remove()
TypeError: list.remove() takes exactly one argument (0 given)
a.remove(1)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    a.remove(1)
ValueError: list.remove(x): x not in list
>>> 
>>> a=["java","R","C"]
>>> a.clear()
>>> a
[]
>>> a.append("Python")
>>> a
['Python']
>>> 
>>> #sort()
>>> a=['python', 'ML', 'R', 'ai', 'DSA', 'java', 'c', 'C++']
>>> a.sort()
>>> a
['C++', 'DSA', 'ML', 'R', 'ai', 'c', 'java', 'python']
>>> b=[13, 5, 2, 54, 32,0]
>>> b.sort()
>>> b
[0, 2, 5, 13, 32, 54]
>>> a=['python', 'ML', 'R', 'ai',5, 2, 54, 32,0]
>>> a.sort()
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
>>> a=["This does not copy anything.","t gives the existing list a second label.","you will notice that a changes too."]
>>> a.sort()
>>> a
['This does not copy anything.', 't gives the existing list a second label.', 'you will notice that a changes too.']
>>> a=["This does not copy anything.","It gives the existing list a second label.","you will notice that a changes too."]
>>> a.sort()
>>> a
['It gives the existing list a second label.', 'This does not copy anything.', 'you will notice that a changes too.']
>>> a=[4.5, 2.3, 5.6, 1.2]
>>> a.sort()
>>> a
[1.2, 2.3, 4.5, 5.6]
>>> a=[True, True, False, True, False]
>>> a.sort()
>>> a
[False, False, True, True, True]
>>> a=[4, 2.3, 4, 1.3]
>>> a.sort()
>>> a
[1.3, 2.3, 4, 4]

#reverse()
a=['python', 'ML', 'R', 'ai', 'DSA', 'java', 'c', 'C++']
a.reverse()
a
['C++', 'c', 'java', 'DSA', 'ai', 'R', 'ML', 'python']
a=[1.2, 2.3, 4.5, 5.6]
a.reverse()
a
[5.6, 4.5, 2.3, 1.2]

#len()
a=['python', 'ML', 'R', 'ai', 'DSA', 'java', 'c', 'C++']
len(a)
8
b="python"
len(b)
6
c=["python"]
len(c)
1

#count())
a=['python', 'ML', 'R', 'ai', 'DSA', 'java', 'c', 'C++','java']
a.count("C++")
1
a.count("java")
2
