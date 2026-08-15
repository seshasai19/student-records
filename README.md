# Student Record Management System

A modern Django web application and REST API for managing student records, with support for filtering, CRUD operations, input validation, and responsive UI design.

## Features
- **Student Dashboard**: Clean, responsive dashboard with search and filter capabilities (Name, Class, Roll No, Age, Marks).
- **CRUD Operations**: Add new students, edit existing records, and delete records with confirmation prompts.
- **REST API**: Django REST Framework endpoints under `/api/students/` with search and ordering backends.
- **Validation**: Server-side and model validation for unique roll numbers, positive age, and marks constraints.

## Tech Stack
- **Backend**: Python 3, Django 5/6, Django REST Framework, Django Filter
- **Frontend**: HTML5, CSS3 (Vanilla CSS, Glassmorphism design system, Inter font)
- **Database**: SQLite3

## Getting Started

### 1. Prerequisites
Ensure Python 3.10+ is installed.

### 2. Installation & Setup
```bash
# Clone the repository
git clone https://github.com/seshasai19/student-records.git
cd student-records

# Install dependencies
pip install django djangorestframework django-filter

# Apply migrations
python manage.py migrate

# Run development server
python manage.py runserver
```

### 3. Accessing the Application
- Web Dashboard: `http://127.0.0.1:8000/`
- REST API: `http://127.0.0.1:8000/api/students/`

## Running Tests
```bash
python manage.py test
```
