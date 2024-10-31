import json

from Course import Course
from Student import Student

students = []
courses = []
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
    if any(student.student_id == student_id for student in students):
        print(f"Student ID '{student_id}' already exists with the name '{next(student.name for student in students if student.student_id == student_id)}'!")
    else:
        student = Student(name, age, address, student_id)
        students.append(student)
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

    if any(course.course_code for course in courses):
        print(f"Course with the code '{course_code}' already exists!")
    else:
        course = Course(course_name, course_code, course_instructor)
        courses.append(course)
        print(f"Course {course_name} (Code: {course_code}) created with instructor {course_instructor}.")

def enroll_student_in_course():
    student_id = student_id_input()
    course_code = course_code_input()

    if any(student.student_id == student_id for student in students) and any(course.course_code for course in courses):
        student = next(student for student in students if student.student_id == student_id)
        course = next(course for course in courses if course.course_code == course_code)
        if course not in student.courses:
            student.enroll_course(course.course_name)
            course.add_student(student.name)
            print(f"Student {student.name} (ID: {student.student_id}) enrolled in {course.course_name} (Code: {course.course_code})")
        else:
            print(f"Student {student.name} (ID: {student.student_id}) already enrolled in {course.course_name} (Code: {course.course_code})")

    elif any(student.student_id == student_id for student in students):
        print("Invalid Course Code")
    elif any(course.course_code for course in courses):
        print("Invalid Student ID")
    else:
        print("Invalid Student ID")
        print("Invalid Course Code")



def add_grade_for_student():
    student_id = student_id_input()
    course_code = course_code_input()
    print(f"Allowed Grades: {allowed_grades}")
    grade = input("Enter Grade: ")
    if len(grade) == 0:
        print("Grade is required!")
        grade = input("Enter Grade: ")
    elif grade not in allowed_grades:
        print("Invalid Grade, try again")
        grade = input("Enter Grade: ")

    if any(student.student_id == student_id for student in students) is False and any(course.course_code == course_code for course in courses) is False:
        print("Invalid Student ID")
        print("Invalid Course Code")
    elif any(student.student_id == student_id for student in students) is False:
        print("Invalid Student ID")
    elif any(course.course_code == course_code for course in courses) is False:
        print("Invalid Course Code")
    else:
        student = next(student for student in students if student.student_id == student_id)
        course = next(course for course in courses if course.course_code == course_code)
        if course.course_name in student.courses:
            student.add_grade(course.course_name, grade)
        else:
            print(f"Student did not enroll for the subject {course.course_name}")

def display_student_details():
    student_id = student_id_input()
    if any(student.student_id == student_id for student in students) is False:
        print(f"No student found for the Student ID:{student_id}")
    else:
        student = next(student for student in students if student.student_id == student_id)
        student.display_student_info()

def display_course_details():
    course_code = course_code_input()

    if any(course.course_code == course_code for course in courses) is False:
        print(f"No Course found for the Course Code:{course_code}")
    else:
        course = next(course for course in courses if course.course_code == course_code)
        course.display_course_info()

def save_data_to_file():
     try:
         students_object = []
         courses_object = []

         for student in students:
             students_object.append(student.__dict__)


         with open("students.json", "w") as studentFile:
             json.dump(students_object, studentFile, indent=4)

         for course in courses:
             courses_object.append(course.__dict__)


         with open("courses.json", "w") as coursesFile:
             json.dump(courses_object, coursesFile, indent=4)

         print("All student and course data saved successfully.")
     except:
         print("There was error in saving data into the file")



def load_data_from_file():
    global students
    global courses

    try:
        with open('students.json', 'r') as studentsFile:
            students_object = json.load(studentsFile)
            students = []
            for std_obj in students_object:
                student = Student(std_obj['name'], std_obj['age'], std_obj['address'], std_obj['student_id'])

                if len(std_obj['courses']) > 0:
                    for student_course in std_obj['courses']:
                        student.enroll_course(student_course)

                if len(std_obj['grades']) > 0:
                    for subject, grade in std_obj['grades'].items():
                        student.add_grade(subject, grade)

                students.append(student)

        with open('courses.json', 'r') as coursesFile:
            courses_object = json.load(coursesFile)

            courses = []
            for course_obj in courses_object:
                course = Course(course_obj['course_name'], course_obj['course_code'], course_obj['instructor'])

                if len(course_obj['students']) > 0:
                    for course_student in course_obj['students']:
                        course.add_student(course_student)

                courses.append(course)
        print("All student and course data loaded successfully.")
    except:
        print("There was an error in loading data from file!")



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
        elif choice == 6:
            display_course_details()
        elif choice == 7:
            save_data_to_file()
        elif choice == 8:
            load_data_from_file()
        elif choice == 0:
            print("Exiting Student Management System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

run()

