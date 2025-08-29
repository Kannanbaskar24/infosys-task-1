#"""What is a Variable in Python?
#A variable is like a container (or a name) used to store data in memory.
#It allows you to store, update, and retrieve values during program execution.

name = "Arjun"
age = 20
marks = 85.5
print("Name:", name)
print("Age:", age)
print("Marks:",marks)
      
# Local Variable → A variable declared inside a function and accessible only within that function.

#Global Variable → A variable declared outside all functions and accessible throughout the program.     

name = "Kannan"
def show_name():
    age = 21
    print("Inside function:", name, age)

show_name()
print("Outside function:",name)