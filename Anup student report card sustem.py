student_list = []

# works out the grade based on percentage
def get_grade(percent):
    if percent >= 90:
        return "A"
    elif percent >= 75:
        return "B"
    elif percent >= 60:
        return "C"
    elif percent >= 40:
        return "D"
    else:
        return "F"

# adds a new student to the list
def add_student():
    name = input("Enter student name: ")
    cgma = int(input("Computer Graphics & Multimedia marks: "))
    os_marks = int(input("Operating System marks: "))
    se = int(input("Software Engineering marks: "))
    ot = int(input("Optimization Techniques marks: "))
    maths3 = int(input("Mathematics 3 marks: "))

    # tuple bcz marks shouldn't change once entered
    marks = (cgma, os_marks, se, ot, maths3)

    total_marks = sum(marks)
    max_possible = len(marks) * 100
    percent = round(total_marks / max_possible * 100, 2)
    grade = get_grade(percent)

    print("Total marks:", total_marks)
    print("Percentage:", percent, "%")
    print("Grade:", grade)

    new_student = {
        "name": name,
        "marks": marks,
        "total": total_marks,
        "percent": percent,
        "grade": grade
    }

    student_list.append(new_student)
    print("Added!")


# shows every student one by one
def show_all():
    if len(student_list) == 0:
        print("List is empty, add someone first")
        return

    for stu in student_list:
        print("---------------------")
        print("Name:", stu["name"])
        print("Computer Graphics & Multimedia:", stu["marks"][0])
        print("Operating System:", stu["marks"][1])
        print("Software Engineering:", stu["marks"][2])
        print("Optimization Techniques:", stu["marks"][3])
        print("Mathematics 3:", stu["marks"][4])
        print("Total:", stu["total"])
        print("Percent:", stu["percent"], "%")
        print("Grade:", stu["grade"])


# looks for one student by name
def find_student():
    search_name = input("Name to search: ")
    match = None

    for stu in student_list:
        if stu["name"] == search_name:
            match = stu
            break

    if match == None:
        print("Not found")
    else:
        print("Found -")
        print("Name:", match["name"])
        print("Computer Graphics & Multimedia:", match["marks"][0])
        print("Operating System:", match["marks"][1])
        print("Software Engineering:", match["marks"][2])
        print("Optimization Techniques:", match["marks"][3])
        print("Mathematics 3:", match["marks"][4])
        print("Total:", match["total"])
        print("Percent:", match["percent"], "%")
        print("Grade:", match["grade"])


# figures out who scored the highest
def get_topper():
    if len(student_list) == 0:
        print("List is empty, add someone first")
        return

    best = student_list[0]
    for stu in student_list:
        if stu["percent"] > best["percent"]:
            best = stu

    print("Topper is:", best["name"])
    print("Computer Graphics & Multimedia:", best["marks"][0])
    print("Operating System:", best["marks"][1])
    print("Software Engineering:", best["marks"][2])
    print("Optimization Techniques:", best["marks"][3])
    print("Mathematics 3:", best["marks"][4])
    print("Total:", best["total"])
    print("Percent:", best["percent"], "%")
    print("Grade:", best["grade"])


# menu loop
while True:
    print("\n1. Add student")
    print("2. Show all")
    print("3. Find student")
    print("4. Topper")
    print("5. Quit")

    option = int(input("Choice: "))

    if option == 1:
        add_student()
    elif option == 2:
        show_all()
    elif option == 3:
        find_student()
    elif option == 4:
        get_topper()
    elif option == 5:
        print("Bye")
        break
    else:
        print("Invalid choice, pick between 1 and 5")
