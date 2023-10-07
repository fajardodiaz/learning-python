#!/usr/bin/python3

todos = []
resp = ""
while resp != "exit":
    resp = input("Type add, show or exit: ")
    match resp:
        case "add":
            todo = input("Insert a task: ")
            todos.append(todo)
        case "show":
            for i in todos:
                print(i)
