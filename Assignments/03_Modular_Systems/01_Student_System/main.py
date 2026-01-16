# Main

f1 = open("students.txt", "w")
n = int(input("Enter number of students: "))
for i in range(n):
    name = input("Enter name: ")
    dept = input("Enter the department: ")
    cgpa = input("Enter the cgpa: ")
    stud = name + "\t" + dept + "\t" + cgpa
    print(stud, end="\n", file=f1)
f1.close()

f1 = open("students.txt", "r")
for line in f1:
    name, dept, cgpa = line.split("\t")
    print("Name:", name)
    print("Department:", dept)
    print("CGPA:", cgpa)
f1.close()
