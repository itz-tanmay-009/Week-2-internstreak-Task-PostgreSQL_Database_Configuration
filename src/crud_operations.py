from database_connection import get_connection


def add_student(student_name, email, age):
    """Create a new student."""
    connection = get_connection()

    if connection is None:
        return

    cursor = None

    try:
        cursor = connection.cursor()

        query = """
            INSERT INTO students (student_name, email, age)
            VALUES (%s, %s, %s);
        """

        cursor.execute(query, (student_name, email, age))
        connection.commit()

        print("Student added successfully.")

    except Exception as error:
        connection.rollback()
        print(f"Error adding student: {error}")

    finally:
        if cursor:
            cursor.close()
        connection.close()


def view_students():
    """Read and display all students."""
    connection = get_connection()

    if connection is None:
        return

    cursor = None

    try:
        cursor = connection.cursor()

        query = """
            SELECT student_id, student_name, email, age
            FROM students
            ORDER BY student_id;
        """

        cursor.execute(query)
        students = cursor.fetchall()

        if not students:
            print("No students found.")
        else:
            print("\nStudent Records")
            print("-" * 60)

            for student in students:
                print(
                    f"ID: {student[0]} | "
                    f"Name: {student[1]} | "
                    f"Email: {student[2]} | "
                    f"Age: {student[3]}"
                )

    except Exception as error:
        print(f"Error viewing students: {error}")

    finally:
        if cursor:
            cursor.close()
        connection.close()


def update_student(student_id, student_name, email, age):
    """Update an existing student's details."""
    connection = get_connection()

    if connection is None:
        return

    cursor = None

    try:
        cursor = connection.cursor()

        query = """
            UPDATE students
            SET student_name = %s,
                email = %s,
                age = %s
            WHERE student_id = %s;
        """

        cursor.execute(
            query,
            (student_name, email, age, student_id)
        )

        connection.commit()

        if cursor.rowcount == 0:
            print("Student not found.")
        else:
            print("Student updated successfully.")

    except Exception as error:
        connection.rollback()
        print(f"Error updating student: {error}")

    finally:
        if cursor:
            cursor.close()
        connection.close()


def delete_student(student_id):
    """Delete a student using the student ID."""
    connection = get_connection()

    if connection is None:
        return

    cursor = None

    try:
        cursor = connection.cursor()

        query = """
            DELETE FROM students
            WHERE student_id = %s;
        """

        cursor.execute(query, (student_id,))
        connection.commit()

        if cursor.rowcount == 0:
            print("Student not found.")
        else:
            print("Student deleted successfully.")

    except Exception as error:
        connection.rollback()
        print(f"Error deleting student: {error}")

    finally:
        if cursor:
            cursor.close()
        connection.close()


if __name__ == "__main__":
    print("CRUD Operations Module")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    while True:
        choice = input("\nEnter your choice: ").strip()

        try:
            if choice == "1":
                name = input("Enter student name: ").strip()
                email = input("Enter student email: ").strip()
                age = int(input("Enter student age: ").strip())

                add_student(name, email, age)

            elif choice == "2":
                view_students()

            elif choice == "3":
                student_id = int(input("Enter student ID: ").strip())
                name = input("Enter new student name: ").strip()
                email = input("Enter new student email: ").strip()
                age = int(input("Enter new student age: ").strip())

                update_student(student_id, name, email, age)

            elif choice == "4":
                student_id = int(input("Enter student ID: ").strip())
                delete_student(student_id)

            elif choice == "5":
                print("Exiting program.")
                break

            else:
                print("Invalid choice. Please select 1 to 5.")

        except ValueError:
            print("Invalid input. Please enter the correct value.")

        except Exception as error:
            print(f"Unexpected error: {error}")