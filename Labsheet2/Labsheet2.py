# Q1: Check multiple of both 3 and 7

num = int(input("Enter a number: "))

if num % 3 == 0 and num % 7 == 0:
    print("The number is a multiple of both 3 and 7")
else:
    print("The number is not a multiple of both 3 and 7")


# Q2: Check palindrome number

num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome number")

# Q3: Check Armstrong number

num = int(input("Enter a number: "))

original = num
temp = num
digits = 0

# Count number of digits
while temp > 0:
    digits += 1
    temp //= 10

temp = num
total = 0

# Calculate sum of powers of digits
while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10

if total == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")


# Q3: Check Armstrong number

num = int(input("Enter a number: "))

original = num
temp = num
digits = 0

# Count number of digits
while temp > 0:
    digits += 1
    temp //= 10

temp = num
total = 0

# Calculate sum of powers of digits
while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10

if total == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

# Q4: Display grade

marks = float(input("Enter marks: "))

if 90 <= marks <= 100:
    print("Grade A")
elif 75 <= marks < 90:
    print("Grade B")
elif 50 <= marks < 75:
    print("Grade C")
elif 0 <= marks < 50:
    print("Grade F")
else:
    print("Invalid marks")


# Q5: Find absolute value

num = float(input("Enter a number: "))

if num < 0:
    num = -num

print("Absolute value =", num)

# Q6: Check valid triangle using angles

a = float(input("Enter first angle: "))
b = float(input("Enter second angle: "))
c = float(input("Enter third angle: "))

if a > 0 and b > 0 and c > 0 and a + b + c == 180:
    print("Valid triangle")
else:
    print("Invalid triangle")

# Q7: Find type of triangle

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Invalid triangle")
elif a == b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")

# Q8: Check substring

text = input("Enter the string: ")
substring = input("Enter the substring: ")

if substring in text:
    print("Substring found")
else:
    print("Substring not found")


# Q9: Check voting eligibility

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible for voting")
else:
    print("Not eligible for voting")


# Q10: Find smallest number

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a <= b and a <= c:
    smallest = a
elif b <= a and b <= c:
    smallest = b
else:
    smallest = c

print("Smallest =", smallest)

# Q11: Print 1 to 10

for i in range(1, 11):
    print(i)


# Q12: Print 10 to 1

i = 10

while i >= 1:
    print(i)
    i -= 1

# Q13: Sum of first n natural numbers

n = int(input("Enter n: "))

total = 0

for i in range(1, n + 1):
    total += i

print("Sum =", total)


# Q14: Multiplication table

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# Q15: Even numbers from 1 to 50

for i in range(2, 51, 2):
    print(i)


# Q16: Odd numbers from 1 to 50

for i in range(1, 51, 2):
    print(i)


# Q17: Factorial

n = int(input("Enter a number: "))

if n < 0:
    print("Factorial is not defined for negative numbers")
else:
    factorial = 1

    for i in range(1, n + 1):
        factorial = factorial * i

    print("Factorial =", factorial)

# Q18: Fibonacci series

n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

print()


# Q19: Reverse a number

num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reverse =", reverse)


# Q20: Count digits

num = int(input("Enter a number: "))

num = abs(num)

if num == 0:
    count = 1
else:
    count = 0

    while num > 0:
        count += 1
        num //= 10

print("Number of digits =", count)


# Q21: Sum of digits

num = int(input("Enter a number: "))

num = abs(num)
total = 0

while num > 0:
    digit = num % 10
    total += digit
    num //= 10

print("Sum of digits =", total)



# Q22: Prime numbers from 1 to 100

for num in range(2, 101):

    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")

print()


# Q23: Check perfect number

num = int(input("Enter a number: "))

total = 0

for i in range(1, num):
    if num % i == 0:
        total += i

if total == num and num > 0:
    print("Perfect number")
else:
    print("Not a perfect number")


# Q24: Star pattern

for i in range(1, 6):

    for j in range(i):
        print("*", end=" ")

    print()

# Q25: Reverse star pattern

for i in range(5, 0, -1):

    for j in range(i):
        print("*", end=" ")

    print()

# Q26: Number pyramid

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):

    # Print spaces
    for j in range(n - i):
        print(" ", end=" ")

    # Print numbers
    for j in range(1, i + 1):
        print(j, end=" ")

    print()

# Q27: Tables from 1 to 10

for num in range(1, 11):

    print("Table of", num)

    for i in range(1, 11):
        print(num, "x", i, "=", num * i)

    print()


# Q28: Find HCF

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = abs(a)
b = abs(b)

hcf = 1

limit = min(a, b)

for i in range(1, limit + 1):

    if a % i == 0 and b % i == 0:
        hcf = i

print("HCF =", hcf)

# Q29: Find LCM

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = abs(a)
b = abs(b)

if a == 0 or b == 0:
    print("LCM = 0")
else:

    if a > b:
        lcm = a
    else:
        lcm = b

    while True:

        if lcm % a == 0 and lcm % b == 0:
            break

        lcm += 1

    print("LCM =", lcm)


# Q30: Check Strong number

num = int(input("Enter a number: "))

original = num
total = 0

while num > 0:

    digit = num % 10

    factorial = 1

    for i in range(1, digit + 1):
        factorial *= i

    total += factorial

    num //= 10

if total == original:
    print("Strong number")
else:
    print("Not a strong number")