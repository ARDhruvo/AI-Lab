# Main

f1 = open("students.txt", "w")
n = int(input("Enter number of students: "))
students = []
for i in range(n):
    name = input("\nEnter name: ")
    dept = input("Enter the department: ")
    cgpa = input("Enter the cgpa: ")
    stud = name + "\t" + dept + "\t" + cgpa
    students.append(stud + "\n")
    print(stud, end="\n", file=f1)
f1.close()

print("\nStudent records:")
f1 = open("students.txt", "r")
index = 1
for line in f1:
    print("Student Index: ", index)
    name, dept, cgpa = line.split("\t")
    print("Name:", name)
    print("Department:", dept)
    print("CGPA:", cgpa)
f1.close()

f1 = open("students.txt", "w")
n = int(input("Enter number of edits: "))
for i in range(n):
    edit_index = int(input("\nEnter the index of student to edit: "))
    if 1 <= edit_index <= len(students):
        name, dept, cgpa = students[edit_index - 1].split("\t")
        cgpa = input("Enter new cgpa: ")
        students[edit_index - 1] = name + "\t" + dept + "\t" + cgpa + "\n"
    else:
        print("Invalid index.")

for student in students:
    f1.write(student)
f1.close()

print("\nUpdated student records:")
f1 = open("students.txt", "r")
for line in f1:
    name, dept, cgpa = line.split("\t")
    print("Name:", name)
    print("Department:", dept)
    print("CGPA:", cgpa)
f1.close()
