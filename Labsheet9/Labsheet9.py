# ==============================================================================
# Lab Sheet-09: Python Programming Lab – CRUD Operations using Python Programming
# MCA I Semester (Session 2026-2027)
# COER University, Roorkee
# ==============================================================================

import os
import sqlite3

# Common SQLite Database for database-based CRUD questions
DB_NAME = "crud_student_db.db"


# ==============================================================================
# Q1: Write a Python program to create a list of student records (Create operation).
# ==============================================================================
# Q1_create_student_records_list.py

print("\n--- Q1: Create Student Records in a List ---")
# Initializing an empty list to hold student record dictionaries
students_list = []

# Function to add/create a student record
def add_student_to_list(s_list, roll_no, name, age, marks):
    student = {
        "roll_no": roll_no,
        "name": name,
        "age": age,
        "marks": marks
    }
    s_list.append(student)
    print(f"Success: Student '{name}' (Roll No: {roll_no}) added.")

# Adding initial student records (Create Operation)
add_student_to_list(students_list, 101, "Shivam Kumar", 22, 88.5)
add_student_to_list(students_list, 102, "Aarav Sharma", 21, 92.0)
add_student_to_list(students_list, 103, "Priya Singh", 23, 85.0)

print(f"Total students in list: {len(students_list)}")
print("Raw List:", students_list)


# ==============================================================================
# Q2: Write a program to display all student records from the list (Read operation).
# ==============================================================================
# Q2_read_all_student_records_list.py

print("\n--- Q2: Read/Display All Student Records from List ---")
if not students_list:
    print("The student list is currently empty.")
else:
    print(f"{'Roll No':<10} {'Student Name':<20} {'Age':<6} {'Marks':<8}")
    print("-" * 46)
    for student in students_list:
        print(f"{student['roll_no']:<10} {student['name']:<20} {student['age']:<6} {student['marks']:<8.1f}")
    print("-" * 46)


# ==============================================================================
# Q3: Write a program to search for a student by name in the list.
# ==============================================================================
# Q3_search_student_by_name_list.py

print("\n--- Q3: Search for Student by Name in List ---")
search_query = "Shivam"
found_students = [s for s in students_list if search_query.lower() in s["name"].lower()]

if found_students:
    print(f"Found {len(found_students)} student(s) matching '{search_query}':")
    for s in found_students:
        print(f"  Roll No: {s['roll_no']}, Name: {s['name']}, Age: {s['age']}, Marks: {s['marks']}")
else:
    print(f"No student found with name matching '{search_query}'.")


# ==============================================================================
# Q4: Write a program to update a student’s marks in the list (Update operation).
# ==============================================================================
# Q4_update_student_marks_list.py

print("\n--- Q4: Update Student Marks in List ---")
target_roll = 101
new_marks = 95.0

updated = False
for student in students_list:
    if student["roll_no"] == target_roll:
        old_marks = student["marks"]
        student["marks"] = new_marks
        print(f"Success: Updated Roll No {target_roll} ({student['name']}) marks from {old_marks} to {new_marks}.")
        updated = True
        break

if not updated:
    print(f"Notice: Student with Roll No {target_roll} not found.")


# ==============================================================================
# Q5: Write a program to delete a student record by roll number (Delete operation).
# ==============================================================================
# Q5_delete_student_record_list.py

print("\n--- Q5: Delete Student Record by Roll Number ---")
del_roll = 103

student_to_delete = None
for s in students_list:
    if s["roll_no"] == del_roll:
        student_to_delete = s
        break

if student_to_delete:
    students_list.remove(student_to_delete)
    print(f"Success: Student with Roll No {del_roll} ('{student_to_delete['name']}') removed.")
else:
    print(f"Notice: Roll No {del_roll} not found in list.")

print(f"Remaining students count: {len(students_list)}")


# ==============================================================================
# Q6: Write a program to implement CRUD operations on a dictionary of employee data.
# ==============================================================================
# Q6_crud_dictionary_employee_data.py

print("\n--- Q6: CRUD Operations on Employee Dictionary ---")
# Employee Dictionary with Emp_ID as Key
employees = {}

# 1. CREATE: Add employees
employees[1001] = {"name": "Rajesh Sharma", "dept": "Engineering", "salary": 75000}
employees[1002] = {"name": "Anita Roy", "dept": "HR", "salary": 62000}
employees[1003] = {"name": "Suresh Nair", "dept": "Finance", "salary": 68000}
print(f"[CREATE] Added 3 employees. Total: {len(employees)}")

# 2. READ: Display all employees
print("[READ] All Employee Records:")
for emp_id, info in employees.items():
    print(f"  ID: {emp_id} | Name: {info['name']:<15} | Dept: {info['dept']:<12} | Salary: Rs.{info['salary']}")

# 3. UPDATE: Update salary of employee 1002
emp_to_update = 1002
if emp_to_update in employees:
    employees[emp_to_update]["salary"] = 67000
    print(f"[UPDATE] Updated salary for Employee {emp_to_update} to Rs.{employees[emp_to_update]['salary']}.")

# 4. DELETE: Remove employee 1003
emp_to_delete = 1003
if emp_to_delete in employees:
    removed_emp = employees.pop(emp_to_delete)
    print(f"[DELETE] Removed Employee {emp_to_delete} ({removed_emp['name']}).")

print(f"[RESULT] Final Employee Dictionary: {employees}")


# ==============================================================================
# Q7: Write a menu-driven Python program for CRUD operations on a list of books (Add, View, Update, Delete).
# ==============================================================================
# Q7_menu_driven_crud_books_list.py

print("\n--- Q7: Menu-Driven CRUD on List of Books ---")
books_catalog = [
    {"isbn": "978-01", "title": "Python Programming", "author": "Guido van Rossum", "price": 450.0},
    {"isbn": "978-02", "title": "Data Structures in Python", "author": "Michael Goodrich", "price": 550.0}
]

def books_crud_app():
    def add_book():
        isbn = input("Enter ISBN (default: '978-03'): ").strip() or "978-03"
        title = input("Enter Title (default: 'Database Systems'): ").strip() or "Database Systems"
        author = input("Enter Author (default: 'Silberschatz'): ").strip() or "Silberschatz"
        price = float(input("Enter Price (default: '600.0'): ").strip() or "600.0")
        books_catalog.append({"isbn": isbn, "title": title, "author": author, "price": price})
        print(f"Success: Book '{title}' added.")

    def view_books():
        print(f"\n{'ISBN':<10} {'Title':<28} {'Author':<20} {'Price (Rs)':<10}")
        print("-" * 70)
        for b in books_catalog:
            print(f"{b['isbn']:<10} {b['title']:<28} {b['author']:<20} {b['price']:<10.2f}")
        print("-" * 70)

    def update_book():
        isbn = input("Enter ISBN to update (default: '978-01'): ").strip() or "978-01"
        for b in books_catalog:
            if b["isbn"] == isbn:
                new_price = float(input("Enter new price (default: '499.0'): ").strip() or "499.0")
                b["price"] = new_price
                print(f"Success: Price for '{b['title']}' updated to Rs.{new_price}.")
                return
        print(f"Book with ISBN '{isbn}' not found.")

    def delete_book():
        isbn = input("Enter ISBN to delete (default: '978-02'): ").strip() or "978-02"
        for idx, b in enumerate(books_catalog):
            if b["isbn"] == isbn:
                removed = books_catalog.pop(idx)
                print(f"Success: Removed book '{removed['title']}'.")
                return
        print(f"Book with ISBN '{isbn}' not found.")

    # Demonstration execution
    print("Executing demonstration of Book Catalog CRUD:")
    print("1. Initial Catalog:")
    view_books()
    print("\n2. Adding a new book:")
    books_catalog.append({"isbn": "978-03", "title": "Database Systems", "author": "Silberschatz", "price": 600.0})
    print("Added 'Database Systems'.")
    print("\n3. Updating book price:")
    books_catalog[0]["price"] = 499.0
    print(f"Updated '{books_catalog[0]['title']}' price to {books_catalog[0]['price']}.")
    print("\n4. Current Books View:")
    view_books()

books_crud_app()


# ==============================================================================
# Q8: Write a program to store and manage product details using CRUD operations.
# ==============================================================================
# Q8_product_details_crud.py

print("\n--- Q8: Product Details Management (CRUD) ---")
products = {}

# CREATE
def add_product(pid, name, category, price, stock):
    products[pid] = {"name": name, "category": category, "price": price, "stock": stock}
    print(f"[CREATE] Product '{name}' (ID: {pid}) registered.")

# READ
def view_products():
    print(f"{'PID':<6} {'Product Name':<18} {'Category':<14} {'Price':<10} {'Stock':<6}")
    print("-" * 56)
    for pid, p in products.items():
        print(f"{pid:<6} {p['name']:<18} {p['category']:<14} Rs.{p['price']:<7.2f} {p['stock']:<6}")
    print("-" * 56)

# UPDATE
def update_product_price(pid, new_price):
    if pid in products:
        products[pid]["price"] = new_price
        print(f"[UPDATE] Updated Product {pid} price to Rs.{new_price}.")
    else:
        print(f"Product {pid} not found.")

# DELETE
def delete_product(pid):
    if pid in products:
        removed = products.pop(pid)
        print(f"[DELETE] Removed product '{removed['name']}' (ID: {pid}).")
    else:
        print(f"Product {pid} not found.")

# Execute operations
add_product(101, "Wireless Mouse", "Electronics", 799.0, 45)
add_product(102, "Mechanical Keyboard", "Electronics", 2499.0, 20)
add_product(103, "USB-C Hub", "Accessories", 1299.0, 30)

view_products()
update_product_price(101, 749.0)
delete_product(103)
print("Updated Products List:")
view_products()


# ==============================================================================
# Q9: Write a program to save student data into a text file and read it back.
# ==============================================================================
# Q9_save_and_read_student_data_file.py

print("\n--- Q9: Save Student Data to Text File & Read Back ---")
file_name = "students_file_data.txt"

# Sample student records
records_to_save = [
    "101,Shivam Kumar,22,88.5\n",
    "102,Aarav Sharma,21,92.0\n",
    "103,Priya Singh,23,85.0\n"
]

try:
    # Writing to file
    with open(file_name, "w", encoding="utf-8") as f:
        f.writelines(records_to_save)
    print(f"Success: Saved {len(records_to_save)} records to '{file_name}'.")

    # Reading back from file
    print(f"Reading back data from '{file_name}':")
    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            r_id, r_name, r_age, r_marks = line.strip().split(",")
            print(f"  Roll No: {r_id} | Name: {r_name:<15} | Age: {r_age} | Marks: {r_marks}")
except IOError as err:
    print(f"File I/O Error: {err}")


# ==============================================================================
# Q10: Write a program to perform CRUD operations on a file — add, view, modify, and delete records.
# ==============================================================================
# Q10_file_based_crud_operations.py

print("\n--- Q10: File-Based CRUD Operations ---")
crud_file = "crud_records.txt"

# Helper to read all records as list of tuples: (id, name, marks)
def load_file_records():
    recs = []
    if os.path.exists(crud_file):
        with open(crud_file, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    parts = line.strip().split(",")
                    recs.append(parts)
    return recs

# Helper to save all records back to file
def save_file_records(recs):
    with open(crud_file, "w", encoding="utf-8") as f:
        for r in recs:
            f.write(",".join(r) + "\n")

# 1. CREATE (Add record)
def file_add_record(rid, name, marks):
    recs = load_file_records()
    recs.append([str(rid), name, str(marks)])
    save_file_records(recs)
    print(f"[FILE CREATE] Added record: ({rid}, {name}, {marks})")

# 2. READ (View all records)
def file_view_records():
    recs = load_file_records()
    print(f"\n[FILE READ] Contents of '{crud_file}':")
    print(f"{'ID':<6} {'Name':<18} {'Marks':<8}")
    print("-" * 34)
    for r in recs:
        print(f"{r[0]:<6} {r[1]:<18} {r[2]:<8}")
    print("-" * 34)

# 3. UPDATE (Modify record by ID)
def file_modify_record(target_id, new_marks):
    recs = load_file_records()
    found = False
    for r in recs:
        if r[0] == str(target_id):
            r[2] = str(new_marks)
            found = True
            break
    if found:
        save_file_records(recs)
        print(f"[FILE UPDATE] Modified ID {target_id} marks to {new_marks}.")
    else:
        print(f"[FILE UPDATE] ID {target_id} not found.")

# 4. DELETE (Delete record by ID)
def file_delete_record(target_id):
    recs = load_file_records()
    original_len = len(recs)
    recs = [r for r in recs if r[0] != str(target_id)]
    if len(recs) < original_len:
        save_file_records(recs)
        print(f"[FILE DELETE] Deleted record with ID {target_id}.")
    else:
        print(f"[FILE DELETE] ID {target_id} not found.")

# Initialize and execute file CRUD demo
save_file_records([]) # reset demo file
file_add_record(1, "Shivam Kumar", 88.5)
file_add_record(2, "Aarav Sharma", 92.0)
file_add_record(3, "Rohan Verma", 78.5)
file_view_records()
file_modify_record(2, 95.0)
file_delete_record(3)
file_view_records()


# ==============================================================================
# Q11: Write a Python program to connect to a database and create a table students.
# ==============================================================================
# Q11_connect_and_create_students_table.py

print("\n--- Q11: Connect to Database & Create Table 'students' ---")
conn = None
try:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        marks REAL
    );
    """
    cursor.execute(create_table_query)
    conn.commit()
    print(f"Success: Connected to '{DB_NAME}' and table 'students' ensured.")
except sqlite3.Error as err:
    print(f"Database Error: {err}")
finally:
    if conn:
        conn.close()


# ==============================================================================
# Q12: Write a program to insert a new record into the table (Create operation).
# ==============================================================================
# Q12_insert_new_student_record.py

print("\n--- Q12: Insert Record into 'students' (Create Operation) ---")
conn = None
try:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    insert_query = "INSERT OR REPLACE INTO students (id, name, age, marks) VALUES (?, ?, ?, ?);"
    new_student = (101, "Shivam Kumar", 22, 88.5)

    cursor.execute(insert_query, new_student)
    conn.commit()
    print(f"Success: Inserted student {new_student} into 'students' table.")
except sqlite3.Error as err:
    print(f"Database Insertion Error: {err}")
finally:
    if conn:
        conn.close()


# ==============================================================================
# Q13: Write a program to read and display all records from the table (Read operation).
# ==============================================================================
# Q13_read_display_all_records.py

print("\n--- Q13: Read & Display All Records from 'students' ---")
conn = None
try:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Pre-populate sample records so read queries have diverse data
    sample_students = [
        (102, "Aarav Sharma", 21, 92.0),
        (103, "Priya Singh", 23, 85.0),
        (104, "Rohan Verma", 22, 78.5),
        (105, "Neha Patel", 21, 95.5)
    ]
    cursor.executemany("INSERT OR REPLACE INTO students VALUES (?, ?, ?, ?);", sample_students)
    conn.commit()

    cursor.execute("SELECT id, name, age, marks FROM students;")
    rows = cursor.fetchall()

    print(f"{'Roll No (ID)':<14} {'Student Name':<20} {'Age':<6} {'Marks':<8}")
    print("-" * 50)
    for r in rows:
        print(f"{r[0]:<14} {r[1]:<20} {r[2]:<6} {r[3]:<8.1f}")
    print("-" * 50)
    print(f"Total records retrieved: {len(rows)}")
except sqlite3.Error as err:
    print(f"Database Read Error: {err}")
finally:
    if conn:
        conn.close()


# ==============================================================================
# Q14: Write a program to search for a specific student by roll number.
# ==============================================================================
# Q14_search_student_by_roll_number.py

print("\n--- Q14: Search Student by Roll Number ---")
target_roll = 101
conn = None
try:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    query = "SELECT id, name, age, marks FROM students WHERE id = ?;"
    cursor.execute(query, (target_roll,))
    student = cursor.fetchone()

    if student:
        print(f"Found Student with Roll No {target_roll}:")
        print(f"  Name  : {student[1]}")
        print(f"  Age   : {student[2]}")
        print(f"  Marks : {student[3]}")
    else:
        print(f"No student found with Roll No {target_roll}.")
except sqlite3.Error as err:
    print(f"Database Search Error: {err}")
finally:
    if conn:
        conn.close()


# ==============================================================================
# Q15: Write a program to update the marks of a student using roll number (Update operation).
# ==============================================================================
# Q15_update_student_marks_db.py

print("\n--- Q15: Update Student Marks using Roll Number ---")
target_roll = 104
updated_marks = 83.5
conn = None
try:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    update_query = "UPDATE students SET marks = ? WHERE id = ?;"
    cursor.execute(update_query, (updated_marks, target_roll))
    conn.commit()

    if cursor.rowcount > 0:
        print(f"Success: Updated marks for Roll No {target_roll} to {updated_marks}.")
    else:
        print(f"Notice: Student with Roll No {target_roll} does not exist.")
except sqlite3.Error as err:
    print(f"Database Update Error: {err}")
finally:
    if conn:
        conn.close()


# ==============================================================================
# Q16: Write a program to delete a student record using roll number (Delete operation).
# ==============================================================================
# Q16_delete_student_by_roll_number_db.py

print("\n--- Q16: Delete Student Record using Roll Number ---")
del_roll = 103
conn = None
try:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    delete_query = "DELETE FROM students WHERE id = ?;"
    cursor.execute(delete_query, (del_roll,))
    conn.commit()

    if cursor.rowcount > 0:
        print(f"Success: Deleted student record with Roll No {del_roll}.")
    else:
        print(f"Notice: Student with Roll No {del_roll} not found.")
except sqlite3.Error as err:
    print(f"Database Deletion Error: {err}")
finally:
    if conn:
        conn.close()


# ==============================================================================
# Q17: Write a program to count and display the total number of records in the table.
# ==============================================================================
# Q17_count_total_records_db.py

print("\n--- Q17: Count Total Records in 'students' Table ---")
conn = None
try:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM students;")
    count = cursor.fetchone()[0]
    print(f"Total number of students in database: {count}")
except sqlite3.Error as err:
    print(f"Database Error: {err}")
finally:
    if conn:
        conn.close()


# ==============================================================================
# Q18: Write a program to display all records sorted by student name.
# ==============================================================================
# Q18_display_sorted_by_name_db.py

print("\n--- Q18: Display Records Sorted by Student Name ---")
conn = None
try:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, age, marks FROM students ORDER BY name ASC;")
    rows = cursor.fetchall()

    print(f"{'Roll No':<10} {'Student Name':<20} {'Age':<6} {'Marks':<8}")
    print("-" * 46)
    for r in rows:
        print(f"{r[0]:<10} {r[1]:<20} {r[2]:<6} {r[3]:<8.1f}")
    print("-" * 46)
except sqlite3.Error as err:
    print(f"Database Sorting Error: {err}")
finally:
    if conn:
        conn.close()


# ==============================================================================
# Q19: Write a program to find the student with the highest marks from the database.
# ==============================================================================
# Q19_find_highest_marks_student_db.py

print("\n--- Q19: Find Student with Highest Marks ---")
conn = None
try:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Query to fetch the student with highest marks
    query = """
    SELECT id, name, age, marks
    FROM students
    WHERE marks = (SELECT MAX(marks) FROM students);
    """
    cursor.execute(query)
    top_students = cursor.fetchall()

    if top_students:
        print("Topper Student(s):")
        for topper in top_students:
            print(f"  Roll No : {topper[0]}")
            print(f"  Name    : {topper[1]}")
            print(f"  Age     : {topper[2]}")
            print(f"  Marks   : {topper[3]}")
    else:
        print("No student records found in table.")
except sqlite3.Error as err:
    print(f"Database Query Error: {err}")
finally:
    if conn:
        conn.close()


# ==============================================================================
# Q20: Write a menu-driven Python application to perform all CRUD operations using a database.
# ==============================================================================
# Q20_menu_driven_database_crud.py

print("\n--- Q20: Menu-Driven Database CRUD Application ---")

def db_crud_application():
    def get_conn():
        return sqlite3.connect(DB_NAME)

    def menu_create_student():
        try:
            sid = int(input("Enter Roll No (default: 106): ").strip() or "106")
            name = input("Enter Student Name (default: 'Megha Sen'): ").strip() or "Megha Sen"
            age = int(input("Enter Age (default: 22): ").strip() or "22")
            marks = float(input("Enter Marks (default: 94.5): ").strip() or "94.5")
            with get_conn() as c:
                c.execute("INSERT OR REPLACE INTO students VALUES (?, ?, ?, ?);", (sid, name, age, marks))
            print(f"Success: Student '{name}' added successfully.")
        except Exception as e:
            print(f"Error adding student: {e}")

    def menu_read_students():
        try:
            with get_conn() as c:
                cur = c.cursor()
                cur.execute("SELECT id, name, age, marks FROM students;")
                rows = cur.fetchall()
            print(f"\n{'Roll No':<10} {'Name':<20} {'Age':<6} {'Marks':<8}")
            print("-" * 46)
            for r in rows:
                print(f"{r[0]:<10} {r[1]:<20} {r[2]:<6} {r[3]:<8.1f}")
            print("-" * 46)
        except Exception as e:
            print(f"Error viewing students: {e}")

    def menu_update_student():
        try:
            sid = int(input("Enter Roll No to update (default: 101): ").strip() or "101")
            new_m = float(input("Enter updated Marks (default: 96.0): ").strip() or "96.0")
            with get_conn() as c:
                cur = c.cursor()
                cur.execute("UPDATE students SET marks = ? WHERE id = ?;", (new_m, sid))
                if cur.rowcount > 0:
                    print(f"Success: Updated marks for Roll No {sid} to {new_m}.")
                else:
                    print(f"Notice: Student with Roll No {sid} not found.")
        except Exception as e:
            print(f"Error updating student: {e}")

    def menu_delete_student():
        try:
            sid = int(input("Enter Roll No to delete (default: 106): ").strip() or "106")
            with get_conn() as c:
                cur = c.cursor()
                cur.execute("DELETE FROM students WHERE id = ?;", (sid,))
                if cur.rowcount > 0:
                    print(f"Success: Deleted record for Roll No {sid}.")
                else:
                    print(f"Notice: Student with Roll No {sid} not found.")
        except Exception as e:
            print(f"Error deleting student: {e}")

    menu_banner = """
    ================ STUDENT DATABASE CRUD APP ================
    1. Create (Add New Student)
    2. Read (View All Students)
    3. Update (Update Student Marks)
    4. Delete (Delete Student by Roll No)
    5. Exit
    ============================================================
    """
    print(menu_banner)
    choice = input("Enter choice (1-5, press Enter to view default demonstration): ").strip()

    if choice == "1":
        menu_create_student()
    elif choice == "2":
        menu_read_students()
    elif choice == "3":
        menu_update_student()
    elif choice == "4":
        menu_delete_student()
    elif choice == "5":
        print("Exiting application.")
    else:
        print("Running automatic demonstration of Database CRUD:")
        print("Viewing all records currently stored in database:")
        menu_read_students()
        print("Demonstration completed successfully.")

db_crud_application()
