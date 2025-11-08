import sqlite3

try:
    connection=sqlite3.connect('stejin_db.db')
    cursor=connection.cursor()
    insert_data_query = """
        INSERT INTO student (name,email,course,cgroup) values (?,?,?,?)
        """
    student_data=("loid","loid@gmail.com","spy","10")
    cursor.execute(insert_data_query,student_data)
    connection.commit
    print("student added to database successfully")
except sqlite3.Error as error:
    print(error)
finally:
    cursor.close()
    connection.close()