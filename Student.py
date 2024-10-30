from Person import Person


class Student(Person):
    def __init__(self, name, age, address, student_id):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.grades = {}
        self.courses = []

    def add_grade(self, subject, grade):
        self.grades[subject] = grade
        print(f"{grade} added for {self.name} in {subject}")

    def enroll_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            print(f"Student {self.name} (ID: {self.student_id}) enrolled in {course.course_name} (Code: {course.course_code})")
        else:
            print(f"Student {self.name} (ID: {self.student_id}) already enrolled in {course.course_name} (Code: {course.course_code})")

    def display_student_info(self):
        self.display_person_info()
        print(f"ID: {self.student_id}")


        print("Enrolled Courses: ", end = " ")
        if len(self.courses) > 0:
            for index, course in enumerate(self.courses):
                if index != (len(self.courses) - 1):
                    print(course.course_name, ",", end=" ")
                else:
                    print(course.course_name)
        else:
            print("None")

        print("Grades:")
        if self.grades:
            for subject, grade in self.grades.items():
                print(f"  {subject}: {grade}")
        else:
            print("  No grades available.")

