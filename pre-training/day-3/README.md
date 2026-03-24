Day 3 — Task Tracker

A simple command-line task tracker. Tasks are saved to `tasks.json` so they survive between runs.

Project structure
```
day-3/
├── task.py
├── task_manager.py
├── main.py
└── tasks.json       ← created automatically
```

How to run
```bash
python tasks.py add 'Fix login bug'
python tasks.py done 1
python tasks.py delete 2
python tasks.py list
python tasks.py list --filter todo
python tasks.py list --filter done
```

Why classes instead of just functions?

With just functions I would have to pass the tasks list into every function manually `add_task(tasks, title)`, `delete_task(tasks, id)` and so on.
With a class, `TaskManager` holds the list inside itself so every method just uses `self.tasks`. Create it once, call `manager.add_task()` anywhere.
Classes make sense when you have data and actions that belong together.
