def new_decorator(original_func):
    def wrap_func():
        print("Start the function")
        original_func()
        print("End the function")

    return wrap_func

@new_decorator
def func_needs_decorator():
    print("I want to be decorated!!!")

@new_decorator
def func_needs_another_decorator():
    print("I want to be double decorated!")

func_needs_decorator()
print("\n\n")
func_needs_another_decorator()