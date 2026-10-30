# ==============================================================================
# Lab Sheet-08: Python Programming Lab – Database Management using Python Programming
# MCA I Semester (Session 2026-2027)
# COER University, Roorkee
# ==============================================================================

import csv
import os
import sqlite3

# Define common database name for all programs
DB_NAME = "student_db.db"


# ==============================================================================
# Q1: Write a Python program to connect to a MySQL (or SQLite) database and display a success message.
# ==============================================================================
# Q1_connect_to_database.py

print("\n--- Q1: Connect to Database ---")
conn = None
try:
    # Establishing connection to the SQLite database
    # (If MySQL is used: mysql.connector.connect(host="localhost", user="root", password="", database="student_db"))
    conn = sqlite3.connect(DB_NAME)
    print(f"Success: Connected successfully to the database '{DB_NAME}'.")
    print(f"SQLite Library Version: {sqlite3.version}")
except sqlite3.Error as err:
    print(f"Database Connection Error: {err}")
finally:
    # Always close the connection
    if conn:
        conn.close()
        print("Database connection closed.")


# ==============================================================================
# Q2: Write a program to create a new database.
# ==============================================================================
# Q2_create_database.py

print("\n--- Q2: Create a New Database ---")
new_db_name = "university_db.db"
conn = None
try:
    # In SQLite, connecting to a non-existent database file automatically creates it
    # In MySQL, you execute: CREATE DATABASE IF NOT EXISTS university_db;
    conn = sqlite3.connect(new_db_name)
    print(f"Success: Database '{new_db_name}' created / opened successfully.")
except sqlite3.Error as err:
    print(f"Error creating database: {err}")
finally:
    if conn:
        conn.close()


# ==============================================================================
# Q3: Write a program to create a new table named students with columns (id, name, age, marks).
# ==============================================================================
# Q3_create_students_table.py

print("\n--- Q3: Create Table 'students' ---")
conn = None
try:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # SQL query to create 'students' table with proper constraints
    create_table_query = """
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        marks REAL NOT NULL
    );
    """
    cursor.execute(create_table_query)
    conn.commit()
    print("Success: Table 'students' (id, name, age, marks) created successfully.")
except sqlite3.Error as err:
    print(f"Error creating table: {err}")
finally:
    if conn:
        conn.close()


# ==============================================================================
# Q4: Write a program to describe the structure of the students table.
# ==============================================================================
# Q4_describe_table_structure.py

print("\n--- Q4: Describe Table Structure ---")
conn = None
try:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # In SQLite, PRAGMA table_info gives the schema (equivalent to DESCRIBE in MySQL)
    cursor.execute("PRAGMA table_info(students);")
    columns = cursor.fetchall()

    print(f"{'Col ID':<8} {'Column Name':<15} {'Data Type':<12} {'Not Null':<10} {'Default':<10} {'PK':<5}")
    print("-" * 65)
    for col in columns:
        col_id, col_name, col_type, not_null, default_val, is_pk = col
        print(f"{col_id:<8} {col_name:<15} {col_type:<12} {str(bool(not_null)):<10} {str(default_val):<10} {str(bool(is_pk)):<5}")
except sqlite3.Error as err:
    print(f"Error describing table: {err}")
finally:
    if conn:
        conn.close()


# ==============================================================================
# Q5: Write a program to list all tables available in the connected database.
# ==============================================================================
# Q5_list_all_tables.py

print("\n--- Q5: List All Tables in Database ---")
conn = None
try:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Query sqlite_master to find all user-created tables (equivalent to SHOW TABLES in MySQL)
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
    tables = cursor.fetchall()

    print(f"Tables available in '{DB_NAME}':")
    if tables:
        for idx, (tbl_name,) in enumerate(tables, start=1):
            print(f"  {idx}. {tbl_name}")
    else:
        print("  No user tables found.")
except sqlite3.Error as err:
    print(f"Error listing tables: {err}")
finally:
    if conn:
        conn.close()


# ==============================================================================
# Q6: Write a program to drop (delete) a table from the database.
# ==============================================================================
# Q6_drop_table.py

print("\n--- Q6: Drop a Table ---")
conn = None
try:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create a temporary table first to demonstrate dropping without destroying main data
    cursor.execute("CREATE TABLE IF NOT EXISTS demo_drop_table (temp_id INT, note TEXT);")
    conn.commit()
    print("Created temporary table 'demo_drop_table'.")

    # Drop the table
    cursor.execute("DROP TABLE IF EXISTS demo_drop_table;")
    conn.commit()
    print("Success: Table 'demo_drop_table' dropped successfully.")
except sqlite3.Error as err:
    print(f"Error dropping table: {err}")
finally:
    if conn:
        conn.close()


# ==============================================================================
# Q7: Write a program to check if a specific table exists in the database.
# ==============================================================================
# Q7_check_table_exists.py

print("\n--- Q7: Check if Table Exists ---")
table_to_check = "students"
conn = None
try:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Parameterized query to prevent SQL injection
    query = "SELECT name FROM sqlite_master WHERE type='table' AND name = ?;"
    cursor.execute(query, (table_to_check,))
    result = cursor.fetchone()

    if result:
        print(f"Verification: Table '{table_to_check}' EXISTS in the database.")
    else:
        print(f"Verification: Table '{table_to_check}' DOES NOT exist in the database.")
except sqlite3.Error as err:
    print(f"Error checking table existence: {err}")
finally:
    if conn:
        conn.close()


# ==============================================================================
# Q8: Write a Python program to insert a single record into the students table.
# ==============================================================================
# Q8_insert_single_record.py

print("\n--- Q8: Insert Single Record into 'students' ---")
conn = None
try:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Use parameterized query (?) to prevent SQL injection
    insert_query = "INSERT OR REPLACE INTO students (id, name, age, marks) VALUES (?, ?, ?, ?);"
    student_data = (1, "Shivam Kumar", 22, 88.5)

    cursor.execute(insert_query, student_data)
    conn.commit()
    print(f"Success: Inserted single student record -> ID: {student_data[0]}, Name: {student_data[1]}, Age: {student_data[2]}, Marks: {student_data[3]}")
except sqlite3.Error as err:
    print(f"Error inserting single record: {err}")
finally:
    if conn:
        conn.close()


# ==============================================================================
# Q9: Write a program to insert multiple records into the students table.
# ==============================================================================
# Q9_insert_multiple_records.py

print("\n--- Q9: Insert Multiple Records into 'students' ---")
conn = None
try:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # List of tuples containing student records
    multiple_students = [
        (2, "Aarav Sharma", 21, 92.0),
        (3, "Priya Singh", 23, 85.0),
        (4, "Rohan Verma", 22, 78.5),
        (5, "Neha Patel", 21, 95.5),
        (6, "Amit Kumar", 24, 38.0),   # Marks < 40 for testing deletion queries later
        (7, "Kavita Rawat", 22, 89.0),
        (8, "Deepak Joshi", 23, 35.5)   # Marks < 40 for testing deletion queries later
    ]

    insert_query = "INSERT OR REPLACE INTO students (id, name, age, marks) VALUES (?, ?, ?, ?);"
    # executemany efficiently executes the parameterized query across all items
    cursor.executemany(insert_query, multiple_students)
    conn.commit()
    print(f"Success: Inserted {len(multiple_students)} records into 'students' table.")
except sqlite3.Error as err:
    print(f"Error inserting multiple records: {err}")
finally:
    if conn:
        conn.close()


# ==============================================================================
# Q10: Write a program to read and display all records from the table.
# ==============================================================================
# Q10_read_all_records.py

print("\n--- Q10: Read and Display All Records ---")
conn = None
try:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, age, marks FROM students;")
    records = cursor.fetchall()

    print(f"{'ID':<6} {'Name':<18} {'Age':<6} {'Marks':<8}")
    print("-" * 42)
    for row in records:
        print(f"{row[0]:<6} {row[1]:<18} {row[2]:<6} {row[3]:<8.1f}")
    print(f"Total records displayed: {len(records)}")
except sqlite3.Error as err:
    print(f"Error reading records: {err}")
finally:
    if conn:
        conn.close()


# ==============================================================================
# Q11: Write a program to display only specific columns (like name and marks).
# ==============================================================================
# Q11_display_specific_columns.py

print("\n--- Q11: Display Specific Columns (Name, Marks) ---")
conn = None
try:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT name, marks FROM students;")
    records = cursor.fetchall()

    print(f"{'Student Name':<20} {'Marks':<8}")
    print("-" * 30)
    for name, marks in records:
        print(f"{name:<20} {marks:<8.1f}")
except sqlite3.Error as err:
    print(f"Error retrieving specific columns: {err}")
finally:
    if conn:
        conn.close()


# ==============================================================================
# Q12: Write a program to retrieve records where marks are greater than 80.
# ==============================================================================
# Q12_retrieve_marks_greater_than_80.py

print("\n--- Q12: Retrieve Records with Marks > 80 ---")
conn = None
try:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    threshold = 80.0
    query = "SELECT id, name, age, marks FROM students WHERE marks > ? ORDER BY marks DESC;"
    cursor.execute(query, (threshold,))
    records = cursor.fetchall()

    print(f"{'ID':<6} {'Name':<18} {'Age':<6} {'Marks':<8}")
    print("-" * 42)
    for row in records:
        print(f"{row[0]:<6} {row[1]:<18} {row[2]:<6} {row[3]:<8.1f}")
    print(f"Found {len(records)} student(s) scoring greater than {threshold}.")
except sqlite3.Error as err:
    print(f"Error querying marks > 80: {err}")
finally:
    if conn:
        conn.close()


# ==============================================================================
# Q13: Write a program to retrieve data sorted by marks in descending order.
# ==============================================================================
# Q13_sort_by_marks_descending.py

print("\n--- Q13: Retrieve Data Sorted by Marks (Descending) ---")
conn = None
try:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, age, marks FROM students ORDER BY marks DESC;")
    records = cursor.fetchall()

    print(f"{'Rank':<6} {'ID':<6} {'Name':<18} {'Marks':<8}")
    print("-" * 40)
    for rank, row in enumerate(records, start=1):
        print(f"{rank:<6} {row[0]:<6} {row[1]:<18} {row[3]:<8.1f}")
except sqlite3.Error as err:
    print(f"Error retrieving sorted data: {err}")
finally:
    if conn:
        conn.close()


# ==============================================================================
# Q14: Write a program to count the total number of records in the table.
# ==============================================================================
# Q14_count_total_records.py

print("\n--- Q14: Count Total Records in 'students' ---")
conn = None
try:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM students;")
    total_count = cursor.fetchone()[0]
    print(f"Total number of student records: {total_count}")
except sqlite3.Error as err:
    print(f"Error counting records: {err}")
finally:
    if conn:
        conn.close()


# ==============================================================================
# Q15: Write a program to display the top 3 highest scoring students.
# ==============================================================================
# Q15_top_3_highest_scoring_students.py

print("\n--- Q15: Top 3 Highest Scoring Students ---")
conn = None
try:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, age, marks FROM students ORDER BY marks DESC LIMIT 3;")
    top_students = cursor.fetchall()

    print(f"{'Rank':<6} {'ID':<6} {'Name':<18} {'Marks':<8}")
    print("-" * 40)
    for rank, student in enumerate(top_students, start=1):
        print(f"{rank:<6} {student[0]:<6} {student[1]:<18} {student[3]:<8.1f}")
except sqlite3.Error as err:
    print(f"Error retrieving top students: {err}")
finally:
    if conn:
        conn.close()


# ==============================================================================
# Q16: Write a Python program to update the marks of a student using their ID.
# ==============================================================================
# Q16_update_marks_by_id.py

print("\n--- Q16: Update Student Marks by ID ---")
target_id = 1
new_marks = 91.5
conn = None
try:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    update_query = "UPDATE students SET marks = ? WHERE id = ?;"
    cursor.execute(update_query, (new_marks, target_id))
    conn.commit()

    if cursor.rowcount > 0:
        print(f"Success: Updated marks for Student ID {target_id} to {new_marks}.")
    else:
        print(f"Notice: No student found with ID {target_id}.")
except sqlite3.Error as err:
    print(f"Error updating marks: {err}")
finally:
    if conn:
        conn.close()


# ==============================================================================
# Q17: Write a program to update the name of a student.
# ==============================================================================
# Q17_update_student_name.py

print("\n--- Q17: Update Student Name ---")
target_id = 4
updated_name = "Rohan V. Verma"
conn = None
try:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    update_query = "UPDATE students SET name = ? WHERE id = ?;"
    cursor.execute(update_query, (updated_name, target_id))
    conn.commit()

    if cursor.rowcount > 0:
        print(f"Success: Updated name of Student ID {target_id} to '{updated_name}'.")
    else:
        print(f"Notice: No student found with ID {target_id}.")
except sqlite3.Error as err:
    print(f"Error updating student name: {err}")
finally:
    if conn:
        conn.close()


# ==============================================================================
# Q18: Write a program to delete a student record using ID.
# ==============================================================================
# Q18_delete_student_by_id.py

print("\n--- Q18: Delete Student Record by ID ---")
delete_id = 8
conn = None
try:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    delete_query = "DELETE FROM students WHERE id = ?;"
    cursor.execute(delete_query, (delete_id,))
    conn.commit()

    if cursor.rowcount > 0:
        print(f"Success: Deleted student record with ID {delete_id}.")
    else:
        print(f"Notice: Record with ID {delete_id} does not exist.")
except sqlite3.Error as err:
    print(f"Error deleting record: {err}")
finally:
    if conn:
        conn.close()


# ==============================================================================
# Q19: Write a program to delete all students with marks below 40.
# ==============================================================================
# Q19_delete_failing_students.py

print("\n--- Q19: Delete All Students with Marks Below 40 ---")
conn = None
try:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cutoff_marks = 40.0
    delete_query = "DELETE FROM students WHERE marks < ?;"
    cursor.execute(delete_query, (cutoff_marks,))
    conn.commit()

    print(f"Success: Deleted {cursor.rowcount} student record(s) with marks < {cutoff_marks}.")
except sqlite3.Error as err:
    print(f"Error deleting records: {err}")
finally:
    if conn:
        conn.close()


# ==============================================================================
# Q20: Write a program to truncate (empty) a table while keeping its structure intact.
# ==============================================================================
# Q20_truncate_table.py

print("\n--- Q20: Truncate (Empty) a Table Keeping Structure Intact ---")
conn = None
try:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create a demo table with rows to demonstrate emptying table without affecting main students table
    cursor.execute("CREATE TABLE IF NOT EXISTS demo_truncate (id INT, val TEXT);")
    cursor.executemany("INSERT INTO demo_truncate VALUES (?, ?);", [(1, "A"), (2, "B"), (3, "C")])
    conn.commit()

    # In SQLite, DELETE FROM <table> empties all records while preserving table structure (equivalent to TRUNCATE TABLE)
    cursor.execute("DELETE FROM demo_truncate;")
    conn.commit()

    # Verify table is empty and structure is preserved
    cursor.execute("SELECT COUNT(*) FROM demo_truncate;")
    count = cursor.fetchone()[0]
    cursor.execute("PRAGMA table_info(demo_truncate);")
    cols = cursor.fetchall()

    print(f"Success: 'demo_truncate' table truncated.")
    print(f"Row count after truncate: {count}")
    print(f"Columns still preserved  : {[c[1] for c in cols]}")

    # Clean up demo table
    cursor.execute("DROP TABLE IF EXISTS demo_truncate;")
    conn.commit()
except sqlite3.Error as err:
    print(f"Error truncating table: {err}")
finally:
    if conn:
        conn.close()


# ==============================================================================
# Q21: Write a Python program to create a table for courses and insert data into it.
# ==============================================================================
# Q21_create_courses_table.py

print("\n--- Q21: Create 'courses' Table and Insert Records ---")
conn = None
try:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    create_courses_sql = """
    CREATE TABLE IF NOT EXISTS courses (
        course_id INTEGER PRIMARY KEY,
        course_name TEXT NOT NULL,
        student_id INTEGER,
        FOREIGN KEY (student_id) REFERENCES students(id)
    );
    """
    cursor.execute(create_courses_sql)

    courses_data = [
        (101, "Python Programming", 1),
        (102, "Database Management", 2),
        (103, "Data Structures", 3),
        (104, "Machine Learning", 1),
        (105, "Cloud Computing", 4),
        (106, "Cyber Security", 99)   # ID 99 does not exist in students to demonstrate LEFT JOIN
    ]

    cursor.executemany("INSERT OR REPLACE INTO courses (course_id, course_name, student_id) VALUES (?, ?, ?);", courses_data)
    conn.commit()
    print(f"Success: 'courses' table created and {len(courses_data)} records inserted.")
except sqlite3.Error as err:
    print(f"Error in courses table operations: {err}")
finally:
    if conn:
        conn.close()


# ==============================================================================
# Q22: Write a program to perform an INNER JOIN between students and courses.
# ==============================================================================
# Q22_inner_join_students_courses.py

print("\n--- Q22: INNER JOIN (students & courses) ---")
conn = None
try:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # INNER JOIN returns rows where student_id matches in both tables
    inner_join_query = """
    SELECT students.id, students.name, courses.course_id, courses.course_name
    FROM students
    INNER JOIN courses ON students.id = courses.student_id;
    """
    cursor.execute(inner_join_query)
    rows = cursor.fetchall()

    print(f"{'Student ID':<12} {'Student Name':<18} {'Course ID':<12} {'Course Name':<22}")
    print("-" * 66)
    for row in rows:
        print(f"{row[0]:<12} {row[1]:<18} {row[2]:<12} {row[3]:<22}")
except sqlite3.Error as err:
    print(f"Error performing INNER JOIN: {err}")
finally:
    if conn:
        conn.close()


# ==============================================================================
# Q23: Write a program to perform a LEFT JOIN between students and courses.
# ==============================================================================
# Q23_left_join_students_courses.py

print("\n--- Q23: LEFT JOIN (students & courses) ---")
conn = None
try:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # LEFT JOIN returns all students, even those who have not enrolled in any course
    left_join_query = """
    SELECT students.id, students.name, courses.course_id, courses.course_name
    FROM students
    LEFT JOIN courses ON students.id = courses.student_id;
    """
    cursor.execute(left_join_query)
    rows = cursor.fetchall()

    print(f"{'Student ID':<12} {'Student Name':<18} {'Course ID':<12} {'Course Name':<22}")
    print("-" * 66)
    for row in rows:
        cid_str = str(row[2]) if row[2] is not None else "None"
        cname_str = row[3] if row[3] is not None else "No Course"
        print(f"{row[0]:<12} {row[1]:<18} {cid_str:<12} {cname_str:<22}")
except sqlite3.Error as err:
    print(f"Error performing LEFT JOIN: {err}")
finally:
    if conn:
        conn.close()


# ==============================================================================
# Q24: Write a program to find the average marks of all students.
# ==============================================================================
# Q24_average_marks_of_students.py

print("\n--- Q24: Average Marks of All Students ---")
conn = None
try:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT AVG(marks), COUNT(*), MIN(marks), MAX(marks) FROM students;")
    avg_marks, count, min_m, max_m = cursor.fetchone()

    print(f"Total Students Evaluated : {count}")
    print(f"Minimum Marks            : {min_m:.2f}")
    print(f"Maximum Marks            : {max_m:.2f}")
    print(f"Average Marks            : {avg_marks:.2f}")
except sqlite3.Error as err:
    print(f"Error calculating average marks: {err}")
finally:
    if conn:
        conn.close()


# ==============================================================================
# Q25: Write a program to display students grouped by age and count how many are in each group.
# ==============================================================================
# Q25_group_by_age_count.py

print("\n--- Q25: Students Grouped by Age ---")
conn = None
try:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    group_query = """
    SELECT age, COUNT(*) AS student_count, AVG(marks) AS average_marks
    FROM students
    GROUP BY age
    ORDER BY age ASC;
    """
    cursor.execute(group_query)
    results = cursor.fetchall()

    print(f"{'Age':<8} {'Student Count':<16} {'Average Marks':<14}")
    print("-" * 40)
    for age, cnt, avg_m in results:
        print(f"{age:<8} {cnt:<16} {avg_m:<14.2f}")
except sqlite3.Error as err:
    print(f"Error executing GROUP BY query: {err}")
finally:
    if conn:
        conn.close()


# ==============================================================================
# Q26: Write a program to export table data from the database into a CSV file.
# ==============================================================================
# Q26_export_table_to_csv.py

print("\n--- Q26: Export Table Data to CSV ---")
csv_export_file = "exported_students.csv"
conn = None
try:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, age, marks FROM students;")
    rows = cursor.fetchall()

    with open(csv_export_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # Write CSV header
        writer.writerow(["ID", "Name", "Age", "Marks"])
        # Write all records
        writer.writerows(rows)

    print(f"Success: Exported {len(rows)} records from 'students' to '{csv_export_file}'.")
except (sqlite3.Error, IOError) as err:
    print(f"Error exporting table to CSV: {err}")
finally:
    if conn:
        conn.close()


# ==============================================================================
# Q27: Write a program to import data from a CSV file into a database table.
# ==============================================================================
# Q27_import_csv_to_database.py

print("\n--- Q27: Import Data from CSV into Table ---")
csv_import_file = "exported_students.csv"
conn = None
try:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create destination table for imported data
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS imported_students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        marks REAL
    );
    """)

    with open(csv_import_file, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)  # Skip header row
        records_to_insert = [(int(r[0]), r[1], int(r[2]), float(r[3])) for r in reader]

    cursor.executemany("INSERT OR REPLACE INTO imported_students VALUES (?, ?, ?, ?);", records_to_insert)
    conn.commit()

    print(f"Success: Imported {len(records_to_insert)} records from '{csv_import_file}' into 'imported_students' table.")
except (sqlite3.Error, IOError, ValueError) as err:
    print(f"Error importing CSV to table: {err}")
finally:
    if conn:
        conn.close()


# ==============================================================================
# Q28: Write a program to display all database errors using exception handling.
# ==============================================================================
# Q28_database_exception_handling.py

print("\n--- Q28: Database Exception Handling Demonstration ---")
conn = None
try:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    print("Attempting to execute an invalid SQL statement (deliberate syntax error)...")
    # This statement deliberately contains an error: "SELEC" instead of "SELECT"
    cursor.execute("SELEC * FROM students;")
except sqlite3.OperationalError as op_err:
    print(f"[Caught OperationalError]: {op_err}")
except sqlite3.IntegrityError as int_err:
    print(f"[Caught IntegrityError]: {int_err}")
except sqlite3.DatabaseError as db_err:
    print(f"[Caught DatabaseError]: {db_err}")
except Exception as general_err:
    print(f"[Caught General Exception]: {general_err}")
finally:
    if conn:
        conn.close()
        print("Database connection safely closed in finally block.")


# ==============================================================================
# Q29: Write a program to use a function to insert and fetch data (modular approach).
# ==============================================================================
# Q29_modular_database_operations.py

print("\n--- Q29: Modular Database Functions ---")

def insert_student(connection, student_id, name, age, marks):
    """Modular function to insert a single student record."""
    sql = "INSERT OR REPLACE INTO students (id, name, age, marks) VALUES (?, ?, ?, ?);"
    with connection:
        connection.execute(sql, (student_id, name, age, marks))
    print(f"Modular Insert: Successfully added '{name}' (ID: {student_id}).")

def fetch_all_students(connection):
    """Modular function to retrieve all student records."""
    cursor = connection.cursor()
    cursor.execute("SELECT id, name, age, marks FROM students;")
    return cursor.fetchall()

def fetch_student_by_id(connection, student_id):
    """Modular function to retrieve a specific student by ID."""
    cursor = connection.cursor()
    cursor.execute("SELECT id, name, age, marks FROM students WHERE id = ?;", (student_id,))
    return cursor.fetchone()

# Demonstration of modular functions
try:
    conn = sqlite3.connect(DB_NAME)
    # Insert new record using modular function
    insert_student(conn, 10, "Vikas Gupta", 23, 87.0)

    # Fetch specific student
    student = fetch_student_by_id(conn, 10)
    print("Modular Fetch by ID (10):", student)

    # Fetch all students
    all_s = fetch_all_students(conn)
    print(f"Modular Fetch All: Retrieved {len(all_s)} total student(s).")
except sqlite3.Error as err:
    print(f"Modular Function Error: {err}")
finally:
    if conn:
        conn.close()


# ==============================================================================
# Q30: Write a program to create a simple menu-driven application for student management (Add, View, Update, Delete).
# ==============================================================================
# Q30_menu_driven_student_management.py

print("\n--- Q30: Menu-Driven Student Management Application ---")

def student_management_app():
    """Menu-driven interactive student management application."""
    def get_connection():
        return sqlite3.connect(DB_NAME)

    def add_student_record():
        try:
            sid = int(input("Enter Student ID: ").strip() or "11")
            name = input("Enter Student Name: ").strip() or "Test Student"
            age = int(input("Enter Age: ").strip() or "22")
            marks = float(input("Enter Marks: ").strip() or "84.0")
            with get_connection() as c:
                c.execute("INSERT OR REPLACE INTO students VALUES (?, ?, ?, ?);", (sid, name, age, marks))
            print(f"Success: Student '{name}' added successfully.")
        except Exception as e:
            print(f"Error adding student: {e}")

    def view_all_students():
        try:
            with get_connection() as c:
                cur = c.cursor()
                cur.execute("SELECT * FROM students;")
                rows = cur.fetchall()
            print(f"\n{'ID':<6} {'Name':<18} {'Age':<6} {'Marks':<8}")
            print("-" * 40)
            for r in rows:
                print(f"{r[0]:<6} {r[1]:<18} {r[2]:<6} {r[3]:<8.1f}")
        except Exception as e:
            print(f"Error viewing students: {e}")

    def update_student_marks():
        try:
            sid = int(input("Enter Student ID to update: ").strip() or "1")
            new_m = float(input("Enter new Marks: ").strip() or "96.0")
            with get_connection() as c:
                cur = c.cursor()
                cur.execute("UPDATE students SET marks = ? WHERE id = ?;", (new_m, sid))
                if cur.rowcount > 0:
                    print(f"Success: Updated ID {sid} to {new_m} marks.")
                else:
                    print(f"Notice: Student ID {sid} not found.")
        except Exception as e:
            print(f"Error updating student: {e}")

    def delete_student_record():
        try:
            sid = int(input("Enter Student ID to delete: ").strip() or "11")
            with get_connection() as c:
                cur = c.cursor()
                cur.execute("DELETE FROM students WHERE id = ?;", (sid,))
                if cur.rowcount > 0:
                    print(f"Success: Deleted Student ID {sid}.")
                else:
                    print(f"Notice: Student ID {sid} not found.")
        except Exception as e:
            print(f"Error deleting student: {e}")

    # Menu display
    menu_text = """
    ================ STUDENT MANAGEMENT SYSTEM ================
    1. Add Student
    2. View All Students
    3. Update Student Marks
    4. Delete Student
    5. Exit
    ===========================================================
    """
    print(menu_text)
    choice = input("Enter choice (1-5, press Enter to view default demonstration): ").strip()

    if choice == "1":
        add_student_record()
    elif choice == "2":
        view_all_students()
    elif choice == "3":
        update_student_marks()
    elif choice == "4":
        delete_student_record()
    elif choice == "5":
        print("Exiting Student Management Application.")
    else:
        # Default demonstration for non-interactive execution
        print("Running automatic demonstration:")
        print("1. Displaying current students list:")
        view_all_students()
        print("\nStudent Management Application demonstration completed.")

# Execute menu app demo
student_management_app()
