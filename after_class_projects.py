# setting up dev tools and intro to python
# no ACP for this lesson

# getting started with programming
# question - store 5 birthdays in the format dd/mm/yyyy in five separate variables. Name each variable after the corresponding person, and store the dates as strings
amit = "15/04/1994"
sneha = "20/05/1995"
arun = "30/06/1993"
vinod = "10/07/1992"
mehak = "25/08/1991"
print(amit)

# data types in python
# question - get two integers from the user and print their sum
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
print("Their sum is", num1 + num2)

# python operators - I
# question - get two integers from the user and ask the user which operation they want to perform (addition, subtraction, multiplication, division). Perform the operation and print the result
x = int(input("Enter first integer: "))
y = int(input("Enter second integer: "))
operation = input("Enter operation (add, subtract, multiply, divide): ")
if operation == "add":
    result = x + y
elif operation == "subtract":
    result = x - y
elif operation == "multiply":
    result = x * y
elif operation == "divide":
    result = x / y
else:
    result = "Invalid operation"

print("Result:", result)

# conditional statements
# question - create a simple login system. Ask the user for a username and password, and check if they match stored values. If they match, print "Login successful", otherwise print "Username or password incorrect"
actual_username = "user123"
actual_password = "pass123"
input_username = input("Enter username: ")
input_password = input("Enter password: ")

if input_username == actual_username and input_password == actual_password:
    print("Login successful")
else:
    print("Username or password incorrect")

# python operators - II
# question - ask the user to enter a number that is a multiple of 9. Then print the appropriate response based on whether the number is a multiple of 9 or not
number = int(input("Enter a number that is a multiple of 9: "))
if number % 9 == 0:
    print("Yes, it's a multiple of 9")
else:
    print("No, it's not")


