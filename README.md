# Task Manager CLI (Python)

A command-line interface (CLI) based **Task Manager with User Authentication**, written in Python.  
Users must **register and login** before managing their own tasks.  
All data is stored locally in a single JSON file — no database or sessions required.

## Features

- **User Authorization**
  - Register with a unique email and password
  - Login with existing credentials
  - Passwords stored securely as SHA-256 hashes
- **Task Management**
  - Add new tasks with title/description
  - View tasks (pending / completed)
  - Mark tasks as completed
  - Delete tasks
- **Data Persistence**
  - All users and tasks stored in one JSON file
  - Each user has an isolated task list

## Requirements

- Python 3.6+  
- Standard library only (no external dependencies)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/WebworldContent/task-manager-python-cli.git
   cd task-manager-python-cli
   ```

2. (Optional) Create a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Run the application:

   ```bash
   python app.py
   ```

## Usage

When you start the program:

```
Welcome to Task Manager CLI

1. Register
2. Login
3. Exit
```

- **Register**: Create a new account (email + password, stored hashed)  
- **Login**: Access your personal task list  
- Once logged in, you will see task management options:

```
--- Task Manager ---
1. List tasks
2. Add task
3. Mark task as done
4. Delete task
5. Logout
```

### Example

```
Choose an option: 1
Enter email: test@gmail.com
Enter password: ****
User registered successfully.

Choose an option: 2
Enter email: test@gmail.com
Enter password: ****
Login successful!

--- Task Manager ---
1. List tasks
2. Add task
3. Mark task as done
4. Delete task
5. Logout
```

## Data Storage

All data is stored in **users.json**.  

Each record represents a user and contains:
- `email` (string, unique identifier for login)  
- `password` (SHA-256 hashed string)  
- `task` (optional list of task objects)  

### Example Structure

```json
[
  {
    "email": "test@gmail.com",
    "password": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"
  },
  {
    "email": "test2@gmail.com",
    "password": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
    "task": [
      {
        "id": 0,
        "task": "take grinder to repair",
        "status": "pending"
      }
    ]
  }
]
```

- Passwords are securely stored as SHA-256 hashes.  
- Each user can have zero or more tasks.  
- Each task contains:
  - `id` → numeric ID unique per user  
  - `task` → the task description  
  - `status` → `"pending"` or `"done"`  

## File Structure

```
.
├── app.py           # Main application logic
├── users.json       # Stores all users + tasks
└── README.md        # Documentation
```

## Contributing

Possible improvements:
- Use stronger password hashing (`bcrypt`) instead of raw SHA-256
- Add task editing support
- Add filtering and sorting (by date, priority, status)
- Replace JSON storage with SQLite for scalability

Contributions are welcome!

## License

MIT License (or specify your license here).
