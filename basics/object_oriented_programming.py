class Student():
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
    
    def print_info(self):
        print(f"Name: {self.name}\nAge: {self.age}\nMajor: {self.major}\n")

student1 = Student("Pablo Fajardo Diaz", 24, "Computer Science")
student2 = Student("Andres Diaz", 20, "Philosophy")

student1.print_info()
student2.print_info()
