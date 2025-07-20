from operator import concat
#Task 1: Perform Basic Mathematical Operation
a=input("Enter the first number: ")
b=input("Enter the Second number: ")
a=int(a)
b=int(b)
print("Addition: ",a+b)
print("subtraction: ",a-b)
print("Multiplication: ",a*b)
print("division: ",a/b)

#task 2: Create a personalised Greeting
first_name=input("Enter your first name: ")
last_name=input("Enter your last name:  ")
full_name= first_name+" "+last_name
print("Hello, ",full_name,"! Welcome to the python program.")