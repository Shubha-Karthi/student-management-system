import json
import os
FILE_NAME = "students.json"

class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "marks": self.marks
        }

class StudentManagementSystem:
    def __init__(self):
        self.students = self.load_data()

    def load_data(self):
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        return []

    def save_data(self):
        with open(FILE_NAME, "w") as file:
            json.dump(self.students, file, indent=4)

    def add_student(self):
        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")

        try:
            marks = float(input("Enter Marks: "))
        except ValueError:
            print("Invalid marks!")
            return

        student = Student(student_id, name, marks)

        self.students.append(student.to_dict())
        self.save_data()

        print("Student added successfully.")

    def view_students(self):
        if not self.students:
            print("No students found.")
            return

        for student in self.students:
            print(
                f"ID: {student['student_id']} | "
                f"Name: {student['name']} | "
                f"Marks: {student['marks']}"
            )

    def search_student(self):
        search_id = input("Enter Student ID to search: ")

        for student in self.students:
            if student["student_id"] == search_id:
                print("Student Found:")
                print(student)
                return

        print("Student not found.")

    def update_marks(self):
        search_id = input("Enter Student ID to update: ")

        for student in self.students:
            if student["student_id"] == search_id:
                try:
                    new_marks = float(input("Enter new marks: "))
                except ValueError:
                    print("Invalid marks!")
                    return

                student["marks"] = new_marks
                self.save_data()

                print("Marks updated successfully.")
                return

        print("Student not found.")

    def delete_student(self):
        search_id = input("Enter Student ID to delete: ")

        for student in self.students:
            if student["student_id"] == search_id:
                self.students.remove(student)
                self.save_data()

                print("Student deleted successfully.")
                return

        print("Student not found.")

    def find_topper(self):
        if not self.students:
            print("No students found.")
            return

        topper = max(self.students, key=lambda x: x["marks"])

        print("\nTopper Details:")
        print(
            f"ID: {topper['student_id']} | "
            f"Name: {topper['name']} | "
            f"Marks: {topper['marks']}"
        )

def main():
    system = StudentManagementSystem()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Find Topper")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            system.add_student()

        elif choice == "2":
            system.view_students()

        elif choice == "3":
            system.search_student()

        elif choice == "4":
            system.update_marks()

        elif choice == "5":
            system.delete_student()

        elif choice == "6":
            system.find_topper()

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()