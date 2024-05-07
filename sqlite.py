import sqlite3

## Connect to SQlite
#connection=sqlite3.connect("student.db")
connection=sqlite3.connect("university_data1.db") 

# Create a cursor object to insert  record, create table

cursor=connection.cursor()

## Create the table
# table_info="""
# Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
# SECTION VARCHAR(25),MARKS INT);

# """

## Create the table
table_info="""
CREATE TABLE Students (
    StudentID INTEGER PRIMARY KEY,
    Name TEXT,
    Age INTEGER,
    Gender TEXT,
    Email TEXT
);

"""
cursor.execute(table_info)

table_info="""
CREATE TABLE Courses (
    CourseID INTEGER PRIMARY KEY,
    Title TEXT,
    Instructor TEXT,
    Credits INTEGER
);
"""
cursor.execute(table_info)

table_info="""
CREATE TABLE Enrollments (
    EnrollmentID INTEGER PRIMARY KEY,
    StudentID INTEGER,
    CourseID INTEGER,
    Grade TEXT,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);
"""

cursor.execute(table_info)



## Insert Some more records


cursor.execute('''
    INSERT INTO Students (Name, Age, Gender, Email) VALUES
    ('Alice', 20, 'Female', 'alice@example.com'),
    ('Bob', 22, 'Male', 'bob@example.com'),
    ('Charlie', 21, 'Male', 'charlie@example.com'),
    ('Diana', 23, 'Female', 'diana@example.com'),
    ('Emily', 19, 'Female', 'emily@example.com');
    ''')

cursor.execute('''
INSERT INTO Courses (Title, Instructor, Credits) VALUES
('Mathematics', 'Dr. Smith', 3),
('Computer Science', 'Prof. Johnson', 4),
('English', 'Prof. White', 3),
('History', 'Prof. Brown', 3),
('Biology', 'Dr. Green', 4);
    ''')

cursor.execute('''               
INSERT INTO Enrollments (StudentID, CourseID, Grade) VALUES
(1, 1, 'A'),
(2, 2, 'B'),
(3, 1, 'B'),
(4, 3, 'A'),
(5, 2, 'C'),
(1, 3, 'B'),
(2, 1, 'C'),
(3, 2, 'B'),
(4, 5, 'A'),
(5, 4, 'B');
    ''')

## Display ALl the records

print("The inserted records are")
data=cursor.execute('''Select * from Students''')
for row in data:
    print(row)

## Commit your changes in the database
connection.commit()
connection.close()
