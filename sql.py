from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
## Configure Genai Key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function To Load Google Gemini Model and provide queries as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

## Function To retrieve query from the database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
prompt=[
    """
    You excel at transforming English inquiries into SQL queries tailored for the university_data.db database!
    \n
    The university_data database includes three tables: Students, Courses, and Enrollments, each with specific columns:
    \n
    1. Students Table:
    - StudentID (Primary Key)
    - Name
    - Age
    - Gender
    - Email
    \n
    2. Courses Table:
    - CourseID (Primary Key)
    - Title
    - Instructor
    - Credits
    \n
    3. Enrollments Table:
    - EnrollmentID (Primary Key)
    - StudentID (Foreign Key referencing Students table)
    - CourseID (Foreign Key referencing Courses table)
    - Grade
    \n
    Here's how you can utilize your SQL expertise:
    \n
    Example Inquiry 1:
    Question: How many students are currently enrolled in the university?
    SQL query: SELECT COUNT(*) FROM Students;
    \n
    Example Inquiry 2:
    Question: Provide a list of all courses offered by the university along with their respective instructors.
    SQL query: SELECT Title, Instructor FROM Courses;
    \n
    Example Inquiry 3:
    Question: Display the names of students who are enrolled in both Computer Science and Mathematics courses.
    SQL query: SELECT s.Name 
            FROM Students s
            JOIN Enrollments e ON s.StudentID = e.StudentID
            JOIN Courses c ON e.CourseID = c.CourseID
            WHERE c.Title IN ('Computer Science', 'Mathematics')
            GROUP BY s.StudentID
            HAVING COUNT(DISTINCT c.CourseID) = 2;
    \n
    Example Inquiry 4:
    Question: Calculate the average age of male students enrolled in Biology courses.
    SQL query: SELECT AVG(s.Age) AS AverageAge
            FROM Students s
            JOIN Enrollments e ON s.StudentID = e.StudentID
            JOIN Courses c ON e.CourseID = c.CourseID
            WHERE s.Gender = 'Male' AND c.Title = 'Biology';
    \n
    Important Note: ALso the sql code should not have ``` in beginning or end and sql word in output

    """


]

## Streamlit App

st.set_page_config(page_title="Gemini App for Text to SQL and retreval")
st.header("I am a Gemini App that can talk to your database. Let me know what information you want. I'll get it from the database. No more writing complex SQL queries.")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"university_data1.db")
    st.subheader("The Response is")
    for row in response:
        print(row)
        st.header(row)