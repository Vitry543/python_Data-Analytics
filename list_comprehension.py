# List Comprehension

#syntax
# a=[expersion for var in collection/range]

# ["codegnan", "python", "course"] -> ["CODEGNAN","PYTHON","COURSE"]


a=["codegnan", "python", "course"]

# 1.using other METHOD
'''b=str(a)
print(b.upper())'''

'''for i in a:
    print(i.upper(),end=",")'''

# 2. Using List Comprehension
'''b=[i.upper() for i in a]
print(b)'''


#tasks

#["hyd", "vzg", "vja"] -> ["Hyd","Vzg","Vja"]
'''a=["hyd", "vzg", "vja"]
b=[i.capitalize() for i in a]
b=[i.title() for i in a]
print(b)'''


#[1,2,3,5,6,7,8,12,13] -> [1,4,9,25,36,49,64,144,169]
'''a=[1,2,3,5,6,7,8,12,13]
b=[i**2 for i in a]
c=[i*i for i in a]
d=[pow(i,2) for i in a]
print(b)
print(c)
print(d)'''


#input - 16, output -> 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
'''a=[i for i in range(16)]
print(a)'''

# [print(i, end=",") for i in range(16)]


#if usage in list comprehension

#task
#range(1, 21) -> print Even Numbers

'''a=[i for i in range(21) if i%2==0]
print(a)'''

#square even numbers
'''a=[i**2 for i in range(21) if i%2==0]
print(a)'''



#["apple","mango","kiwi","dragon","berry","grapes","banana"]

'''a=["apple","mango","kiwi","dragon","berry","grapes","banana"]
b=[i for i in a if "a" in i]
print(b)

c=[i for i in a if "a" not in i]
print(c)'''


# No elif usage in list comprehension

# if-else usage in list comprenhension

#range(31) -> even number **2 and odd*5
'''a = [i**2 if i % 2 == 0 else i * 5 for i in range(31)]
print(a)'''


#[1,2,3,4,5] + [5,4,3,2,1] -> [6,6,6,6,6]
'''a= [1,2,3,4,5]
b= [5,4,3,2,1]
c=[a[i]+b[i] for i in range(len(a))]
print(c)

c=[a[i]+b[i] for i in range(5)]
print(c)

a= [1,2,3,4,5]
b= [5,4,3,2,1,0]
c=[a+b for a,b in zip(a,b)]
print(c)'''
#zip: automatically stops when the shorter list (a) runs out of items.


