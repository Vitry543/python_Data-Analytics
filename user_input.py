# Run-time (user) input

'''
a=10
b=20
print(a+b)
'''

'''
a=10
b=20
c=a+b
print(c)
'''

# print(10+20)

'''
a=int(input("Enter the a value"))
b=int(input("Enter the b value"))
print(a+b)'''

'''
a=float(input("Enter the a value"))
b=float(input("Enter the b value"))
print(a+b)'''

'''
a=str(input("Data1"))
b=str(input("Data2"))
print(a+b)'''

'''
a=input("Data1")
b=input("Data2")
print(a+b)'''

'''
a=complex(input("Enter the a value"))
b=complex(input("Enter the b value"))
print(a+b)'''

'''
a=bool(input("Enter the a value"))
b=bool(input("Enter the b value"))
print(a+b)'''

'''
a=bool(input("Enter the a value"))
b=bool(input("Enter the b value"))
c=bool(input("Enter the c value"))
print(a+b+c)
'''
'''
a=int(input("Enter the a value"))
b=int(input("Enter the b value"))
option = int(input("Enter the option 1.add 2.sub 3.mul"))
print(a+b)
print(a-b)
print(a*b)'''

"""
a=int(input("Enter the a value"))
b=int(input("Enter the b value"))
option = int(input('''Enter the option
                   1.add
                   2.sub
                   3.mul'''))
print(a+b)
print(a-b)
print(a*b)
"""

'''
a=int(input("Enter the a value"))
b=int(input("Enter the b value"))
option = input("Enter the option add sub mul")
print(a+b)
print(a-b)
print(a*b)
'''
'''
a=int(input())
b=int(input())
print(a+b)'''

'''
a=input()
b=input()
print(a+b)
'''

### TASKS
'''
a=["code","python","course"]
#["CODE", "PYTHON", "COURSE"]
a=str(a)
print(a)
print(type(a))
a=a.upper()
print(a)


a = ["code", "python", "course"]
output = [a[0].upper(), a[1].upper(), a[2].upper()]
print(type(a[0]))
print(output)
'''

'''
a=[2,3,4,5,6,7,'code']
#[2,3,4,5,6,7,'c','o','d','e']
a=a[:-1]+list(a[-1])
print(a)

b=[2,3,4,5,6,7,'code']
b.remove('code')
b.extend("code")
print(b)
'''

'''
a=['python','java','c','c++']
#['python','java','dsa','c','c++']
a.insert(2,'dsa')
print(a)

'''

'''
a=(10,20,30,40)
#(10,20,30,40,50)
b=list(a)
b.append(50)
a=tuple(b)
print(a)
'''

'''
a={3,4,5,6,7,8,9,10}
#{4,5,6,7,8,9,10}
a.pop()
print(a)

'''

'''
a=['apple','banana']
#a['apple','banana','grapes','mango']
a.extend(['grapes','mango'])
print(a)
'''