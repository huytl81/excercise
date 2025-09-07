import sqlite3

conn = sqlite3.connect("example.db")

with conn:
    cursor = conn.cursor()

    ## create table
    # create table
    # cursor.execute("""
    #     CREATE TABLE IF NOT EXISTS Student(
    #         ID INTEGER PRIMARY KEY AUTOINCREMENT,
    #         Name TEXT NOT NULL,
    #         Age INTEGER,
    #         Grade TEXT
    #     )
    # """)

    ## insert 1 row
    # cursor.execute("""
    #     INSERT INTO Student(Name,Age,Grade)
    #     VALUES('Nguyen Van A', 20, 'A')
    # """)

    ## insert nhieu row thi dung .executemany
    # my_data = [("Sen Thoi", 14, "A"), ("Nam", 21, "B"), ("Duc", 22, "C")]
    # cursor.executemany("""
    # INSERT INTO Student(Name,Age,Grade)
    # VALUES(?,?,?)
    # """, my_data)

    # update
    # cursor.execute("""
    # UPDATE Student
    # SET Name = "Dao"
    # WHERE Name = "Duc"
    # """)

    # delete
    # cursor.execute("""
    # DELETE FROM Student
    # WHERE Name = "Nam"
    # """)

    conn.commit()

    # fetch all row - khong can commit
    # cursor.execute("SELECT name, age FROM Student WHERE Age > 20")
    # rows = cursor.fetchall()
    # print(rows)

    conn.close()