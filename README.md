# Student Management System

A CLI-based **Student Management System** implemented in Python using Object-Oriented Programming (OOP) principles. This system allows for managing student records, course enrollments, and grade assignments. The project supports file-based storage using JSON to persist data between sessions.
It is developed as assignment of the **Ostad** Platform Python Course "**Full Stack Web Development with Python, Django & React**"

## Features

- **Add New Students**: Create and store student profiles with personal information like name, age, and address.
- **Manage Courses**: Add new courses with details like course name, course code, and instructor.
- **Enroll Students in Courses**: Enroll students in their desired courses and track their participation.
- **Assign and Update Grades**: Add or modify student grades for specific courses.
- **View Details**: Display detailed information about students, including their enrolled courses and grades, and course information with enrolled students.
- **File Operations**: Save and load all student and course data to/from a JSON file, enabling persistent data storage.

## System Functionalities

1. **Add Student**: Add a new student with a unique ID.
2. **Enroll in Course**: Enroll a student in a course by their ID and course code.
3. **Assign Grades**: Add or update the grade of a student for a specific course.
4. **Display Student and Course Details**: View details about any student or course.
5. **Save/Load Data**: Save the current session data to a file or load it from a saved file.
6. **Menu-Driven CLI**: Interact with the system through a user-friendly command-line interface.

## How to Use

Clone the repository and run the `main.py` script. The menu will guide you through adding students, courses, enrolling in courses, assigning grades, and managing data.

## Requirements
- **Python 3.x**

```bash
git clone https://github.com/your-username/student-management-system.git
cd student-management-system
python main.py