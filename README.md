## Student Enrollment System
This Python script demonstrates a simple student enrollment system using an SQLite database. The script allows you to register new students, add courses, and enroll students in courses.

## Getting Started
## Prerequisites
Python 3.x installed on your system
SQLite3 library (usually included with Python installations)
Installation
Clone or download the repository to your local machine.

bash
Copy code
git clone https://github.com/your-username/student-enrollment.git
Navigate to the project directory.

bash
Copy code
cd student-enrollment
Install any required dependencies.

bash
Copy code
pip install -r requirements.txt
Usage
Run the Python script to interact with the student enrollment system.

bash
Copy code
python student_enrollment.py
Follow the prompts to register new students, add courses, and enroll students in courses.

## Features
1.Register Students: Add new students with their personal information.
2.Add Courses: Create new courses with details like course name, instructor, credits, and semester.
3.Enroll Students: Enroll students in courses they want to take.
4.Database Structure

## The SQLite database contains three tables:

Students: Stores student information (student ID, first name, last name, date of birth, email, phone number).
Courses: Stores course information (course ID, course name, instructor, credits, semester).
Enrollments: Tracks student enrollments in courses (enrollment ID, student ID, course ID, enrollment date).
Contributing
Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
Special thanks to the SQLite development team for providing the SQLite database library.

