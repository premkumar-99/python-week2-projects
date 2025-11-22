"""
Library Book Inventory Manager (CLI)
- Book and Library classes
- Persist to JSON (books.json)
- Add, search by title/author, issue/return, simple reports
"""
import json
import os
from dataclasses import dataclass, asdict
from typing import List, Optional

DATA_FILE = "books.json"

@dataclass
class Book:
    id: str
    title: str
    author: str
    issued_to: Optional[str] = None  # student id or name

class Library:
    def __init__(self, data_file=DATA_FILE):
        self.data_file = data_file
        self.books: List[Book] = []
        self.load()

    def load(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                try:
                    data = json.load(f)
                    self.books = [Book(**b) for b in data]
                except json.JSONDecodeError:
                    self.books = []
        else:
            self.books = []

    def save(self):
        with open(self.data_file, "w") as f:
            json.dump([asdict(b) for b in self.books], f, indent=2)

    def add_book(self, book_id, title, author):
        if any(b.id == book_id for b in self.books):
            raise ValueError("Book ID already exists.")
        b = Book(id=book_id, title=title, author=author)
        self.books.append(b)
        self.save()
        return b

    def search(self, query):
        q = query.lower()
        results = [b for b in self.books if q in b.title.lower() or q in b.author.lower()]
        return results

    def issue_book(self, book_id, to_whom):
        for b in self.books:
            if b.id == book_id:
                if b.issued_to:
                    raise ValueError("Book already issued.")
                b.issued_to = to_whom
                self.save()
                return b
        raise ValueError("Book not found.")

    def return_book(self, book_id):
        for b in self.books:
            if b.id == book_id:
                if not b.issued_to:
                    raise ValueError("Book is not issued.")
                b.issued_to = None
                self.save()
                return b
        raise ValueError("Book not found.")

    def report(self):
        total = len(self.books)
        issued = sum(1 for b in self.books if b.issued_to)
        return {"total": total, "issued": issued}

def print_book(b: Book):
    status = f"Issued to {b.issued_to}" if b.issued_to else "Available"
    print(f"{b.id} | {b.title} | {b.author} | {status}")

def menu():
    lib = Library()
    while True:
        print("""
Library Manager
1) List all books
2) Add book
3) Search by title/author
4) Issue book
5) Return book
6) Report
7) Exit
""")
        choice = input("Choose: ").strip()
        if choice == "1":
            if not lib.books:
                print("No books.")
            for b in lib.books:
                print_book(b)
        elif choice == "2":
            bid = input("Book ID: ").strip()
            title = input("Title: ").strip()
            author = input("Author: ").strip()
            try:
                lib.add_book(bid, title, author)
                print("Added.")
            except ValueError as e:
                print("Error:", e)
        elif choice == "3":
            q = input("Search query: ").strip()
            res = lib.search(q)
            if not res:
                print("No matches.")
            for b in res:
                print_book(b)
        elif choice == "4":
            bid = input("Book ID to issue: ").strip()
            to = input("Issue to (name/id): ").strip()
            try:
                lib.issue_book(bid, to)
                print("Issued.")
            except ValueError as e:
                print("Error:", e)
        elif choice == "5":
            bid = input("Book ID to return: ").strip()
            try:
                lib.return_book(bid)
                print("Returned.")
            except ValueError as e:
                print("Error:", e)
        elif choice == "6":
            rpt = lib.report()
            print(f"Total books: {rpt['total']}, Issued: {rpt['issued']}")
        elif choice == "7":
            print("Bye.")
            break
        else:
            print("Invalid.")
if __name__ == '__main__':
    menu()
