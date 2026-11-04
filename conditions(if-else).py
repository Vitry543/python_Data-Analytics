#if-else conditions
#if-else is a decision making statement which is used to execute a block of code based on a condition. If the condition is true, the code inside the 'if' block will be executed, otherwise the code inside the 'else' block will be executed.

'''
a=20
b=3
if a>b:
    print("a is greater than b")
else:
    print("a is less than b")

a=20
b=30
if a>b:
    print("a is greater than b")
else:
    print("a is less than b")
'''

#1.using Comparison operators
#<, >, <=, >=, ==, !=

'''
a=int(input("Enter the value:"))
b=int(input("Enter the value:"))

if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")

if a<b:
    print("a is smaller than b")
else:
    print("b is smaller than a")

if a<=b:
    print("a is less than or equal b")
else:
    print("b is greater than a")
    
if a>=b:
    print("a is greater than or equal b")
else:
    print("b is smaller than a")

if a!=b:
    print("a is not equal to b")
else:
    print("a is equal to b")

if a==b:
    print("a is equal to b")
else:
    print("a is not equal to b")


#using string
a=input("Enter the value:")
b=input("Enter the value:")
if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")
'''


# logical operators
# and, or, not

'''
a = int(input("Enter the value:"))
b= int(input("Enter the value:"))

#and operator
if a>10 and b>10:
    print("Both a and b are greater than 10")
else:
    print("Either a or b is less than or equal to 10")

if a>b and b<a:
    print("Both conditions are true")
else:
    print("Either one or both conditions are false")

if a<=b and b>=a:
    print("b is greater than or equal to a")
else:
    print("b is less than a")

if a!=b and a==b:
    print("Both conditions are true")
else:
    print("Either one or both conditions are false")


#or operator
a = int(input("Enter the value:"))
b= int(input("Enter the value:"))

if a>b or b<a:
    print("Both conditions are true")
else:
    print("Either one or both conditions are false")

if a<=b or b>=a:
    print("b is greater than or equal to a")
else:
    print("b is less than a")

if a!=b or a==b:
    print("Both conditions are true")
else:
    print("Either one or both conditions are false")



#not operator
a= int(input("Enter the value:"))
b= int(input("Enter the value:"))

if not a>b:
    print("a is not greater than b")
else:
    print("a is greater than b")

if not (a>b and b<a):
    print("True")
else:
    print("False")


#identify operators
#is, is not
a= int(input("Enter the value:"))
b= int(input("Enter the value:"))

if a is b:
    print("a and b are same")
else:
    print("a and b are not same")

if a is not b:
    print("a and b are not same")
else:
    print("a and b are same")

if type(a) is int:
    print("a is int")
else:
    print("a is not int")



a=float(input("Enter the value:"))
if type(a) is float:
    print("it is float")
else:
    print("it is not float")

a=input("Enter the value:")
if type(a) is str:
    print("it is String")
else:
    print("it is not String")



#membership operators
#in, not in

a= int(input("Enter the value:"))
if a in [1, 2, 3, 4, 5]:
    print("a is in the list")
else:
    print("a is not in the list")

a= int(input("Enter the value:"))
if a not in [1, 2, 3, 4, 5]:
    print("a is not in the list")
else:
    print("a is in the list")


a=[2,3,4,5,6,7,8,9]
b=int(input("Enter the value:"))
if b in a:
    print("true")
else:
    print("false")

'''

