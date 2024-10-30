from Course import Course
from Student import Student

students = {}
courses = {}
allowed_grades = ("F", "D-", "D", "D+", "C-", "C", "C+", "B-", "B", "B+", "A-", "A", "A+")

def student_id_input():
    student_id = input("Enter Student ID: ")
    if len(student_id) == 0:
        print("Student ID is required!")
        student_id = input("Enter Student ID: ")
    return  student_id

def course_code_input():
    course_code = input("Enter Course Code: ")

    if len(course_code) == 0:
        print("Course Code is required")
        course_code = input("Enter Course Code: ")
    return course_code

def add_student():
    global students
    name = input("Enter Name: ")

    if len(name) == 0:
        print("Name is required!")
        name = input("Enter Name: ")


    try:
        age = int(input("Enter Age: "))
    except ValueError:
        print("Please input numeric value")
        age = int(input("Enter Age: "))
    except:
        print("Something wrong in age value, please try again!")
        age = int(input("Enter Age: "))

    address = input("Enter Address: ")

    student_id = student_id_input()
    if student_id in students:
        print(f"Student ID '{student_id}' already exists with the name '{name}'!")
    else:
        student = Student(name, age, address, student_id)
        students[student_id] = student
        print(f"Student {name} (ID: {student_id}) added successfully.")

def add_course():
    course_name = input("Enter Course Name: ")

    if len(course_name) == 0:
        print("Course Name is required!")
        course_name = input("Enter Course Name: ")

    course_code = course_code_input()

    course_instructor = input("Enter Instructor Name: ")

    if len(course_instructor) == 0:
        print("Instructor Name is required!")
        course_instructor = input("Enter Instructor Name: ")

    if course_code in courses:
        print(f"Course with the code '{course_code}' already exists!")
    else:
        course = Course(course_name, course_code, course_instructor)
        courses[course_code] = course
        print(f"Course {course_name} (Code: {course_code}) created with instructor {course_instructor}.")

def enroll_student_in_course():
    student_id = student_id_input()
    course_code = course_code_input()

    if student_id not in students and course_code not in courses:
        print("Invalid Student ID")
        print("Invalid Course Code")
    elif student_id not in students:
        print("Invalid Student ID")
    elif course_code not in courses:
        print("Invalid Course Code")
    else:
        student = students[student_id]
        course = courses[course_code]
        student.enroll_course(course)
        course.add_student(student)


def add_grade_for_student():
    student_id = student_id_input()
    course_code = course_code_input()
    print(f"Allowed Grades: ({allowed_grades})")
    grade = input("Enter Grade: ")
    if len(grade) == 0:
        print("Grade is required!")
        grade = input("Enter Grade: ")
    elif grade not in allowed_grades:
        print("Invalid Grade, try again")
        grade = input("Enter Grade: ")

    if student_id not in students and course_code not in courses:
        print("Invalid Student ID")
        print("Invalid Course Code")
    elif student_id not in students:
        print("Invalid Student ID")
    elif course_code not in courses:
        print("Invalid Course Code")
    else:
        student = students[student_id]
        course = courses[course_code]
        if course in student.courses:
            student.add_grade(course.course_name, grade)
        else:
            print(f"Student did not enroll for the subject {course.course_name}")

def display_student_details():
    student_id = student_id_input()
    if student_id not in students:
        print(f"No student found for the Student ID:{student_id}")
    else:
        student = students[student_id]
        student.display_student_info()

def display_course_details():
    course_code = course_code_input()

    if course_code not in courses:
        print(f"No Course found for the Course Code:{course_code}")
    else:
        course = courses[course_code]
        course.display_course_info()

# def save_data_to_file():
#
# def load_data_from_file()



def run():
    while True:
        print("\n==== Student Management System ====")
        print("1. Add New Student")
        print("2. Add New Course")
        print("3. Enroll Student in Course")
        print("4. Add Grade for Student")
        print("5. Display Student Details")
        print("6. Display Course Details")
        print("7. Save Data to File")
        print("8. Load Data from File")
        print("0. Exit")

        # Taking operation option
        try:
            choice = int(input("Select Option: "))
        except ValueError:
            choice = None
            print("Please input numeric value")
        except:
            choice = None
            print("There was an error, please try again!")

        # Running operation according to the selected option
        if choice == 1:
            add_student()
        elif choice == 2:
            add_course()
        elif choice == 3:
            enroll_student_in_course()
        elif choice == 4:
            add_grade_for_student()
        elif choice == 5:
            display_student_details()
        elif choice == 0:
            print("Exiting Student Management System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

run()

