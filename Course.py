class Course:
    def __init__(self, course_name, course_code, instructor):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []

    def add_student(self, student):
            self.students.append(student)

    def display_course_info(self):
        print(" ")
        print(" ")
        print("======== Course Information ============")
        print(f"Course Name: {self.course_name}")
        print(f"Course Code: {self.course_code}")
        print(f"Instructor: {self.instructor}")
        print(f"Enrolled Students: {', '.join(self.students) if self.students else 'No students enrolled'}")
        print("================================")
        print(" ")