import sqlite3

##Connect to SQLite
connection = sqlite3.connect("student.db")

##Create a cursor object to insert record,create table

cursor = connection.cursor()

##Create a table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25));

"""
cursor.execute(table_info)

#Insert some records

cursor.execute('''Insert Into STUDENT values('Aya','Mahine Learning','A')''')
cursor.execute('''Insert Into STUDENT values('Reem','Biomedical Eng','B')''')
cursor.execute('''Insert Into STUDENT values('Hasan','Medicine','C')''')
cursor.execute('''Insert Into STUDENT values('Reine','Biology ','D')''')
cursor.execute('''Insert Into STUDENT values('Fatouma','Mahine Learning','A')''')

##Display all the results
print("The inserted records are")
data = cursor.execute('''Select * from  STUDENT''')
for row in data:
    print(row)