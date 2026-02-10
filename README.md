# Task Tracker CLI

A simple command-line task tracking application that helps you manage your tasks with different statuses. Tasks are stored in a JSON file for persistence.

## Features

- Add new tasks with auto-incrementing IDs
- Update task descriptions
- Delete tasks
- Mark tasks with different statuses
- List all tasks or filter by status
- Automatic timestamp tracking (created and updated)

## Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd <repo-name>
```

2. Ensure you have Python 3.10+ installed (uses `match` statement)

## Usage

### Add a Task

Add a new task with a description:
```bash
python task_tracker.py add "Buy groceries"
```

Output: `Added item with ID: 1`

### List All Tasks

Display all tasks:
```bash
python task_tracker.py list
```

### List Tasks by Status

Filter tasks by their status:
```bash
python task_tracker.py list in-progress
python task_tracker.py list done
python task_tracker.py list todo
```

### Update a Task Description

Update the description of an existing task:
```bash
python task_tracker.py update 1 "Buy groceries and cook dinner"
```

### Delete a Task

Remove a task by ID:
```bash
python task_tracker.py delete 1
```

### Update Task Status

Change the status of a task using the `mark-<status>` command:
```bash
python task_tracker.py mark-done 1
python task_tracker.py mark-in-progress 2
python task_tracker.py mark-todo 3
```

## Data Structure

Tasks are stored in a `data` file as JSON with the following structure:
```json
[
  {
    "id": 1,
    "description": "Buy groceries",
    "status": "in-progress",
    "createdAt": "2024-02-10 14:30:00.123456",
    "updatedAt": "2024-02-10 14:30:00.123456"
  }
]
```

## Task Statuses

- `todo` - Task is pending
- `in-progress` - Task is currently being worked on
- `done` - Task is completed

## Requirements

- Python 3.10 or higher
- No external dependencies (uses only standard library)

## Project Structure
```
.
├── task_tracker.py    # Main application file
├── data               # JSON file storing tasks (auto-created)
└── README.md          # This file
```

## Error Handling

The application handles common errors gracefully:

- Missing or corrupted data file
- Invalid JSON format
- File not found scenarios

## Example Workflow
```bash
# Add some tasks
python task_tracker.py add "Write documentation"
python task_tracker.py add "Review pull requests"
python task_tracker.py add "Deploy to production"

# List all tasks
python task_tracker.py list

# Mark a task as in-progress
python task_tracker.py mark-in-progress 1

# Update task description
python task_tracker.py update 1 "Write comprehensive documentation"

# Mark as done
python task_tracker.py mark-done 1

# List only done tasks
python task_tracker.py list done

# Delete a task
python task_tracker.py delete 3
```

## Contributing

Feel free to submit issues or pull requests to improve this project.
