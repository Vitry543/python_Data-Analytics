#conditions
# we mainly use 4 operators in python conditions: 1.Comparsion operators 2.Logical operators 3.Identity operators 4.Membership operators

#if-conditions
#1.using Comparison operators
#<, >, <=, >=, ==, !=

'''
a=10
b=30
if a>b:
    print("a is greater than b")
'''

'''
a=20
b=10
if a>b:
    print("a is greater than b")

a=8
b=9
if a<=b:
    print("a is less than or equal b")


a=88
b=10
if a>=b:
    print("a is greater than or equal b")

a=88
b=10
if a!=b:
    print("a is not equal b")

a=9
b=9
if a==b:
    print("a is equal to b")
'''

#using run time input
'''
a=int(input("Enter the value:"))
b=int(input("Enter the value:"))
if a>b:
    print("a is greater than b")


a=int(input("Enter the value:"))
b=int(input("Enter the value:"))
if a<b:
    print("a is less than b")

'''

'''
a=int(input("Enter the value:"))
if a<20:
    print("a is less than 20")


#using String
a="python"
if a!="java":
    print("True")

'''

#2.using Logical operators
#and, or, not

#1.and
'''
a=10
b=20
if a<b and b>a:
    print("true")

a=20
b=12
if a<=b and b>=a:
    print("true")

a=20
b=10
if a!=b and a==b:
    pritn("true")

'''

#2.or
'''
a=5
b=75
if a<b or b>a:
    print("true")

a=34
b=12
if a<=b or b>=a:
    print("true")

a=20
b=20
if a!=b or a==b:
    print("true")'''

#3.not
'''
a=10
b=20
if not a<b:
    print("less")

a=34
b=42
if not a>b:
    print("greater")

a=10
b=20
if not a<b and a>b:
    print("less")
'''

#using run time input
'''
a=int(input("Enter the value:"))
b=int(input("Enter the value:"))
if a>b and b<a:
    print("a is greater")

if a>b or b<a:
    print("True")

if not a>b or b<a:
    print("True")


a=int(input("Enter the value:"))
b=int(input("Enter the value:"))
if not a>b and b<a:
    print("True")
'''

#using identify operators
# is, is not
'''
a=9
if type(a) is int:
    print("it is int")


a=9
if type(a) is not int:
    print("it is not int")
  

a=int(input("Enter the value:"))
if type(a) is int:
    print("it is int")

a=float(input("Enter the value:"))
if type(a) is float:
    print("it is float")

a=input("Enter the value:")
if type(a) is str:
    print("it is String")


a=9.9
if type(a) is float:
    print("it is float")

a="python"
if type(a) is str:
    print("it is string")
'''

#using membership operators
# in, not in
'''
a=2,3,4,5,6,7,8,9
if 6 in a:
    print("true")

if 10 not in a:
    print("true")



a=int(input("Enter the value:"))
if 20 in a:
    print("true")
#error: if 20 in a:
TypeError: argument of type 'int' is not a container or iterable
'''

'''
a=[2,3,4,5,6,7,8,9]
b=int(input("Enter the value:"))
if b in a:
    print("true")
'''


#tasks
#if marks>90 they are eligible for placements
'''
marks=int(input("Enter the marks:"))
if marks>=90:
    print("your eligible for placements")'''
    
#electricity bill
# units = 300 and above ->high electricity usage
units=int(input("Enter the units:"))
if units>=300:
    print("high electricity  usage")