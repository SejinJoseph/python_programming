import sqlite3

try:
    connection = sqlite3.connect("stejin_db.db")
    cursor = connection.cursor()
    creat_table_query = """
        CREATE TABLE student(
        rollno INTEGER PRIMARY KEY AUTOINCREMENT,
        name varchar(40),
        email varchar(40),
        course varchar(10),
        cgpa varchar(10,2))
        """
    cursor.execute(creat_table_query)
    print("Table created successfully")
except sqlite3.Error as error:
    print(error)
finally:
    cursor.close()
    connection.close()