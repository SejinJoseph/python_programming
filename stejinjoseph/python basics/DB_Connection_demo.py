import sqlite3

try:
    connection=sqlite3.connect('stejin_db.db')
    cursor=connection.cursor()


    cursor.execute("SELECT * FROM student")
    print("student in the database:")
    for row in cursor.fetchall():
        print(row)

except sqlite3.Error as e:
    print(f"sqlite error: {e}")
finally:
    if connection:
        connection.close()