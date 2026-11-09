#loops: loops are used to repeat a block of code multiple times without writing it again and again.
# loops : 1. for , 2.while, 3.range 4.break 5.continue 6.pass

#1.for loop(): A for loop is used to iterate over a sequence (such as a string, list, tuple, or range) and execute a block of code repeatedly.

# for
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
#dict()
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

#set
'''
a={2.0,3.7,4.7,5.9,6.3,7.4,8.9}
b={"Jay", "HYd", "VIJ", "VZG"}
c={8+9j, 5+7j, 4+3j, 6+9j}
d={True, False, True, True}


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

#dictionary
'''
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

b={101.1:2.3, 102.1:3.3, 103.1:4.3}
for i in b:
    print(i)
print(type(b))
print(type(i))

for i in b.keys():
    print(i)
print(type(b))
print(type(i))

for i in b.values():
    print(i)
print(type(b))
print(type(i))

for i in b.items():
    print(i)
print(type(b))
print(type(i))


c={"name":"Mani", "place":"hyd", "mail":"sai@32"}
for i in c:
    print(i)
print(type(c))
print(type(i))

for i in c.keys():
    print(i)
print(type(c))
print(type(i))

for i in c.values():
    print(i)
print(type(c))
print(type(i))

for i in c.items():
    print(i)
print(type(c))
print(type(i))

'''


'''
#task
#a=["apple", "banana", "grapes"] -> ["APPLE", "BANANA", "GRAPES"]
a=["apple", "banana", "grapes"]

b=str(a)
print(b.upper())

for i in a:
    print(i.upper(), end=" ")

we are using empty list b, because list is not possible in for loop

b=[]
for i in a:
    i = i.upper()
    b.append(i)
print(b)
'''

'''
a=[2,3.4,"python",4+9j, True]
print(type(a))
print(type(a[0]))

for i in a:
    print(i)
    print(type(i))
'''


### While loop
'''
a=10
while a>1:
    print(a)'''

'''
a=10
while a>1:
    print(a)
    a=a-1
    '''
'''
a=10
while a>=1:
    print(a)
    a=a-1'''

'''
a=10
while a>1:
    a=a-1
    print(a)'''

'''
a=10
while a>1:
    print(a)
    a-=1
'''
'''
a=20
while a>5:
    print(a)
    a+=1
'''
'''
a=20
while a>=5:
    print(a)
    a-=1'''

'''
a=5
while a<=100:
    print(a)
    a*=2'''

'''
while True:
    a=int(input("Enter the value:"))
    if a>=18:
        print("Eligible for voting")
    else:
        print("not Eligible for voting")
'''

'''
while 1:
    a=['a','e','i','o','u', 'A','E','I','O','U']
    char = input("Enter the Character:")
    if char in a:
        print("the character is vowel")
    else:
        print("the character is consonant")'''



#range()
#start-stop-step

#1.stop

'''
for i in range(10):
    print(i, end=" ")'''

'''
for i in range(2, 15):
    print(i, end=" ")
'''

#real time example
#print 1000 numbers
'''
for i in range(1, 1001):
    print(i, end=" ")


b=[]
for i in range(1,1001):
    b.append(i)
print(b)
'''

#task
#2,4,6,8,10,12,16,18
#0,3,6,9,12,15,18,21,24,27
#5,10,15,20,25,30,35,40,45

'''
#1.2,4,6,8,10,12,16,18
for i in range(2,20,2):
    print(i, end=" ")

#0,3,6,9,12,15,18,21,24,27
for i in range(0,30,3):
    print(i, end=" ")

#5,10,15,20,25,30,35,40,45
for i in range(5,50,5):
    print(i, end=" ")
    '''


#task
#student grade system
'''
marks       grades
91 to 101   grade-a
81 to 91    grade-b
71 to 81    grade-c
50 to 71    grade-d
50 below    fail
'''
marks = int(input("Enter the marks:"))

if marks in range(91,101):
    print("grade-a")
elif marks in range(81,91):
    print("grade-b")
elif marks in range(71,81):
    print("grade-c")
elif marks in range(51,71):
    print("grade-d")
elif marks in range(51):
    print("fail")
else:
    print("enter the marks between 0 to 100")
    
    
'''
marks = int(input("Enter the marks: "))

for i in range(marks, 101):
    if i >= 91:
        print("Grade A")
    elif i >= 81:
        print("Grade B")
    elif i >= 71:
        print("Grade C")
    elif i >= 50:
        print("Grade D")
    else:
        print("Fail")
    break


marks = int(input("Enter the marks: "))

while marks < 101:
    if marks >= 91:
        print("Grade A")
    elif marks >= 81:
        print("Grade B")
    elif marks >= 71:
        print("Grade C")
    elif marks >= 50:
        print("Grade D")
    else:
        print("Fail")

    marks = 101
'''



