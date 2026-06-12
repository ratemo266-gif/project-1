# project-1


# Project Management CLI Tool

A command-line application for managing users, projects, and tasks with persistent JSON storage. Built for team collaboration and project tracking.

## Author
Douglas karanja wachira 

## Date
June 2026




---

## Table of Contents
1. [Setup Instructions](#setup-instructions)
2. [How to Run](#how-to-run)
3. [Example Data](#example-data)
4. [All Commands](#all-commands)
5. [Command Examples](#command-examples)
6. [Features](#features)
7. [File Structure](#file-structure)
8. [Data Relationships](#data-relationships)



---

## Setup Instructions

### Prerequisites
- Python 3.6 or higher installed on your computer
- pip package manager (comes with Python)

### Step 1: Download the Files
Create a folder called `project_manager` and save all these files inside it:
- `main.py`
- `cli.py`
- `models.py`
- `storage.py`
- `requirements.txt`

### Step 2: Install Dependencies
Open your terminal or command prompt, navigate to the project folder, and run:

```bash
cd project_manager
pip install -r requirements.txt

## How to Run
First Time Running
The first time you run the program, it automatically creates example data with:

6 users (including an admin)

5 projects

15 tasks

You'll see a message showing what was created.

Login
The system uses simple name-based login (no passwords for simplicity):

## All Commands 


Command	Description	Required Role
login <name>	Login as a user	None
logout	Logout current user	None
add-user <name> <email> <role>	Create a new user	Admin
list-users	Show all users	Admin
add-project <title> <desc> <due>	Create a new project	Any logged in user
list-projects	Show all projects	Any logged in user
assign-project <user> <project_id>	Assign project to user	Admin
add-task <project_id> <title>	Add task to project	Any logged in user
list-tasks <project_id>	Show tasks in a project	Any logged in user
complete-task <task_id>	Mark a task as complete	Any logged in user
my-projects	Show projects assigned to you	Any logged in user
my-tasks	Show tasks assigned to you	Any logged in user
user-projects <name>	Show projects for a specific user	Any logged in user
help	Show help menu	None
exit	Quit the program	None


# file structure

project_manager/
│
├── main.py              # Entry point - starts the CLI application
├── cli.py               # Command handling - all user interaction logic
├── models.py            # Data models - User, Project, Task classes
├── storage.py           # File I/O - saving and loading JSON data
├── requirements.txt     # Dependencies - tabulate package
├── README.md            # This file - documentation
│
└── data/                # Created automatically on first run
    ├── users.json       # Stores all user data
    ├── projects.json    # Stores all project data
    └── tasks.json       # Stores all task data

Features
  ## Core Features
User Management: Create users with different roles (admin, manager, contributor)

Project Management: Create projects with title, description, due date

Task Management: Add tasks to projects, assign to users, mark complete

Access Control: Admin-only commands for sensitive operations

Persistent Storage: All data saved to JSON files automatically

## Data Relationships
One-to-Many: One user can own or be assigned to multiple projects

One-to-Many: One project can contain multiple tasks

Many-to-One: Multiple tasks can be assigned to one user

 ## Technical Features
Object-oriented design with three main classes (User, Project, Task)

Property decorators for data validation (email format, name length)

Class-level dictionaries for tracking all objects

JSON file I/O with error handling

External package (tabulate) for formatted output

Modular code structure across 4 Python files

## Display Features
Color-coded command responses (using terminal colors)

Formatted tables with borders and headers

Clear error and success messages

Context-aware command prompt (shows current user)












# visual representation
User (Sarah Johnson)
  │
  ├── Projects (assigned to her)
  │     ├── Company Website Redesign (Project ID: a1b2c3)
  │     │       ├── Task: Design homepage (assigned to Alex)
  │     │       ├── Task: Responsive navigation (assigned to Alex)
  │     │       └── Task: Analytics tracking (assigned to David)
  │     │
  │     └── Mobile App Development (Project ID: d4e5f6)
  │             ├── Task: User auth (assigned to Alex)
  │             └── Task: Push notifications (assigned to Emma)
  │
  └── Projects (she owns)
        ├── Security Audit (Project ID: m3n4o5)
        └── (same projects as above - she owns them too)