# Q1: Add two integers

num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))

result = num1 + num2

print("Sum =", result)

# Q2: Subtract two integers

num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))

result = num1 - num2

print("Difference =", result)

# Q3: Multiply two integers

num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))

result = num1 * num2

print("Product =", result)

# Q4: Find quotient and remainder

num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))

quotient = num1 // num2
remainder = num1 % num2

print("Quotient =", quotient)
print("Remainder =", remainder)

# Q5: Find square and cube

num = float(input("Enter a number: "))

square = num ** 2
cube = num ** 3

print("Square =", square)
print("Cube =", cube)

# Q6: Calculate area of rectangle

length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width

print("Area of rectangle =", area)

# Q7: Calculate perimeter of circle

radius = float(input("Enter radius: "))

pi = 3.14159
perimeter = 2 * pi * radius

print("Perimeter of circle =", perimeter)

# Q8: Swap two variables using temporary variable

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

temp = a
a = b
b = temp

print("After swapping:")
print("a =", a)
print("b =", b)

# Q9: Swap two variables without temporary variable

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

a = a + b
b = a - b
a = a - b

print("After swapping:")
print("a =", a)
print("b =", b)

# Q10: Convert Celsius to Fahrenheit

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Temperature in Fahrenheit =", fahrenheit)


# Q11: Convert Fahrenheit to Celsius

fahrenheit = float(input("Enter temperature in Fahrenheit: "))

celsius = (fahrenheit - 32) * 5 / 9

print("Temperature in Celsius =", celsius)

# Q12: Calculate simple interest

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest =", simple_interest)


# Q13: Calculate compound interest

principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual rate of interest: "))
time = float(input("Enter time in years: "))

amount = principal * (1 + rate / 100) ** time
compound_interest = amount - principal

print("Compound Interest =", compound_interest)
print("Total Amount =", amount)

# Q14: Calculate average of three numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

average = (num1 + num2 + num3) / 3

print("Average =", average)

# Q15: Convert kilometers to miles

kilometers = float(input("Enter distance in kilometers: "))

miles = kilometers * 0.621371

print("Distance in miles =", miles)

# Q16: Find remainder

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

remainder = num1 % num2

print("Remainder =", remainder)

# Q17: Calculate power without using pow()

base = float(input("Enter base: "))
exponent = int(input("Enter exponent: "))

result = 1

for i in range(exponent):
    result = result * base

print("Result =", result)

# Q18: Calculate BMI

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height ** 2)

print("BMI =", bmi)

# Q19: Calculate monthly EMI

principal = float(input("Enter loan amount: "))
annual_rate = float(input("Enter annual interest rate (%): "))
years = int(input("Enter loan period in years: "))

monthly_rate = annual_rate / (12 * 100)
months = years * 12

if monthly_rate == 0:
    emi = principal / months
else:
    emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / \
          ((1 + monthly_rate) ** months - 1)

print("Monthly EMI =", emi)


# Q20: Calculate percentage of marks in 5 subjects

marks1 = float(input("Enter marks of subject 1: "))
marks2 = float(input("Enter marks of subject 2: "))
marks3 = float(input("Enter marks of subject 3: "))
marks4 = float(input("Enter marks of subject 4: "))
marks5 = float(input("Enter marks of subject 5: "))

total = marks1 + marks2 + marks3 + marks4 + marks5
percentage = (total / 500) * 100

print("Total marks =", total)
print("Percentage =", percentage, "%")


# Q21: Check positive or negative

num = float(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")


# Q22: Check even or odd

num = int(input("Enter an integer: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# Q23: Check whether number is divisible by 5

num = int(input("Enter a number: "))

if num % 5 == 0:
    print("The number is divisible by 5")
else:
    print("The number is not divisible by 5")

# Q24: Check leap year

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")

# Q25: Find largest of two numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    print("Largest =", num1)
elif num2 > num1:
    print("Largest =", num2)
else:
    print("Both numbers are equal")

# Q26: Find largest of three numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print("Largest =", largest)


# Q27: Check vowel or consonant

character = input("Enter a character: ")

if len(character) != 1:
    print("Please enter only one character")
elif character.lower() in "aeiou":
    print("Vowel")
elif character.isalpha():
    print("Consonant")
else:
    print("Not an alphabet")


# Q28: Check uppercase, lowercase, or digit

character = input("Enter a character: ")

if len(character) != 1:
    print("Please enter only one character")
elif character.isupper():
    print("Uppercase")
elif character.islower():
    print("Lowercase")
elif character.isdigit():
    print("Digit")
else:
    print("Special character")


# Q29: Check whether number is in a given range

num = float(input("Enter a number: "))
minimum = float(input("Enter minimum value: "))
maximum = float(input("Enter maximum value: "))

if minimum <= num <= maximum:
    print("The number is within the range")
else:
    print("The number is outside the range")


# Q30: Check whether a number is prime

num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number")
else:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")