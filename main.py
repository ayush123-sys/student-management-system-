import json
students=[]
def add_student():
    roll = int(input("Enter roll number:"))
    name = input("Enter students name:")
    age = int(input("Enter age:"))
    m1=float(input("Enter marks for subject1:"))
    m2=float(input("Enter marks for subject 2:"))
    m3=float(input("Enter marks for subject 3 :"))
    total= m1+m2+m3
    percentage=total/3
    if percentage >=90:
        grade="A"
    elif percentage>=75:
        grade = "B"
    elif percentage >=60:
        grade = "C"
    else:
        grade = "D"
    student = {
        "roll":roll,
        "name": name,
        "age": age,
        "marks":[m1,m2,m3],
        "percentage":percentage,
        "grade":grade} 
    students.append(student)
    print("student added successfully") 
def view_student():
    if len(students)==0: 
        print("No students found")
        return 
    for student in students:
        print("Roll number:",student["roll"])
        print("name:", student["name"])
        print("age:",student["age"])
        print("marks:",student["marks"])
        print("percentage:",student["percentage"])
        print("grade:",student["grade"])
def search_student():
    roll =int(input("enter roll number to search:"))
    for student in students:
        if student["roll"]==roll:
            print("student found!")
            print("name:", student["name"])
            print("age:",student["age"])
            print("marks:",student["marks"])
            print("percentage:", student["percentage"])
            print("grade:", student["grade"])
            return
        print("student not found")
def delete_student():
    roll =int(input("enter roll number to delete:"))
    for student in students:
        if student["roll"]== roll:
            students.remove(student)
        print("student deleted!")
        return
def update_students():
    roll=int(input("enter roll number to update:"))
    for student in students:
        if student["roll"]==roll:
            student["name"]=input("enter students name")
            student["age"]=int(input("enter new age"))
        print("Student updated successfully")
        return
print("Student not found")
while True:
        print("\nStudent Management System")
        print("1.Add Student")
        print("2.View Students")
        print("3.Search Student")
        print("4.delete Student")
        print("5.update student")
        print("6.Exit")
        choice=input("enter your choice:")
        if choice=="1":
            add_student()
        elif choice=="2":
            view_student()
        elif choice=="3":
            search_student()
        elif choice=="4":
            delete_student()
        elif choice=="5":
            update_students()
        elif choice=="6":
            print("thank you")
            break