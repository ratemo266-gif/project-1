import uuid

class User:
    all_users = {}
    
    def __init__(self, name, email, role="contributor"):
        self._name = name
        self._email = email
        self.role = role
        self.user_id = str(uuid.uuid4())[:6]
        self.projects = []
        User.all_users[self.user_id] = self
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if len(value) > 0:
            self._name = value
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if "@" in value and "." in value:
            self._email = value
    
    def add_project(self, project_id):
        if project_id not in self.projects:
            self.projects.append(project_id)
    
    def to_dict(self):
        return {
            "name": self._name,
            "email": self._email,
            "role": self.role,
            "user_id": self.user_id,
            "projects": self.projects
        }
    
    @classmethod
    def from_dict(cls, data):
        user = cls(data["name"], data["email"], data["role"])
        user.user_id = data["user_id"]
        user.projects = data["projects"]
        return user
    
    def __str__(self):
        return f"User: {self._name} ({self.role})"


class Project:
    all_projects = {}
    
    def __init__(self, title, description, due_date, owner_id):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.owner_id = owner_id
        self.project_id = str(uuid.uuid4())[:6]
        self.tasks = []
        Project.all_projects[self.project_id] = self
    
    def add_task(self, task):
        self.tasks.append(task)
    
    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "owner_id": self.owner_id,
            "project_id": self.project_id,
            "tasks": [t.to_dict() for t in self.tasks]
        }
    
    @classmethod
    def from_dict(cls, data):
        project = cls(data["title"], data["description"], data["due_date"], data["owner_id"])
        project.project_id = data["project_id"]
        project.tasks = [Task.from_dict(t) for t in data.get("tasks", [])]
        return project
    
    def __str__(self):
        return f"Project: {self.title} (Due: {self.due_date})"


class Task:
    all_tasks = {}
    
    def __init__(self, title, status="pending", assigned_to=None):
        self.title = title
        self.status = status
        self.assigned_to = assigned_to
        self.task_id = str(uuid.uuid4())[:6]
        Task.all_tasks[self.task_id] = self
    
    def complete(self):
        self.status = "completed"
    
    def to_dict(self):
        return {
            "title": self.title,
            "status": self.status,
            "assigned_to": self.assigned_to,
            "task_id": self.task_id
        }
    
    @classmethod
    def from_dict(cls, data):
        task = cls(data["title"], data["status"], data["assigned_to"])
        task.task_id = data["task_id"]
        return task
    
    def __str__(self):
        return f"Task: {self.title} [{self.status}]"