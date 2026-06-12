import json
import os
from models import User, Project, Task

DATA_DIR = "data"
USERS_FILE = os.path.join(DATA_DIR, "users.json")
PROJECTS_FILE = os.path.join(DATA_DIR, "projects.json")
TASKS_FILE = os.path.join(DATA_DIR, "tasks.json")

def ensure_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def save_all():
    ensure_data_dir()
    
    users_data = {uid: user.to_dict() for uid, user in User.all_users.items()}
    with open(USERS_FILE, "w") as f:
        json.dump(users_data, f, indent=2)
    
    projects_data = {pid: project.to_dict() for pid, project in Project.all_projects.items()}
    with open(PROJECTS_FILE, "w") as f:
        json.dump(projects_data, f, indent=2)
    
    tasks_data = {tid: task.to_dict() for tid, task in Task.all_tasks.items()}
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks_data, f, indent=2)

def load_all():
    ensure_data_dir()
    
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, "r") as f:
                users_data = json.load(f)
                for uid, data in users_data.items():
                    if uid not in User.all_users:
                        User.from_dict(data)
        except Exception:
            pass
    
    if os.path.exists(PROJECTS_FILE):
        try:
            with open(PROJECTS_FILE, "r") as f:
                projects_data = json.load(f)
                for pid, data in projects_data.items():
                    if pid not in Project.all_projects:
                        Project.from_dict(data)
        except Exception:
            pass
    
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, "r") as f:
                tasks_data = json.load(f)
                for tid, data in tasks_data.items():
                    if tid not in Task.all_tasks:
                        Task.from_dict(data)
        except Exception:
            pass