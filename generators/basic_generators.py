# 
# A decorator is a design pattern that allows you to modify the functionality of a function by wrapping it in another function
# Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of a function or class. 
# 

# Python has decorators that allow you to tack on extra functionality to an already existing function
# They use the @ operator and are then placed on top of the original function


def hello():
    return "Hello!"

print(hello())
print(hello)

greet = hello



