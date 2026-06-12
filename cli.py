
from models import User, Project, Task
from storage import save_all, load_all
# Prefer the real tabulate package; if unavailable provide a minimal fallback.
try:
    from tabulate import tabulate  # type: ignore
except Exception:
    def tabulate(table, headers=None):
        # Minimal fallback: simple column separator, suitable for small CLI output
        lines = []
        if headers:
            lines.append(" | ".join(headers))
            lines.append("-" * len(lines[0]))
        for row in table:
            lines.append(" | ".join(str(c) for c in row))
        return "\n".join(lines)

class CLI:
    def __init__(self):
        load_all()
        self.current_user = None
        self.load_example_data()
    
    def load_example_data(self):
        print("Welcome to Project Manager CLI")
        print("Type 'help' for commands, 'exit' to quit")
        
        
        sarah = User("Sarah Johnson", "sarah.johnson@techcorp.com", "admin")
        mike = User("Mike Chen", "mike.chen@techcorp.com", "manager")
        emma = User("Emma Rodriguez", "emma.rodriguez@techcorp.com", "manager")
        alex = User("Alex Kim", "alex.kim@techcorp.com", "contributor")
        lisa = User("Lisa Wong", "lisa.wong@techcorp.com", "contributor")
        david = User("David Patel", "david.patel@techcorp.com", "contributor")
        
        website = Project("Company Website Redesign", "Complete overhaul of company website with new branding", "2025-03-15", sarah.user_id)
        mobile_app = Project("Mobile App Development", "iOS and Android app for customer portal", "2025-05-01", sarah.user_id)
        database = Project("Database Migration", "Move from on-premise to cloud database", "2025-02-28", mike.user_id)
        api = Project("REST API Development", "Build public API for third-party integrations", "2025-04-20", emma.user_id)
        security = Project("Security Audit", "Annual security compliance and penetration testing", "2025-01-30", sarah.user_id)
        
        sarah.add_project(website.project_id)
        sarah.add_project(mobile_app.project_id)
        sarah.add_project(security.project_id)
        mike.add_project(database.project_id)
        mike.add_project(api.project_id)
        emma.add_project(api.project_id)
        emma.add_project(website.project_id)
        alex.add_project(website.project_id)
        alex.add_project(mobile_app.project_id)
        lisa.add_project(database.project_id)
        david.add_project(api.project_id)
        
        task1 = Task("Design homepage mockups", "pending", alex.user_id)
        task2 = Task("Create responsive navigation", "pending", alex.user_id)
        task3 = Task("Write content for about page", "completed", lisa.user_id)
        task4 = Task("Set up analytics tracking", "pending", david.user_id)
        website.add_task(task1)
        website.add_task(task2)
        website.add_task(task3)
        website.add_task(task4)
        
        task5 = Task("User authentication system", "in_progress", alex.user_id)
        task6 = Task("Push notifications setup", "pending", emma.user_id)
        task7 = Task("App store submission", "pending", sarah.user_id)
        mobile_app.add_task(task5)
        mobile_app.add_task(task6)
        mobile_app.add_task(task7)
        
        task8 = Task("Backup all data", "completed", mike.user_id)
        task9 = Task("Test migration script", "pending", lisa.user_id)
        task10 = Task("Update connection strings", "pending", mike.user_id)
        database.add_task(task8)
        database.add_task(task9)
        database.add_task(task10)
        
        task11 = Task("Design API endpoints", "completed", emma.user_id)
        task12 = Task("Write API documentation", "pending", david.user_id)
        task13 = Task("Rate limiting implementation", "pending", mike.user_id)
        api.add_task(task11)
        api.add_task(task12)
        api.add_task(task13)
        
        task14 = Task("Vulnerability scanning", "completed", sarah.user_id)
        task15 = Task("Penetration testing", "pending", david.user_id)
        security.add_task(task14)
        security.add_task(task15)
        
        save_all()
        
        print("Example data loaded successfully!")
        print(f"Created {len(User.all_users)} users")
        print(f"Created {len(Project.all_projects)} projects")
        print(f"Created {len(Task.all_tasks)} tasks")
        print("\nAvailable users:")
        for user in User.all_users.values():
            print(f"  - {user.name} ({user.email}) - Role: {user.role}")
        print("\nTip: Try 'login Sarah Johnson' to start as admin\n")
    
    def run(self):
        print("Welcome to Project Manager CLI")
        print("Type 'help' for commands, 'exit' to quit")
        
        while True:
            if self.current_user:
                prompt = f"{self.current_user.name}> "
            else:
                prompt = "(none)> "
            
            try:
                cmd = input(prompt).strip()
                if cmd == "exit":
                    print("Goodbye!")
                    break
                elif cmd == "help":
                    self.show_help()
                elif cmd.startswith("login"):
                    self.login(cmd)
                elif cmd == "logout":
                    self.logout()
                elif cmd.startswith("add-user"):
                    self.add_user(cmd)
                elif cmd == "list-users":
                    self.list_users()
                elif cmd.startswith("add-project"):
                    self.add_project(cmd)
                elif cmd == "list-projects":
                    self.list_projects()
                elif cmd.startswith("assign-project"):
                    self.assign_project(cmd)
                elif cmd.startswith("add-task"):
                    self.add_task(cmd)
                elif cmd.startswith("list-tasks"):
                    self.list_tasks(cmd)
                elif cmd.startswith("complete-task"):
                    self.complete_task(cmd)
                elif cmd == "my-projects":
                    self.my_projects()
                elif cmd == "my-tasks":
                    self.my_tasks()
                elif cmd.startswith("user-projects"):
                    self.user_projects(cmd)
                else:
                    print("Unknown command. Type 'help'")
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")
    
    def show_help(self):
        print("\n=== COMMANDS ===")
        print("login <name>                    - Login as user")
        print("logout                          - Logout")
        print("add-user <name> <email> <role>  - Add new user (any logged in user)")
        print("list-users                      - Show all users (any logged in user)")
        print("add-project <title> <desc> <due> - Create project")
        print("list-projects                   - Show all projects")
        print("assign-project <user> <proj_id> - Assign project to user (any logged in user)")
        print("add-task <proj_id> <title>      - Add task to project")
        print("list-tasks <proj_id>            - Show tasks in project")
        print("complete-task <task_id>         - Mark task complete")
        print("my-projects                     - Show projects assigned to you")
        print("my-tasks                        - Show tasks assigned to you")
        print("user-projects <name>            - Show user's projects")
        print("help                            - This menu")
        print("exit                            - Quit\n")
    
    def login(self, cmd):
        parts = cmd.split()
        if len(parts) != 2:
            print("Usage: login <name>")
            return
        name = parts[1]
        for user in User.all_users.values():
            if user.name == name:
                self.current_user = user
                print(f"Logged in as {name} ({user.role})")
                return
        print(f"User '{name}' not found")
    
    def logout(self):
        self.current_user = None
        print("Logged out")
    
    def add_user(self, cmd):
        # REMOVED: if not self.current_user or self.current_user.role != "admin":
        if not self.current_user:
            print("Login required")
            return
        parts = cmd.split()
        if len(parts) != 4:
            print("Usage: add-user <name> <email> <role>")
            return
        name, email, role = parts[1], parts[2], parts[3]
        if role not in ["admin", "manager", "contributor"]:
            print("Role must be admin/manager/contributor")
            return
        for user in User.all_users.values():
            if user.name == name:
                print("User already exists")
                return
        user = User(name, email, role)
        save_all()
        print(f"User '{name}' created with ID: {user.user_id}")
    
    def list_users(self):
        # REMOVED: if not self.current_user or self.current_user.role != "admin":
        if not self.current_user:
            print("Login required")
            return
        if not User.all_users:
            print("No users found")
            return
        table = []
        for user in User.all_users.values():
            table.append([user.name, user.email, user.role, user.user_id, len(user.projects)])
        print(tabulate(table, headers=["Name", "Email", "Role", "ID", "Projects"]))
    
    def add_project(self, cmd):
        if not self.current_user:
            print("Login required")
            return
        parts = cmd.split(maxsplit=3)
        if len(parts) < 4:
            print("Usage: add-project <title> <description> <due_date>")
            return
        title = parts[1]
        description = parts[2]
        due_date = parts[3]
        project = Project(title, description, due_date, self.current_user.user_id)
        self.current_user.add_project(project.project_id)
        save_all()
        print(f"Project '{title}' created with ID: {project.project_id}")
    
    def list_projects(self):
        if not Project.all_projects:
            print("No projects found")
            return
        table = []
        for project in Project.all_projects.values():
            owner = User.all_users.get(project.owner_id)
            owner_name = owner.name if owner else "Unknown"
            task_count = len(project.tasks)
            completed = sum(1 for t in project.tasks if t.status == "completed")
            table.append([project.title, owner_name, task_count, completed, project.due_date, project.project_id])
        print(tabulate(table, headers=["Title", "Owner", "Tasks", "Done", "Due", "ID"]))
    
    def assign_project(self, cmd):
        # REMOVED: if not self.current_user or self.current_user.role != "admin":
        if not self.current_user:
            print("Login required")
            return
        parts = cmd.split()
        if len(parts) != 3:
            print("Usage: assign-project <username> <project_id>")
            return
        username = parts[1]
        project_id = parts[2]
        user = None
        for u in User.all_users.values():
            if u.name == username:
                user = u
                break
        if not user:
            print(f"User '{username}' not found")
            return
        if project_id not in Project.all_projects:
            print(f"Project '{project_id}' not found")
            return
        user.add_project(project_id)
        save_all()
        print(f"Project assigned to '{username}'")
    
    def add_task(self, cmd):
        if not self.current_user:
            print("Login required")
            return
        parts = cmd.split(maxsplit=2)
        if len(parts) < 3:
            print("Usage: add-task <project_id> <task_title>")
            return
        project_id = parts[1]
        title = parts[2]
        if project_id not in Project.all_projects:
            print(f"Project '{project_id}' not found")
            return
        project = Project.all_projects[project_id]
        task = Task(title, "pending", self.current_user.user_id)
        project.add_task(task)
        save_all()
        print(f"Task '{title}' added with ID: {task.task_id}")
    
    def list_tasks(self, cmd):
        parts = cmd.split()
        if len(parts) != 2:
            print("Usage: list-tasks <project_id>")
            return
        project_id = parts[1]
        if project_id not in Project.all_projects:
            print(f"Project '{project_id}' not found")
            return
        project = Project.all_projects[project_id]
        if not project.tasks:
            print("No tasks in this project")
            return
        table = []
        for task in project.tasks:
            assignee = User.all_users.get(task.assigned_to) if task.assigned_to else None
            assignee_name = assignee.name if assignee else "Unassigned"
            table.append([task.task_id, task.title, task.status, assignee_name])
        print(tabulate(table, headers=["ID", "Title", "Status", "Assignee"]))
    
    def complete_task(self, cmd):
        if not self.current_user:
            print("Login required")
            return
        parts = cmd.split()
        if len(parts) != 2:
            print("Usage: complete-task <task_id>")
            return
        task_id = parts[1]
        for project in Project.all_projects.values():
            for task in project.tasks:
                if task.task_id == task_id:
                    task.complete()
                    save_all()
                    print(f"Task '{task.title}' completed")
                    return
        print(f"Task '{task_id}' not found")
    
    def my_projects(self):
        if not self.current_user:
            print("Login required")
            return
        user_projects = []
        for pid in self.current_user.projects:
            if pid in Project.all_projects:
                user_projects.append(Project.all_projects[pid])
        if not user_projects:
            print("No projects assigned to you")
            return
        table = []
        for project in user_projects:
            task_count = len(project.tasks)
            completed = sum(1 for t in project.tasks if t.status == "completed")
            table.append([project.title, project.description[:30], task_count, completed, project.due_date, project.project_id])
        print(tabulate(table, headers=["Title", "Description", "Tasks", "Done", "Due", "ID"]))
    
    def my_tasks(self):
        if not self.current_user:
            print("Login required")
            return
        my_tasks = []
        for project in Project.all_projects.values():
            for task in project.tasks:
                if task.assigned_to == self.current_user.user_id:
                    my_tasks.append((project.title, task))
        if not my_tasks:
            print("No tasks assigned to you")
            return
        table = []
        for project_name, task in my_tasks:
            table.append([task.task_id, project_name, task.title, task.status])
        print(tabulate(table, headers=["Task ID", "Project", "Title", "Status"]))
    
    def user_projects(self, cmd):
        parts = cmd.split()
        if len(parts) != 2:
            print("Usage: user-projects <username>")
            return
        username = parts[1]
        user = None
        for u in User.all_users.values():
            if u.name == username:
                user = u
                break
        if not user:
            print(f"User '{username}' not found")
            return
        user_projects = []
        for pid in user.projects:
            if pid in Project.all_projects:
                user_projects.append(Project.all_projects[pid])
        if not user_projects:
            print(f"No projects for '{username}'")
            return
        table = []
        for project in user_projects:
            table.append([project.title, project.description[:30], project.due_date, project.project_id])
        print(tabulate(table, headers=["Title", "Description", "Due", "ID"]))
        print(f"Total: {len(user_projects)} projects")