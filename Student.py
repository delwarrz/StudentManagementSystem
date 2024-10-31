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
            self.courses.append(course)

    def display_student_info(self):
        print(" ")
        print(" ")
        print("======== Course Information ============")
        self.display_person_info()
        print(f"ID: {self.student_id}")


        print("Enrolled Courses: ", end = " ")
        if len(self.courses) > 0:
            print(', '.join(self.courses))
        else:
            print("None")

        print("Grades:")
        if self.grades:
            for subject, grade in self.grades.items():
                print(f"  {subject}: {grade}")
        else:
            print("  No grades available.")

        print("================================")
        print(" ")


