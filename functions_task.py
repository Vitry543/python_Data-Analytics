# 1)Define a function that can accept two strings as input and print the string with maximum length in the console. If two strings have the same length, then the function should print all strings line by line.

def cond():
    a=input()
    b=input()
    if len(a)>len(b):
        print(a)
    elif len(a)==len(b):
        print(a)
        print(b)
    else:
        print(b)
cond()


#  2)Define a function which can print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are squares of keys.

def square():
    n = int(input())
    a={}
    for i in range(1,n+1):
        a[i] = i**2
    return a
print(square())


# 3)Define a function which can generate a list where the values are squares of numbers between 1 and 15 (both included). Then the function needs to print the first 5 and last 5 elements in the list.

def square():
    n = int(input())
    l=[]
    for i in range(1, n+1):
        l.append(i**2)
    print(l[:5])
    print(l[-5:])
square()

def square():
    l = [i**2 for i in range(1, 16)]
    print(l[:5])
    print(l[-5:])

square()

# 4)Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0). Suppose If the following n is given as input to the program:5 Then, the output of the program should be: 3.55

def compute():
    n = int(input())
    sum=0
    for i in range(1, n+1):
        op = i/(i+1)
        sum+=op
    print(f"{sum:.2f}")
compute()

#  5)Write a Function to generate all sentences where the subject is in ["I", "You"] and the verb is in ["Play", "Love"] and the sport is in ["Hockey", "Cricket"].
def sentences():
    subject = ["I", "You"]
    verb = ["Play", "Love"]
    sport = ["Hockey", "Cricket"]

    for i in subject:
        for j in verb:
            for k in sport:
                print(i, j, k)

sentences()


# 6)With a given list [12,24,35,24,88,120,155,88,120,155], write a Function to print this list after removing all duplicate values with original order reserved. 

'''def org():
    l=[12,24,35,24,88,120,155,88,120,155]
    s=set(l)
    l=sorted(list(s))
    print(l)
org()'''

def org():
    l = [12,24,35,24,88,120,155,88,120,155]
    a = []

    for i in l:
        if i not in a:
            a.append(i)

    print(a)

org()


# 7)Write a Function that accepts a string from the user and gives the output of vowels in a given string as list along with the length of the list? 

def vowels():
    s=input()
    l=[]
    
    for i in s:
        if i in "aeiou" or i in "AEIOU":
            l.append(i)
    print(l)
    print(len(l))
vowels()


# 8)Create a Function which includes your name,age,designation and years of Experience,and assign a different name to the function and call it through the new name?

def details():
    name = input()
    age = int(input())
    designation = input()
    exp = int(input())

    print("Name:", name)
    print("Age:", age)
    print("Designation:", designation)
    print("Experience:", exp, "years")

new = details
new()



#  9)Write a function for checking the speed of drivers. This function should have one parameter: speed. -->If speed is less than 70, it should print "Riding Well". -->Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. For example, if the speed is 80, it should print: "Points: 2". -->If the driver gets more than 10 points, the function should print: "License suspended"

def speed_check(speed):
    points = 0
    if speed <=70:
        print("Riding well")
    elif speed >70:
        speed = speed - 70
        points += speed // 5
        print(f"Points:{points}")
    if points > 10:
        print("Lincense Suspended")
speed_check(int(input()))


# 10)Write a function that returns the sum of multiples of 3 and 5 between 0 and given limit. For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20

def multiple(n):
    total = 0
    for i in range(1,n+1):
        if i%3==0 or i%5==0:
            # print(i, end=" ")
            total+=i
    # print()
    # print(total)
    return total
# multiple(int(input()))
print(multiple(int(input())))


# 11)Write a function that accepts roll number and returns whether the student is present or absent? Hint : Use list to store the roll number of the Student 

'''# def attendance(n):
#     attendances = [101, 102, 104, 106, 108]

#     if n in attendances:
#         return "Present"
#     else:
#         return "Absent"

# print(attendance(int(input("Enter roll number: "))))

def attendance(n):
    attendances = []

    for i in range(1, n+1):
        a = input(f"Enter student {i} P/A: ").lower()

        if a == "p":
            attendances.append(i)
            
    print(attendances)
    roll = int(input("Enter roll number to check: "))

    if roll in attendances:
        print("Present")
    else:
        print("Absent")

attendance(int(input("Enter number of students: ")))'''

def attendance(n):
    attendances = [101, 102, 104, 106, 108]

    for i in attendances:
        if i == n:
            print("Present")
            break
    else:
        print("Absent")

attendance(int(input("Enter roll number: ")))


# 12)Write a Function which counts vowels and consonants in the given string, accept string from the user?
'''def alphas():
    vowels = 0
    const=0
    s = input().lower()
    for i in s:
        if i in "aeiou":
            vowels+=1
        else:
            const+=1
    print("Vowels", vowels)
    print("consonants:", const)

alphas()'''

def alphas():
    vowels = 0
    const = 0
    s = input().lower()

    for i in s:
        if i in "aeiou":
            vowels += 1
        elif i.isalpha():
            const += 1

    print("Vowels:", vowels)
    print("Consonants:", const)

alphas()


# 13)Write a Python Function to generate the sum of squares of even numbers by accepting input from the user?

'''def even_square(n):
    total=0
    for i in range(n+1):
        if i%2==0:
            total+= i**2
    print(total)
even_square(int(input()))

def even_square(n):
    print(sum(i**2 for i in range(2, n+1, 2)))

even_square(int(input()))'''

