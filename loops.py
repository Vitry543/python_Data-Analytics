#loops: loops are used to repeat a block of code multiple times without writing it again and again.
# loops : 1. for , 2.while, 3.range 4.break 5.continue 6.pass

#1.for loop(): A for loop is used to iterate over a sequence (such as a string, list, tuple, or range) and execute a block of code repeatedly.
'''
a=[10,20,30,40,50]
for i in a:
    print(i)
    

a=[10,20,30,40,50]
for i in a:
    print(a)

a=[10,20,30,40,50,60]
for i in a:
    print(a)


a=[10,20,30,40,50]
for i in a:
    print(i,end=" ") # end=" " prints a space after each value instead of starting a new line

a=[10,20,30,40,50]
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

'''
a=[10,20,30,40,50]
for i in a:
    print(i)
print(type(a))
print(type(i))
'''
'''
#tuple
b=(5,6,7,8,9,10)
for i in b:
    print(i)
print(type(b))
print(type(i))
'''

'''
#set
c={5,6,7,8,9,2,3}
for i in c:
    print(i)
print(type(c))
print(type(i))
'''

'''
#set
a={"name":"sai", "year":2001, "month":11}
for i in a:
    print(i)
    
for i in a.keys():
    print(i)
for i in a.values():
    print(i)
for i in a.items():
    print(i)
'''

'''
#dict()
a={"name":"sai", "year":2001, "month":11}
for i in a:
    print(i)
    print(type(a))
    print(type(i))
    
for i in a.keys():
    print(i)
    print(type(a))
    print(type(i))
for i in a.values():
    print(i)
    print(type(a))
    print(type(i))
for i in a.items():
    print(i)
    print(type(a))
    print(type(i))

'''

'''
#list
a=[1.2,3.4,5.6,7.8]
b=["Mani", "Sai", "Jai", "Uday"]
c=[8+9j, 5+7j, 4+3j, 6+9j]
d=[True, False, True, True]
for i in a:
    print(i)
print(type(a))
print(type(i))

for j in b:
    print(j)
print(type(b))
print(type(j))

for k in c:
    print(k)
print(type(c))
print(type(k))

for l in d:
    print(l)
print(type(d))
print(type(l))

a=["sai", 8+9j, 4, 4.5, True]
for i in a:
    print(i)
    print(type(i))
print(type(a))
print(type(i))
'''


'''
#tuple
a=(1.2,3.4,5.6,7.8)
b=("Mani", "Sai", "Jai", "Uday")
c=(8+9j, 5+7j, 4+3j, 6+9j)
d=(True, False, True, True)
for i in a:
    print(i)
print(type(a))
print(type(i))

for j in b:
    print(j)
print(type(b))
print(type(j))

for k in c:
    print(k)
print(type(c))
print(type(k))

for l in d:
    print(l)
print(type(d))
print(type(l))
'''

a={2,3,4,5,6,7,8}
b={"Jay", "HYd", "VIJ", "VZG"}
c={}


#task
#a=["apple", "banana", "grapes"] -> ["APPLE", "BANANA", "GRAPES"]
a=["apple", "banana", "grapes"]
b=[]
for i in a:
    i = i.upper()
    b.append(i)
print(b)
