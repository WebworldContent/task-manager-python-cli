# Task Manager CLI (Python)

A simple command-line interface (CLI) based task manager written in Python.  
Manage your tasks (to‑dos), mark them as done, delete them, and persist them between runs via a JSON file.

## Table of Contents

- [Features](#features)  
- [Requirements](#requirements)  
- [Installation](#installation)  
- [Usage](#usage)  
- [File Structure](#file-structure)  
- [Configuration & Data Storage](#configuration--data-storage)  
- [Contributing](#contributing)  
- [License](#license)  
- [Future Enhancements](#future-enhancements)  

## Features

- Add new tasks with title and (optional) description  
- View all tasks with status (pending / completed)  
- Mark tasks as completed  
- Delete tasks  
- Persist tasks in a JSON file so data remains between runs  

## Requirements

- Python 3.6+  
- Standard library (no external dependencies required as of now)  

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/WebworldContent/task-manager-python-cli.git
   cd task-manager-python-cli
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. (Optional) Install dependencies (if you add any later).  
   For now, no external modules are required.

## Usage

Run the main app script:

```bash
python app.py
```

Once running, you will see a prompt or menu to:

- List tasks  
- Add a task  
- Mark a task as completed  
- Delete a task  
- Exit  

### Example Session

```
Welcome to Task Manager!

1. List tasks  
2. Add task  
3. Mark task as done  
4. Delete task  
5. Exit

Choose an option: 2  
Enter title: Finish report  
Enter description (optional): Complete the monthly finances  

Task added.

Choose an option: 1  
[ ] 1. Finish report — Complete the monthly finances  

Choose an option: 3  
Enter task ID to mark done: 1  

Task marked as done.

Choose an option: 1  
[x] 1. Finish report — Complete the monthly finances  

Choose an option: 5  
Goodbye!
```

## File Structure

```
.
├── app.py
├── user_data.json
└── README.md
```

- `app.py` — the main Python script implementing the CLI  
- `user_data.json` — the JSON file used to store tasks (auto‑generated / modified)  
- `README.md` — this documentation  

## Configuration & Data Storage

- Tasks are stored in **user_data.json** in JSON format.  
- If the `user_data.json` file does not exist, the script should create it automatically.  
- Each task record typically includes:
  - `id` (unique integer)  
  - `title` (string)  
  - `description` (optional string)  
  - `status` (e.g. `"pending"` or `"done"`)  

## Contributing

Contributions are welcome! Here are some ways you could help:

- Add command-line argument parsing (e.g. via `argparse`)  
- Add support for due dates, priorities, categories  
- Add task editing (change title / description)  
- Add filtering / sorting (by status, date, etc.)  
- Add tests (unit tests)  
- Improve error handling and user prompts  
- Add more persistent storage options (SQLite, YAML, etc.)

If you plan to contribute:

1. Fork the repo  
2. Create a branch (e.g. `feature/new-feature`)  
3. Commit your changes  
4. Submit a pull request  

## License

Specify your license here (e.g. MIT License, Apache 2.0, etc.).  

*Example:*  
```
MIT License

Copyright (c) 2025 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy …
```

## Future Enhancements

- Add priority levels and deadlines  
- Allow editing of existing tasks  
- Use a more robust storage backend (e.g. SQLite)  
- Add synchronization or backup options  
- Improve the CLI interface (colorful output, better menus)  
- Add search or filter commands  
- Add undo / redo support  

---

Thanks for checking out **Task Manager CLI (Python)**!  
Feel free to use, modify, or extend it as much as you like.  
If you add features, don’t forget to update this README accordingly.  
