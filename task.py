# Student profile
'''
student_name = input("Enter your name: ")
id = input("Enter your ID: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender: ")
mailid = input("Enter your mail ID: ")
mobileno = int(input("Enter the mobile number:"))

college = input("Enter your college name: ")
branch = input("Enter your branch: ")


print("Student Profile")
print("Name:",student_name)
print("ID:",id)
print("Age:",age)
print("Gender:",gender)
print("mailid:",mailid)
print("mobileno:",mobileno)
print("College:",college)
print("branch:",branch)

'''

"""student_profile = {
    "Name": student_name,
    "ID": id,
    "Age": age,
    "Gender": gender,
    "Mail ID": mailid,
    "Mobile Number": mobileno,
    "College": college,
    "Branch": branch
}
"""

'''
#firstname+lastname = fullname(format method $ fstring)
fname = input("Enter your First name:")
lname = input("Enter your Last name:")
fullname = (fname+" "+lname).title()
print("Full Name is {}".format(fullname))
print(f"Full Name is {fullname}")
'''

'''
a="listen"
#silent

#first method
b=a.replace("listen","silent")
print(b)

#second method
b=a[2]+a[1]+a[0]+a[4]+a[5]+a[3]
print(b)

#third method
b=a[:3]
c=a[3:]
print(b)
print(c)


b=b[::-1]
print(b)
c=c.replace("ten","ent")
print(c)
print(b+c)
'''

a=["i","am","working","in","codegnan"]
#["i am working in codegnan"]

# " ".join(a)
print(" ".join(a))

