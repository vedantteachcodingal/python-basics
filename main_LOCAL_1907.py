# setting up dev tools and intro to python
print("hello")

# getting started with programming
m = 10
print(m)

# data types in python
x = 4
y = 5
print(x + y)

a = "4"
b = "5"
print(a + b)

print(type(x))
print(type(a))

weight_in_kg = 60.5
print(type(weight_in_kg))

isMarried = True # or False
print(type(isMarried))

birth_year = input("Enter your birth year: ")
age = 2025 - int(birth_year)
print("Your age is", age)

# python operators - I
age_1 = 25
age_2 = 35
age_3 = 50
sum = age_1 + age_2 + age_3
average = sum / 3
print("Average:", average)

print("Welcome to ATM")
amount = input("Enter amount (in multiples of 100) to withdraw: ")
amount = int(amount)
note_500 = amount // 500
amount = amount % 500
note_200 = amount // 200
amount = amount % 200
note_100 = amount // 100

print("500 note count:", note_500)
print("200 note count:", note_200)
print("100 note count:", note_100)

print("Enter marks obtained (out of 100) in the below 4 subjects:")
maths = int(input("Maths: "))
science = int(input("Science: "))
english = int(input("English: "))
history = int(input("History: "))
total_marks = maths + science + english + history
percentage = (total_marks / 400) * 100  
print("Percentage:", percentage, end="%")
print("\n")


# conditional statements
number = int(input("Enter a number: "))
if number > 0:
    print("Its a positive number")
elif number < 0:
    print("Its a negative number")
else:
    print("Its zero")

cost_price = int(input("Enter cost price of the apple: "))
selling_price = int(input("Enter selling price of the apple: "))

profit = selling_price - cost_price

if selling_price > cost_price:
    print(f"You made a profit of ₹{profit}")
elif selling_price < cost_price:
    print(f"You incurred a loss of ₹{-profit}")
else:
    print("No Profit No Loss")


first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

if first_number > second_number:
    print("First number is greater than second number")
elif first_number < second_number:
    print("Second number is greater than first number")
else:
    print("Both numbers are equal")


number = int(input("Enter a number to check for even/odd: "))
remainder = number % 2
if remainder == 0:
    print("It's even")
else:
    print("It's odd")


# python operators - II
a = 10
b = 20
result = a > b
print(result)

x = 10
y = -20
z = -30
if x > 0 or y > 0 or z > 0:
    print("At least one number is positive")
else:
    print("All numbers are negative or zero")


body_temperature = 38
if body_temperature != 37:
    print("Abnormal body temperature detected")


height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))
bmi_denominator = (height / 100)**2
bmi = weight / bmi_denominator
if bmi < 18.5:
    print("You are underweight")
elif bmi < 24.9:
    print("You have a normal weight")
elif bmi < 29.9:
    print("You are overweight")
else:
    print("You are obese")

print("Your BMI is", round(bmi, 2))

year = int(input("Enter a year to check if it's a leap year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It's a leap year!")
else:
    print("It's not a leap year")

