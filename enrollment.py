import sqlite3

# Connect to the SQLite database or create it if it doesn't exist
conn = sqlite3.connect('student_enrollment.db')
cursor = conn.cursor()

# Create the Students, Courses, and Enrollments tables if they don't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Students (
        student_id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        date_of_birth TEXT,
        email TEXT,
        phone_number TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Courses (
        course_id INTEGER PRIMARY KEY,
        course_name TEXT NOT NULL,
        instructor TEXT,
        credits INTEGER,
        semester TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Enrollments (
        enrollment_id INTEGER PRIMARY KEY,
        student_id INTEGER,
        course_id INTEGER,
        enrollment_date TEXT,
        FOREIGN KEY (student_id) REFERENCES Students(student_id),
        FOREIGN KEY (course_id) REFERENCES Courses(course_id)
    )
''')

# Function to register a new student
def register_student(first_name, last_name, date_of_birth, email, phone_number):
    cursor.execute('''
        INSERT INTO Students (first_name, last_name, date_of_birth, email, phone_number)
        VALUES (?, ?, ?, ?, ?)
    ''', (first_name, last_name, date_of_birth, email, phone_number))
    conn.commit()
    return "Student registered successfully!"

# Function to add a new course
def add_course(course_name, instructor, credits, semester):
    cursor.execute('''
        INSERT INTO Courses (course_name, instructor, credits, semester)
        VALUES (?, ?, ?, ?)
    ''', (course_name, instructor, credits, semester))
    conn.commit()
    return "Course added successfully!"

# Function to enroll a student in a course
def enroll_student(student_id, course_id, enrollment_date):
    cursor.execute('''
        INSERT INTO Enrollments (student_id, course_id, enrollment_date)
        VALUES (?, ?, ?)
    ''', (student_id, course_id, enrollment_date))
    conn.commit()
    return "Student enrolled in the course!"

# Sample usage of the functions
registration_message = register_student("John", "Doe", "2000-01-01", "john.doe@email.com", "123-456-7890")
course_message = add_course("Introduction to Python", "Dr. Smith", 3, "Spring 2024")
enrollment_message = enroll_student(1, 1, "2024-03-18")

# Close the database connection
conn.close()

# Print the messages
print(registration_message)
print(course_message)
print(enrollment_message)
