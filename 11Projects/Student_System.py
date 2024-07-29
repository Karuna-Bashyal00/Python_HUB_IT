# Program to create Student Management System. Students data must be created, update, read and delete. Data must be saved in Json File.

import json

class Student:
    def __init__(self, student_id, name, age, grades):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grades = grades

    def update_info(self, name=None, age=None, grades=None):
        if name:
            self.name = name
        if age:
            self.age = age
        if grades:
            self.grades = grades

    def to_dict(self):
        return {
            'student_id': self.student_id,
            'name': self.name,
            'age': self.age,
            'grades': self.grades
        }

# Function to save data to file
def save_to_file(data, filename='students.json'):
    try:
        with open(filename, 'a') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"Error saving file: {e}")

# Function to load data from file
def load_from_file(filename='students.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error loading file: {e}")
        return {}

# Generator to iterate over student records
def student_generator(records):
    for student_id, student_data in records.items():
        yield Student(**student_data)

# Main functionality
def main():
    students = {}
    while True:
        print("\n1. Add Student")
        print("2. Update Student")
        print("3. View Students")
        print("4. Delete Student")
        print("5. Save and Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':  # Add Student
            student_id = input("Enter student ID: ")
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            grades = list(map(int, input("Enter grades separated by space: ").split()))
            students[student_id] = Student(student_id, name, age, grades).to_dict()
        
        elif choice == '2':  # Update Student
            student_id = input("Enter student ID to update: ")
            if student_id in students:
                name = input("Enter new name (leave blank to keep current): ")
                age = input("Enter new age (leave blank to keep current): ")
                grades = input("Enter new grades separated by space (leave blank to keep current): ")
                grades = list(map(int, grades.split())) if grades else None
                students[student_id] = Student(student_id, **students[student_id]).update_info(
                    name=name if name else None,
                    age=int(age) if age else None,
                    grades=grades
                ).to_dict()
            else:
                print("Student ID not found.")

        elif choice == '3':  # View Students
            if students:
                for student in student_generator(students):
                    print(f"ID: {student.student_id}, Name: {student.name}, Age: {student.age}, Grades: {student.grades}")
            else:
                print("No student records found.")

        elif choice == '4':  # Delete Student
            student_id = input("Enter student ID to delete: ")
            if student_id in students:
                del students[student_id]
                print("Student deleted.")
            else:
                print("Student ID not found.")

        elif choice == '5':  # Save and Exit
            save_to_file(students)
            print("Records saved. Exiting...")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()
