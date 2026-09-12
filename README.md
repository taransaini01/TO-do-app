# CLI To-Do List (SQLite Edition)

A simple command-line to-do list application built in Python, using **SQLite** for persistent storage. Tasks are saved to a local database file, so they persist between runs — unlike a plain in-memory list.

This is an upgraded version of an earlier CLI to-do app that originally stored tasks in a Python list. This version replaces that with a real embedded database.

## Features

- Add a new task
- View all tasks (with status: Pending / Completed)
- Mark a task as completed
- Delete a task
- Data persists across program runs (stored in a local database file)

## Tech Stack

- Python 3
- `sqlite3` (built into Python's standard library — no extra installation needed)

## Project Structure

.
├── to-do-list.py # CLI menu and program flow
├── database.py # All SQLite logic (create table, insert, view, update, delete)
└── Task_manager # SQLite database file (auto-created on first run)

## How It Works

- `database.py` contains all the database logic, kept separate from the CLI/menu code for clarity
- `to-do-list.py` imports these functions and wires them up to a simple numbered menu
- On startup, `create_table()` ensures the `Tasks` table exists before anything else runs
- Each task is stored with a `task_name` and `task_status` (`"Pending"` or `"Completed"`), plus SQLite's built-in `rowid` used as the task ID

## Getting Started

### Prerequisites

- Python 3 installed (comes with `sqlite3` built in — nothing extra to install)

### Run it

```bash
python to-do-list.py
```

### Menu Options

--- TO-DO LIST ---

Add Task
View Task
Mark Task as Done
Delete Task
Exit

## Example Usage

Please enter your number(1-5): 1
Enter your task: Finish SQLite project
Task Finish SQLite project has been added successfully

Please enter your number(1-5): 2
(1, 'Finish SQLite project', 'Pending')

Please enter your number(1-5): 3
Enter your task number: 1
Task marked as completed

## Possible Future Improvements

- Add due dates / priority levels
- Add input validation (e.g. handle non-numeric task IDs gracefully)
- Turn this into a Flask REST API (in progress as a next step)
- Add a simple GUI or web front-end

## Author

Built as a self-study project while learning Python, SQL, and SQLite fundamentals.
