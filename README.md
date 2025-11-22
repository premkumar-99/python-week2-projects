📘 Python Week-2 Projects
Student Management System · Library Manager · File Organizer
A set of beginner-friendly but industry-aligned Python projects covering OOP, file handling, JSON data storage, CLI workflows, and automation scripting.
These tasks are part of my ongoing commitment to improving my Python fundamentals and building real, usable tools.
🚀 Projects Included
1️⃣ Student Management System
A command-line tool to manage student records using Python classes & JSON storage.
Features
Add, update, delete students
Search student by ID
List all students in a formatted table
JSON-based data persistence
Input validation (unique IDs)
Tech Used
dataclasses
JSON read/write
CLI menus
📄 File: student_management_system.py
📁 Data: students.json
Run:
python student_management_system.py
2️⃣ Library Book Inventory Manager
A simple library inventory system to track books, issues/returns, and availability.
Features
Add books with ID, Title, Author
Search by title or author
Issue/Return books
Generate basic availability reports
Persistent storage with JSON
Tech Used
Object-oriented design (Book, Library)
JSON persistence
CLI interface
📄 File: library_manager.py
📁 Data: books.json
Run:
python library_manager.py
3️⃣ File Organizer Script
A practical automation script that organizes files into folders based on their extensions.
Features
Auto-categorizes files (images, docs, videos, code, etc.)
Handles name conflicts safely
--dry-run mode (preview actions)
Logs all moves to file_organizer.log
Tech Used
os, shutil
Logging
Categorization logic
Automation script design
📄 File: file_organizer.py
Run:
python file_organizer.py <folder-path>
python file_organizer.py <folder-path> --dry-run
🧰 Folder Structure
│── student_management_system.py
│── library_manager.py
│── file_organizer.py
│── students.json
│── books.json
│── .gitignore
│── README.md
🎯 What I Learned (For Recruiters)
Building CLI tools with clean, modular design
Working with classes, objects, and structured data
Persisting data across program runs (JSON)
Writing automation scripts for real use cases
Handling errors, validations, and edge cases
Clean coding practices & GitHub repo structure
