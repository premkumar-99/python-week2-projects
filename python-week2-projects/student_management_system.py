"""
Student Management System (CLI)
- Student class and StudentManager for operations
- Persist to JSON file (students.json)
- Add / update / delete / list students with simple validation (unique ID)
"""
import json
import os
from dataclasses import dataclass, asdict
from typing import List, Optional

DATA_FILE = "students.json"

@dataclass
class Student:
    id: str
    name: str
    grade: str

class StudentManager:
    def __init__(self, data_file=DATA_FILE):
        self.data_file = data_file
        self.students: List[Student] = []
        self.load()

    def load(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                try:
                    data = json.load(f)
                    self.students = [Student(**s) for s in data]
                except json.JSONDecodeError:
                    self.students = []
        else:
            self.students = []

    def save(self):
        with open(self.data_file, "w") as f:
            json.dump([asdict(s) for s in self.students], f, indent=2)

    def list_students(self):
        if not self.students:
            print("No students found.")
            return
        print("{:<10} {:<25} {:<10}".format("ID", "Name", "Grade"))
        print("-"*50)
        for s in self.students:
            print("{:<10} {:<25} {:<10}".format(s.id, s.name, s.grade))

    def find(self, student_id) -> Optional[Student]:
        for s in self.students:
            if s.id == student_id:
                return s
        return None

    def add_student(self, student_id, name, grade):
        if self.find(student_id):
            raise ValueError("Student ID already exists.")
        s = Student(id=student_id, name=name, grade=grade)
        self.students.append(s)
        self.save()
        return s

    def update_student(self, student_id, name=None, grade=None):
        s = self.find(student_id)
        if not s:
            raise ValueError("Student not found.")
        if name:
            s.name = name
        if grade:
            s.grade = grade
        self.save()
        return s

    def delete_student(self, student_id):
        s = self.find(student_id)
        if not s:
            raise ValueError("Student not found.")
        self.students = [x for x in self.students if x.id != student_id]
        self.save()
        return True

def menu():
    mgr = StudentManager()
    while True:
        print("""
Student Management
1) List students
2) Add student
3) Update student
4) Delete student
5) Exit
""")
        choice = input("Choose: ").strip()
        if choice == "1":
            mgr.list_students()
        elif choice == "2":
            sid = input("ID: ").strip()
            name = input("Name: ").strip()
            grade = input("Grade: ").strip()
            try:
                mgr.add_student(sid, name, grade)
                print("Added.")
            except ValueError as e:
                print("Error:", e)
        elif choice == "3":
            sid = input("ID to update: ").strip()
            name = input("New name (leave blank to keep): ").strip() or None
            grade = input("New grade (leave blank to keep): ").strip() or None
            try:
                mgr.update_student(sid, name, grade)
                print("Updated.")
            except ValueError as e:
                print("Error:", e)
        elif choice == "4":
            sid = input("ID to delete: ").strip()
            try:
                mgr.delete_student(sid)
                print("Deleted.")
            except ValueError as e:
                print("Error:", e)
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    menu()
