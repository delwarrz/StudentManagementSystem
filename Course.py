class Course:
    def __init__(self, course_name, course_code, instructor):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            print(f"{student.name} added to {self.course_name}.")
        else:
            print(f"{student.name} is already enrolled in {self.course_name}.")

    def display_course_info(self):
        print("======== Course Information ============")
        print(f"Course Name: {self.course_name}")
        print(f"Course Code: {self.course_code}")
        print(f"Instructor: {self.instructor}")
        print(
            f"Enrolled Students: {', '.join([student.name for student in self.students]) if self.students else 'No students enrolled'}")