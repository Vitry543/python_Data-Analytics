# Attendence tracker
'''
no. of students ->3
stud1 -> p
stud2->a
stud3->p

output:
total student = 5
no. of presenties -> 2
no. of absenties -> 2
'''

total_students = int(input("Enter the number of students"))

presenties = 0
absenties = 0


for i in range(1, total_students+1):
    status = input(f"student {i} (P/A):").lower()
    if status == "p":
        presenties+=1
    elif status == "a":
        absenties+=1
    else:
        print("invalid input!")

print("----------Attendence report----------")
print("Total Students:", total_students)
print("Total present students: ", presenties)
print("Total absent students: ", absenties)