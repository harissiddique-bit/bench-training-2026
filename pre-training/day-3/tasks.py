import sys
from task_manager import TaskManager

args = sys.argv[1:]

print(sys.argv)

if len(args) == 0:
    print("Usage:")
    print("  python / python3 tasks.py add 'task title'")
    print("  python / python3 tasks.py done <id>")
    print("  python / python3 tasks.py delete <id>")
    print("  python / python3 tasks.py list")
    print("  python / python3 tasks.py list --filter todo")
    print("  python / python3 tasks.py list --filter done")

else:
    manager = TaskManager()
    command = args[0]

    if command == "add":
        if len(args) < 2:
            print("Please provide a task title.")
        else:
            manager.add_task(args[1])

    elif command == "done":
        if len(args) < 2:
            print("Please provide a task id.")
        else:
            manager.complete_task(int(args[1]))

    elif command == "delete":
        if len(args) < 2:
            print("Please provide a task id.")
        else:
            manager.delete_task(int(args[1]))

    elif command == "list":
        if "--filter" in args:
            i = args.index("--filter")
            manager.list_tasks(filter=args[i + 1])
        else:
            manager.list_tasks()

    else:
        print("Unknown command:", command)