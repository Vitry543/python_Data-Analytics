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

while 1:

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

    rail_ticket(price, gender)

