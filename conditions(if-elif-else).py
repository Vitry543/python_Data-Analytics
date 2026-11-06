#if-elif-else condition

#comparison
'''
a=3
b=6
if a<b:
    print("less")
elif a>b:
    print("greater")
else:
    print("true")


a=3
b=6
if a>b:
    print("less")
elif b>a:
    print("greater")
else:
    print("true")

a=10
b=20
if a==b:
    print("Equal")
elif a!=b:
    print("Not equal")
elif a>b:
    print("greater")

'''

#Logical
#and
'''
a=4
b=40
if a>b and b<a:
    print("greater")
elif a<b and b>a:
    print("less")
elif a==b and a!=b:
    print("True")
else:
    print("False")

#or
a=40
b=400
if a>b or b<a:
    print("greater")
elif a<b or b>a:
    print("less")
elif a==b or a!=b:
    print("True")
else:
    print("False")

#not
    a=40
b=400
if not a>b or b<a:
    print("greater")
elif not a<b or b>a:
    print("less")
elif not a==b or a!=b:
    print("True")
else:
    print("False")



#Identify
#is, is not
a=30
b="python"
if type(a) is str():
    print("Str is True")
elif type(a) is int():
    print("Int is true")
else:
    print("False")

a=30
b="python"
if type(a) is not str():
    print("True")
elif type(a) is not int():
    print("False")
else:
    print(" \n")

#membership
#in, not in
fruit = "apple"
bag = ["banana", "orange", "apple"]

if fruit not in bag:
  print(f"{fruit} is missing from the bag.")
elif fruit in ["banana", "mango"]:
  print("It is a yellow fruit.")
else:
  print(f"{fruit} is found in the bag.")
'''

#task
#1.bakery cake price
'''
s={"redvelvet":1200, "almond cake":1000, "choclate cake":800, "butterscotch":600}
cake = input("Enter the cake name").lower()
if cake in s:
    print("Cake price is:",s[cake])
elif cake not in s:
    print("sorry cake is not available")
else:
    print("Enter correct input")

#or
cake = input("Enter the cake name:")
if cake == "redvelvet":
    print("cake prize is 1200")
elif cake == "almond cake":
    print(1000)
elif cake == "choclate cake":
    print(800)
elif cake == "butterscotch":
    print(600)
else:
    print("sorry cake is not available")
'''

#2.pizza price -> name
'''
s={1000:"bbq pizza", 800: "crispy chicken pizza", 600:"panner pizza", 400:"sweet corn pizza", 200:"frenchfries & coke"}

prize = int(input("Enter the prize:"))
if prize == 1000:
    print("bbq pizza available at that prize")
elif prize == 800:
    print("crispy chicken pizza available at that prize")
elif prize == 600:
    print("panner pizza available at that prize")
elif prize == 400:
    print("sweet corn pizza available at that prize")
elif prize == 200:
    print("frenchfries & coke available at that prize")
else:
    print("no pizza is available at that prize")


s={1000:"bbq pizza", 800: "crispy chicken pizza", 600:"panner pizza", 400:"sweet corn pizza", 200:"frenchfries & coke"}
prize = int(input("Enter the prize:"))
if prize in s:
    print("pizza is:",s[prize])
elif cake not in s:
    print("sorry pizza is not available")
else:
    print("Enter correct input")

'''


#multiple if
'''
#comparison
a=5
b=10
if a<b:
    print("a is less")
if b>a:
    print("b is greater")
if a!=b:
    print("a and b not equal")

print("\n")

a=5
b=10
if a==b:
    print("a is equal")
if b>a:
    print("b is greater")
if a!=b:
    print("a and b not equal")
'''

#logical
'''
a=5
b=50
if a>b and b<a:
    print("greater")
if a<b and b>a:
    print("less")
if a>b or b<a:
    print("b is less")
if not a>b or b<a:
    print("a is less")


#identify
a=20
b="python"
if type(a) is int:
    print("a is int")
if type(a) is not str:
    print("a is not str")
if type(b) is str:
    print("b is str")
if type(b) is not int:
    print("b is not int")
'''

#membership
'''
a = 20
b = "python"

if "2" in str(a):
    print("2 is in a")

if "5" not in str(a):
    print("5 is not in a")

if "p" in b:
    print("p is in b")

if "z" not in b:
    print("z is not in b")

'''

#tasks
'''
#1.
age >= 18, eligible for scholarship
marks>=80, eligible for placement
attendence>=90, allowed to write exams


age=int(input("Enter the age:"))
marks = int(input("Enter the marks"))
attendence = int(input("Enter the attendence"))
if age>= 18:
    print("Eligible for scholarship")
else:
    print("not Eligible for scholarship")


if marks>=80:
    print("Eligible for placements")
else:
    print("Not Eligible for placemnet")


if attendence >=90:
    print("Allowed to write exams")
else:
    print("not allowed to write exams")

'''

# 2.positive and negative, zero
'''
num = int(input("Enter the number:"))
if num>0:
    print("positive number")
if num<0:
    print("Negative number")
if num==0:
    print("the number is zero")

# num = int(input("Enter the number:"))
# if num>0:
#     print("positive number")
# elif num<0:
#     print("Negative number")
# elif num==0:
#     print("the number is zero")
# else:
#     print("Enter correct input")
'''

#3. marks >=35, pass
# if marsk >= 75, first class
#if marks >= 60, second class
#if marks >= 90, distinction

'''
marks =  int(input("Enter the marks:"))
if marks>=90:
    print("Distinction")
if marks>=60 and marks<90:
    print("first class")
if marks>=35 and marks<60:
    print("pass and second class")
'''


