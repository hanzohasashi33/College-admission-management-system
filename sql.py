import sqlite3

conn=sqlite3.connect('database.db')

conn.execute('CREATE TABLE STUDENTS(name varchar(255),father varchar(255),num INTEGER,email varchar(255),rank INTEGER,telephone INTEGER,dorm TEXT)')


conn.close()
prasanna
