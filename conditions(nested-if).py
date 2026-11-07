#nested if conditions
#nested if conditions are used when we have to check multiple conditions 
# and we want to execute a block of code only if all the conditions are true. 
# In this case, we can use nested if conditions to check if a is less than b and if b is greater than a.

'''
a=3
b=7
if a<b:
    print("less")
    if b>a:
        print("gretaer")
'''

'''
a=3
b=7
if a<b:
    print("less")
    if b<a:
        print("gretaer")
        '''
'''
a=3
b=7
if a==b:
    print("Equal")
    if b>a:
        print("greater")'''

'''
a=4
b=8
if a<b:
    print("less")
    if a>b:
        print("greater")
    else:
        print("true")


a=4
b=8
if b<a:
    print("less")
    if a>b:
        print("greater")
    else:
        print("True")
else:
    print("False")
 '''   

'''   
a=4
b=8
if b>a:
    print("less")
    if a>b:
        print("False")
    elif a<b:
        print("greater")
    else:
        print("True")
else:
    print("False")'''


#tasks
#social media login: 
#using nested if conditions
'''
username = input("enter the username:").lower()
password = int(input("Enter the password:"))
if username == "mani":
    if password == 3214:
        print("login successfully,Welcome Mani")
    else:
        print("wrong password")
else:
    print("invalid username")



#using if else conditions
username = input("enter the username:").lower()
password = int(input("Enter the password:"))
if username == "mani" and password==3214:
    print("Login Successfully")
else:
    print("Invalid Credentials")

username = input("enter the username:").lower()
password = input("Enter the password:")
if username == "mani" and password=="mani@3214":
    print("Login Successfully")
else:
    print("Invalid Credentials")

'''



