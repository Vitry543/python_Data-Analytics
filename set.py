Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# set{}
s={2, 3.4, "python", 6+8j, True, False}
s
{False, True, 'python', 3.4, 2, (6+8j)}
type(s)
<class 'set'>
x = {5, 10, 15, 26, 15, 10, 43, 5}
x
{26, 5, 10, 43, 15}

#methods
#add()
s={4, 5, 13, 2, 45, 67}
s.add(90)
s
{2, 67, 4, 5, 13, 90, 45}

#issubset()
a={1,2,3,4,5,6}
b={4,5,6}
b.issubset(a)
True
a.issubset(b)
False

#issuperset()
a={2,3,4,5,6,7,8,9}
b={5,6,7,8,9}
a.issuperset(b)
True
b.issuperset(a)
False

#union()
a={5, 6, 7, 8, 9, 10}
b={1, 2, 3, 4, 5, 6, 7}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

#intersection()
a={5, 6, 7, 8, 9, 10}

b={1, 2, 3, 4, 5, 6, 7}
a.intersection(b)
{5, 6, 7}
b.intersection(a)
{5, 6, 7}

#update()
a={5, 6, 7, 8, 9, 10}
b={1, 2, 3, 4, 5, 6, 7}
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
b.update(a)
b
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
b
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

#difference between union and update
#union
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
a={5, 6, 7, 8, 9, 10}
b={1, 2, 3, 4, 5, 6, 7}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
a
{5, 6, 7, 8, 9, 10}

#update
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


#difference()
a={5, 6, 7, 8, 9, 10}
b={1, 2, 3, 4, 5, 6, 7}
a.difference(b)
{8, 9, 10}
b.difference(a)
{1, 2, 3, 4}

a={1,2,3,4,5}
b={6,7,8,9,10}
a.difference(b)
{1, 2, 3, 4, 5}
b.difference(a)
{6, 7, 8, 9, 10}


#symmetric_difference
a={10, 11, 12, 13, 14, 15}
b={13, 14, 15, 16, 17, 18}
a.symmetric_difference(b)
{10, 11, 12, 16, 17, 18}
b.symmetric_difference(a)
{10, 11, 12, 16, 17, 18}

#intersection_update
a={10, 11, 12, 13, 14, 15}
b={13, 14, 15, 16, 17, 18}
a.intersection_update(b)
a
{13, 14, 15}

a
{13, 14, 15}
b.intersection_update(a)
b
{13, 14, 15}
b
{13, 14, 15}

#difference_update
a={10,20,30,40,50}
b={30,40,50,60,70}
a.difference_update(b)
a
{20, 10}
b.difference_update(a)

b
{50, 70, 40, 60, 30}

a={10,20,30,40,50}
b={30,40,50,60,70}
b.difference_update(a)
b
{70, 60}
a.difference_update(b)
a
{50, 20, 40, 10, 30}


#symmetric_difference_update
a={3, 4, 5, 6, 7, 8, 9}
b={1, 2, 3, 4, 5, 6}
a.symmetric_difference_update(b)
a
{1, 2, 7, 8, 9}
b.symmetric_difference_update(a)
b
{3, 4, 5, 6, 7, 8, 9}

#pop()
a={1,2,3,4,5,6,7,8}
a.pop()
1
a
{2, 3, 4, 5, 6, 7, 8}
a.pop(7)
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    a.pop(7)
TypeError: set.pop() takes no arguments (1 given)

#remove()
a
{2, 3, 4, 5, 6, 7, 8}
a.remove(8)
a
{2, 3, 4, 5, 6, 7}
#discard()
a
{2, 3, 4, 5, 6, 7}
a.discard(2)
a
{3, 4, 5, 6, 7}


#copy()
a= {1,2,3,4,5,6,7,8}
a.copy()
{1, 2, 3, 4, 5, 6, 7, 8}
b=a.copy()
b
{1, 2, 3, 4, 5, 6, 7, 8}

#clear()
a.clear()
a
set()
b=set()
b.add(30)
b
{30}
>>> b.add(40, 45, 34)
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    b.add(40, 45, 34)
TypeError: set.add() takes exactly one argument (3 given)
>>> b.update(40)
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    b.update(40)
TypeError: 'int' object is not iterable
>>> 
>>> a={1,2,3,4,5,6,7,89}
>>> len(a)
8
>>> a.index(89)
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    a.index(89)
AttributeError: 'set' object has no attribute 'index'
>>> a.count(7)
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    a.count(7)
AttributeError: 'set' object has no attribute 'count'
>>> 
>>> #isdisjoint()
>>> a={1,2,3,4,5}
>>> b={6,7,8,9,10}
>>> a.isdisjoint(b)
True
>>> 
>>> a={1,2,3,4,5,6,7}
>>> b={6,7,8,9,10}
>>> a.isdisjoint(b)
False
>>> b.disjoint(a)
Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    b.disjoint(a)
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
>>> b.isdisjoint(a)
False
