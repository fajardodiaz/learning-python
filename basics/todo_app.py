#!/usr/bin/python3

todos = []
resp = ""
while resp != "exit":
    resp = input("Type add, edit, show or exit: ")
    resp = resp.lower()
    match resp:
        case "add":
            todo = input("Insert a task: ")
            todos.append(todo)
        case "show":
            if len(todos) > 0:
                for i in todos:
                    print(i)
            else:
                print("Task list is empty")
        case "edit":
            if len(todos) > 0:
                print("ID - TASK")
                for i in range(len(todos)):
                    print(i, "-", todos[i])
                task_id = int(input("ID: "))
                new_task = str(input("Insert the new value: "))
                todos[task_id] = new_task
            else:
                print("Task list is empty")
        case default:
            print("Invalid option")
            
