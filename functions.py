# functions

'''a=10
b=20
print("The sum is", a+b)
print("The diff is",a-b)
print("The product is", a*b)

a=100
b=200
print("The sum is", a+b)
print("The diff is",a-b)
print("The product is", a*b)

a=1000
b=2000
print("The sum is", a+b)
print("The diff is",a-b)
print("The product is", a*b)'''

# now using functions
'''def calculate(a,b):
    print("The sum is", a+b)
    print("The diff is",a-b)
    print("The product is", a*b)
    

calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''

#//, **, %
'''def calculate1(a,b):
    print("the floor division:",a//b)
    print("The Power a of b is", a**b)
    print("The Modules is",a%b)

calculate1(4,2)
calculate1(20,30)
calculate1(30,2)'''


'''def add(a,b):
    print(a+b)
add(5,4)'''

#user input 
'''def cal():
    a=int(input("A value"))
    b=int(input("B Value"))
    print(a+b)
cal()'''

'''while 1:
    def cal():
        a=int(input("A value"))
        b=int(input("B Value"))
        print(a+b)
    cal()'''

#recursive function
'''def cal():
    a=int(input("A value"))
    b=int(input("B Value"))
    print(a+b)
    cal()
cal()'''


# Full name
'''def fullname():
    f_name = input("Enter the first name")
    l_name = input("Enter the last name")
    print((f_name+ " " + l_name).title())
fullname()


# recursive function vs while loop

# recursive 
# Uses the call stack (memory).
# Must have a base case to stop.
# Good for problems with self-similar structure:
# Tree traversal
# Graph search
# Factorial
# Fibonacci (optimized versions)

def countdown(n):
    if n == 0:      # base case
        print("Done")
        return
    print(n)
    countdown(n - 1)   # recursive call

countdown(5)

#  While
# Repeats using iteration, not self-calls.
# Uses very little extra memory.
# Usually faster than recursion.
# Suitable for:
# Game loops
# Servers
# Menu-driven programs
# Continuous monitoring

n = 5

while 1:
    if n == 0:
        print("Done")
        break
    print(n)
    n -= 1
    '''


#print vs return

# print just shows the human user output in a console
# print()
# -> Displays output on the screen.
# -> Does not send a value back to the caller.
# -> Mainly used for debugging or user output.


# return will terminate the function & gives back a value from the function
# -> Sends a value back to the caller.
# -> Ends the function immediately.
# -> Allows the result to be stored, reused, or passed to other functions.


# codes
'''def mul(a,b):
    print(a*b)
mul(3,4)'''

'''def mul(a,b):
    return a*b
# mul(3,4)
print(mul(3,4))

def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(2,3)'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    # return c
    # return d
    # return e
    return c,d,e
print(cal(3,4))'''


'''def cal():
    a=int(input())
    b=int(input())
    return a+b
print(cal())'''



# Tasks
'''def cal():
    a=int(input("Enter the a value"))
    b=int(input("Enter the b value"))
    option = input("Enter your option\n 1.add\n 2.sub\n 3.mul\n 4.div")
    if option == "1":
        return a+b
    elif option == "2":
        return a-b
    elif option == "3":
        return a*b
    elif option == "4":
        if b!=0:
            return a/b
        else:
            return "Error! not divisble by zero"
    else:
        return "Wrong option"
print(cal())'''

'''
while 1:
    def cal():
        a=int(input("Enter the a value"))
        b=int(input("Enter the b value"))
        option = input("Enter your option\n 1.add\n 2.sub\n 3.mul\n 4.div")
        if option == "1":
            print("the add is",a+b)
        elif option == "2":
            print("the sub is",a-b)
        elif option == "3":
            print("The mul is",a*b)
        elif option == "4":
            if b!=0:
                print("The division is",a/b)
                break
            else:
                print("Error! not divisble by zero")
        else:
            print("Wrong option")
    cal()
'''


        

'''def cal():
    a = int(input("Enter the a value: "))
    b = int(input("Enter the b value: "))

    def add():
        return a + b

    def sub():
        return a - b

    def mul():
        return a * b

    def div():
        if b != 0:
            return a / b
        else:
            return "Error! Not divisible by 0"

    option = input(
        "Enter your option\n"
        "1. Add\n"
        "2. Sub\n"
        "3. Mul\n"
        "4. Div\n"
    )

    if option == "1":
        return add()
    elif option == "2":
        return sub()
    elif option == "3":
        return mul()
    elif option == "4":
        return div()
    else:
        return "Wrong choice"


print(cal())'''



'''def add():
    print(a + b)

def sub():
    print(a - b)
def mul():
    print(a * b)

def div():
    if b != 0:
        print(a / b)
    else:
        print("Error! Not divisible by 0")
while 1:
    a=int(input("Enter the a value"))
    b=int(input("Enter the b value"))

    option = input(
            "Enter your option\n"
            "1. Add\n"
            "2. Sub\n"
            "3. Mul\n"
            "4. Div\n"
        )

    if option == "1":
        add()
    elif option == "2":
        sub()
    elif option == "3":
        mul()
    elif option == "4":
        div()
    else:
        print("Wrong choice")'''


# Keyword and Positional Arguments

'''def Details(id, name, mailid):
    id = 10
    name="sai"
    mailid = "sai@gmail.com"
    print(id, name, mailid)
Details(id="id", name="name", mailid="mailid")'''


'''def Details(id, name, mailid):
    print(id, name, mailid)
Details(id="id", name="name", mailid="mailid")
Details(id=10, name="sai", mailid="sai@gmail.com")
Details(40, "veera", "veera@gmail.com")
Details("veera", "veera@gmail.com", 40)
Details(name="Veera", mailid="Veera@gmail.com", id=40)'''


# tasks
'''def employee():
    name=input()
    designation=input()
    salary=float(input())
    print(name, designation, salary)
employee()'''

'''def employee(name, designation, salary):
    print(name, designation, salary)
employee("sai","DA",25000.00)
employee(name="sai", designation="DA", salary=25000.00)
employee(25000.00, "sai", "DA")
employee(salary=34211.00, designation="DA", name="Sai")'''


# Default Arguments
'''def Grocery(item, price):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("rice", 2000)'''

'''def Grocercy(item="sugar", price=100):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocercy()'''

'''def Grocery(item, price=200):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("dhal")'''

'''def Grocery(item="ghee", price): 
    # non default arg follows default arg
    print("item is %s" %item)
    print("price is %.2f" %price)

Grocery(100) 
# output:
#SyntaxError: parameter without a default follows parameter with a default'''


# tasks
# bakery-> name, price, quantity
'''def bakery(name="blackberry", price=200, quantity=2):
    print("cake name is %s" %name)
    print("cake price is %.2f" %price)
    print("Cake Quantity %.2f" %quantity)
bakery()'''


'''def bakery(name, price, quantity=2):
    print("cake name is %s" %name)
    print("cake price is %.2f" %price)
    print("Cake Quantity %s" %quantity)
bakery("blackberry", 200)'''

'''def bakery(name, price=200, quantity=2):
    print("cake name is %s" %name)
    print("cake price is %.2f" %price)
    print("Cake Quantity %s" %quantity)
bakery("blackberry")'''

'''def bakery(name, price, quantity):
    print("cake name is %s" %name)
    print("cake price is %.2f" %price)
    print("Cake Quantity %s" %quantity)
bakery("blackberry",200,2)'''



# * (star) arguments -> * is used to unpack the elements

'''a=[2,3,4,5,6]
print(a)
print(*a)


b=(6,5,4,3,2,1)
print(b)
print(*b)

c={2,3,4,5,6,7,8}
print(c)
print(*c)

d={"name":"sai", "year":2025}
print(d)
print(*d)'''


'''a="codegnan"
print(a)
print(*a)

a="codegnan IT solutions"
print(a)
print(*a)'''

'''a,b,c = 2,3,4,5,6,7,8,9,10,11,12
print(a)
print(b)
print(c)''' #error

'''a,*b,c = 2,3,4,5,6,7,8,9,10,11,12
print(a)
print(*b)

a,*b,c = 2,3,4,5,6,7,8,9,10,11,12
print(a)
print(*b)
print(c)

*a,b,c = 2,3,4,5,6,7,8,9,10,11,12
print(*a)
print(b)
print(c)'''

'''a,b,c = "codegnan"
print(a)
print(b)
print(c)''' #error

'''a,b,c = "cod"
print(a)
print(b)
print(c)'''

'''a,*b,c = "codegnan"
print(a)
print(*b)
print(c)'''


# variable length arguments: they are automatically stores in tuple and we use * arguments

'''def check(*a):
    print(a)
    print(type(a))
check()

check(3,4,5,6,7,8)

b=[2,3,4,5,6,7]
check(*b)

c=(2,3,4,5,6,7)
check(*c)

d={3,4,5,6,7,8,9}
check(*d)

d={"name":"sai", "year":2025}
check(*d)'''

'''def check1(*a):
    d=2
    print(a)
    print(type(a))
    for i in a:
        d=d+i
        print(d, end=" ")
check1()
check1(2,3,4,5,6)

check1(2,3,4,2.3,3.4)'''

# Task
'''def check1(*a):
    d=2
    print(a)
    print(type(a))
    for i in a:
        if type(i) is str:
            pass
        else:
            d=d+i
            print(d, end=" ")
check1(2,3,4,2.2,3.4,"pooja")'''

'''def check1(*a):
    d=2
    print(a)
    print(type(a))
    for i in a:
        # if type(i) is int or type(i) is float:
        if type(i) in (int, float):
            d=d+i
            print(d, end=" ")
check1(2,3,4,2.2,3.4,"pooja", 7+8j, True, False)'''



# task
'''
split bill->
test cases:
            input()                                                 output
total friends - 10 & total amt -> 10000                 bill is 1000 for each member

'''

'''def bill():
    total_frnds= int(input("Enter the total friends"))
    total_amount = float(input("Enter the total amount"))
    splitbill = total_amount / total_frnds
    print("the bill splitting amoung the friends is %.2f"%splitbill)
    print(f"the bill splitting amoung the friends is {splitbill:.2f}")
    print("the bill splitting amoung the friends is {:.2f}".format(splitbill))
bill()'''

# kwargs(**) arguments -> automatically stores in Dict format

'''def Details(**a):
    print(a)
    print(type(a))
Details()

d={"idnos":[101,102,103], "names":["sai", "veera", "satya"],
   "status":["p","a", "p"]}
Details(**d)'''


'''# task return only keys, return only values, returnn both key and values
d={"idnos":[101,102,103], "names":["sai", "veera", "satya"],
   "status":["p","a", "p"]}

#return keys, values, items using dict methods

def details (**d):
    # return keys
    for i in d.keys():
        print(i)
    for i in d:
        print(i)
    # return values
    for i in d:
        print(d[i])
    for i in d.values():
        print(i)
    # return items
    for i in d:
        print(i, d[i])
    for i in d.items():
        print(i)
details(**d)'''

#  2.task
# Both * and ** usage


'''def final(*a, **b):
    d=2
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d, end=" ")
    print()
    # for j in b:
    #     print(j)
    # for j in b.keys():
    #     print(j)
    # for j in b:
    #     print(b[j])
    # for j in b.values():
    #     print(j)
    # for j in b:
    #     print(j, b[j])
    # for j in b.items():
    #     print(j)
    
    for i,j in b.items():
        print("Key is",i)
        print("Values is", j)

a=(2,3,4,5,6,7)
b={"idnos":[101,102,103], "names":["sai", "veera", "satya"],
   "status":["p","a", "p"]}
final(*a)
final(**b)
final(*a, **b)'''

# application
# ----------------------- railway ticket ----------------------

# 1.ticket price: ticket == 1000
# 2.gender ->           male                                                 
                # >60 -> senior citizen  -> flat-30% discount                
                # <60 -> normal citizen   -> flat - 0% discount              
        #   ->             female
        #       >60 -> senior citizen  -> flat-50% discount                
        #       <60 -> normal citizen   -> flat - 30% discount  
        



'''while 1:

    def rail_ticket(ticket, gender):
        
        if gender == "male":
            age = int(input("Enter the male age: "))
            if age >= 60:
                price = ticket - (ticket * (30/100))
                print("The ticket price for senior citizen is: ", price)
            else:
                print("The ticket price is ", ticket)
        elif gender == "female":
            age = int(input("Enter the female age: "))
            if age >= 60:
                price = ticket - (ticket * (50/100))
                print("The ticket price for senior citizen is: ", price)
            else:
                price = ticket - (ticket * (30/100))
                print("the ticket price is ", price)
        else:
            print("Incorrect choice")

    price = int(input("Enter the ticket price: "))
    gender = input("Enter the Geneder Male or Female").lower()

    rail_ticket(price, gender)'''


'''def rail_ticket():
    ticket = int(input("Enter the ticket price: "))
    gender = input("Enter the Geneder Male or female").lower()
    if gender == "male":
        age = int(input("Enter the male age: "))
        if age >= 60:
            price = ticket - (ticket * (30/100))
            print("The ticket price for senoir citizen is: ", price)
        else:
            print("The ticket price is ", ticket)
    elif gender == "female":
        age = int(input("Enter the female age: "))
        if age >= 60:
            price = ticket - (ticket * (50/100))
            print("The ticket price for senior citizen is: ", price)
        else:
            price = ticket - (ticket * (30/100))
            print("the ticket price is ", price)
    else:
        print("Incorrect choice")
rail_ticket()'''


# local and global variable:
# ->a variable is defined inside and outside the function is called global and local variables

# local variable:->a variable is defined inside the function and it is consider as a entire local space is called local variable

# global variable: ->a variable is defined outside the function and it is consider as a entire global space is called global variable


#global variable

#first case with global
'''a=5
def check1():
    print("Inside value is", a)
check1()
print("outside value is",a)'''

# second case with global
'''a=5
def check2():
    a=3
    print("Inside value is",a)
check2()
print("outside value is",a)'''

# third case with global and local variables
'''a=3
def check3():
    a=5
    print("Inside value is",a)
    a=7
    print("Update value is",a+5)
    b=12 #local variable
    b=b+a
    print("value of b", b)
check3()
print("Outside value of a",a)'''
# print("Value of b",b) #output: error! because we cannot access local variable outside the function without global keyword


'''#4th case
#### NOTE:
# usage of global keyword
# -> when user wants to create a variable inside the function directly and carry forward the updated value even outside the function then we need to use global keyword

a=10
def final():
    global a
    print("inside value is",a)
    a=15
    print("updated value is",a) 
    global b
    b=20
    b=b+a
    print("Value of b",b)
final() 
print("value of a",a)
print("b value is ",b)'''


# generators
# No tuple comprehension in above cases if we remove those braceses[] & keep paranthesis () then outcome is generators

# comparsing with list comperhension
# list = [exp for var in collections/Range]

'''a=[i for i in range(16)]
print(a)
print(type(a))'''

# Now Generators
'''a=(i for i in range(16))
print(a)
print(*a)
print(type(a))'''

# print(list(a))
# print(type(a))

# print(tuple(a))
# print(set(a))

# print(set(*a))


##### GENERATOR:
# A Generator is also a function which can be used as an iterator (loop) by producing group of values, where we can use yield keyword. 
# Yield Vs Return

# Return will terminate the function whereas yiled can pass the function and go on with every successive iteration.


'''a,b=[int(x) for x in input("Enter the values").split(",")]
print(a+b)'''


# difference between yield vs return
# 1.Example
'''a,b = (int(x) for x in input("Enter the values").split(","))
def check(a,b):
    while a<b:
        # yield a
        a=a+1
        yield a
print(check(a,b))
print(*check(a,b))'''


'''a,b = (int(x) for x in input("Enter the values").split(","))
def check(a,b):
    while a<b:
        a=a+1
        # return a
    return a
print(check(a,b))
# print(*check(a,b))'''


# 2.Example
'''def mygen():
    # return "python"
    # return "java"
    # return "c"
    return "python","java","c"
print(mygen())
print(*mygen())'''

'''def mygen():
    yield "Python"
    yield "java"
    yield "c"
print(mygen())
print(*mygen())

d=mygen()
# next() -> build-in function
print(next(d))
print(next(d))
print(next(d))'''


# max(), min(), sum()

'''print(max(2,4,8,7,54,32,120))
print(min(23,4,323,1,23,0.5,45))

print(sum([10,20,30]))
a,b,c=20,10,30
print(sum([a,b,c]))
print(sum([a,b,c],5))

a=2,3,4,5,6,7,8,9
print(sum(a))

a=[1,2,3,4,5]
b=[5,4,3,2,1]
print(sum(a,b))'''


# Task
# Marks analysis Report
#  No of Students-> 5
# std1->70, std2->30, std->45, std4->10, std5->100
# output: total no. of sytudents ->100, lowest mark->10, total markls->255, Average -> 67


'''
# students = [f"std{i}" for i in range(1, n+1)]
# marks = []
# for i in range(n):
#     mark = int(input("Enter the marks"))
#     marks.append(mark)

n = int(input("Enter the number of students: "))
marks = [int(input("Enter the marks: ")) for i in range(n)]


print("-------------------Marks Analysis Report -------------------")
print("total no. of Studentts:",n)
print("Maximum marks in a class: ",max(marks))
print("Minimum marks in a class: ",min(marks))
print("total marks in a class: ",sum(marks))
avg = sum(marks) / n
print("Average marks in a class: ",avg)
# print(students)'''



'''

def check():
    n=int(input("Enter the number of students in a class: "))
    marks = [int(input(f"Enter the marks of std{i}: ")) for i in range(1,n+1)]
    
    print("-------------------Marks Analysis Report -------------------")
    print("total no. of Studentts:",n)
    print("Maximum marks in a class: ",max(marks))
    print("Minimum marks in a class: ",min(marks))
    print("total marks in a class: ",sum(marks))
    avg = sum(marks) / n
    print("Average marks in a class: ",avg)
check()'''

# using Generators
'''n=int(input("Enter the number of students in a class: "))

def check():
    marks = (int(input(f"Enter the marks of std{i}: ")) for i in range(1,n+1))
    
    first = next(marks)
    maximum = minimum = total = first
    
    for mark in marks:
        maximumm = max(maximum, mark)
        minimum = min(minimum, mark)
        total +=mark
        
    avg = total / n
    print("Maximum marks in a class: ",maximum)
    print("Minimum marks in a class: ",minimum)
    print("total marks in a class: ",total)
    print("Average marks in a class: ",avg)
check()'''

'''
n=int(input("Enter the no of weeks: "))
marks = [int(input(f"Enter the week{i} marks: ")) for i in range(1,n+1)]
print("-------------------Marks Analysis Report -------------------")
print("total no. of week tests:",n)
print("Maximum marks in a class: ",max(marks))
print("Minimum marks in a class: ",min(marks))
print("total marks in a class: ",sum(marks))
avg = sum(marks) / n
print("Average marks in a class: ",avg)'''



# Build-in Functions
'''print(), next(), type(), sum(), max(), min(), len(), input(), range()'''

'''# dir()
print(dir())
print(dir("__builtins__"))'''


'''# fromkeys()
a="codegnan"
print(a)
print(list(a))
print(tuple(a))
print(set(a))

# print(dict(a))

# using fromkeys
b=dict.fromkeys(a)
print(b)

b=dict.fromkeys(a,"Pooja")
print(b)

b["d"]="Python"
print(b)'''

'''# eval(): evaluate can accept any datatype
# examples
while 1:
    a=int(input("Enter a value"))
    b=int(input("Enter b value"))
    print(a+b)'''

'''while 1:
    a=float(input("Enter a value"))
    b=float(input("Enter b value"))
    print(a+b)'''

'''while 1:
    a=input("Enter a value")
    b=input("Enter b value")
    print(a+b)'''

'''# Now using eval()
while 1:
    a=eval(input("Enter a value"))
    b=eval(input("Enter b value"))
    print(a+b)'''


# zip(): we can combine multiple collections into one collections
'''a=[10,20,30,40,50]
names = ["sumanth","sai","roshan","Mani", "uday"]
print(a+names)

b=zip(a,names)
print(b)

c=list(zip(a, names))
print(c)

c=tuple(zip(a, names))
print(c)

d=set(zip(a, names))
print(d)

d=dict(zip(a, names))
print(d)'''


# task
def bmi():
    height = float(input("Enter the Height:"))
    weight = float(input("Enter the weight"))
    bmis = weight / (height **2)
    print(bmis)
    
    if bmis<18.5:
        print("under weight")
    elif 18.5<= bmis < 24.5:
        print("healthy weight")
    elif 24.5<= bmis <=29.5:
        print("Over Weight")
    else:
        print("Obesity")
bmi()