import sqlite3

# DATABASE SETUP ----------------
connection = sqlite3.connect("crud_operations.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS crud (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    cource TEXT NOT NULL,
    age INTEGER NOT NULL,
    contact INTEGER NOT NULL
)
""")
connection.commit()


#  CRUD FUNCTIONS ----------------
def list_all_students():
    cursor.execute("SELECT * FROM crud")
    rows = cursor.fetchall()

    if not rows:
        print("No students found")
    else:
        for row in rows:
            print(row)


def add_student():
    name = input("Name: ").strip()
    cource = input("Course: ").strip()

    while True:
        age_input = input("Age: ").strip()
        if age_input.isdigit():
            age = int(age_input)
            break
        print("Age must be a number")

    while True:
        contact_input = input("Contact: ").strip()
        if contact_input.isdigit():
            contact = int(contact_input)
            break
        print("Contact must be a number")

    cursor.execute(
        "INSERT INTO crud (name, cource, age, contact) VALUES (?, ?, ?, ?)",
        (name, cource, age, contact)
    )
    connection.commit()
    print("Student added")


def update_student():
    student_id = int(input("Student ID to update: "))

    cursor.execute("SELECT * FROM crud WHERE id = ?", (student_id,))
    student = cursor.fetchone()

    if not student:
        print("Student not found")
        return

    _, old_name, old_cource, old_age, old_contact = student

    print("Press Enter to skip a field")

    name = input(f"New name ({old_name}): ") or old_name
    cource = input(f"New course ({old_cource}): ") or old_cource

    age_input = input(f"New age ({old_age}): ")
    age = int(age_input) if age_input else old_age

    contact_input = input(f"New contact ({old_contact}): ")
    contact = int(contact_input) if contact_input else old_contact

    cursor.execute(
        "UPDATE crud SET name=?, cource=?, age=?, contact=? WHERE id=?",
        (name, cource, age, contact, student_id)
    )
    connection.commit()
    print("Student updated")


def delete_student():
    student_id = int(input("Student ID to delete: "))
    cursor.execute("DELETE FROM crud WHERE id = ?", (student_id,))
    connection.commit()
    print("Student deleted")


# MAIN MENU -------------------------------
def main():
    while True:
        print("\n--- CRUD MENU ---")
        print("1. List students")
        print("2. Add student")
        print("3. Update student")
        print("4. Delete student")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            list_all_students()
        elif choice == "2":
            add_student()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid choice")

    connection.close()


# RUN APP ----------------
if __name__ == "__main__":
    main()