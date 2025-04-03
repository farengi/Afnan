from dotenv import load_dotenv
load_dotenv() ##load all the environment variables

import streamlit as st
import os
import sqlite3

from google.generativeai import genai
##Configure Genai Key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

##Function to load Google Gemini Model

def get_gemini_response(question,prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0],question])
    return response.text

##Function to retrieve query from the database
 
def read_sql_query(sql,db):
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    data = cur.execute("Select * FROM STUDENT")
    print(data)
    for row in data:
        print(row)

##Define your prompt
prompt = [
    """
    You are an expert in converting English questions to SQL code!
    The SQL database has the name STUDENT and has the following columns -Name, Class,
    SECTION \n\nFor example,\nExample 1 - How many enteries of records are present?,
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT;
    \nExample 2 - Tell me all students studying in Data Science class?,
    the SQL command will be something like this SELECT * FROM STUDENT where CLASS="Data Science";
    also the sql code should not have ``` in beginning or end and sql word in output

    """
]

## Streamlit App
st.set_page_config(page_title="I cam Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question= st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response = get_gemini_response(question,prompt)
    print(response)
    response = read_sql_query(response,"student.db")
    st.subheader("The Response is:")
    for row in response:
        print(row)
        st.header(row)
