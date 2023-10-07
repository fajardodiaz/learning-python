#!/usr/bin/python3

user_prompt = "Enter a todo: "

i = 0
todos = list()
while i != 4:
    todo = input(user_prompt)
    todos.append(todo)
    i += 1

print(todos)