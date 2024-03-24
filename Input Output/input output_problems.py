# Start of Program
print('Hello World')

# 1. Write a program to print whether a number is even or odd, also take input from the user.
num = input("Enter a number: ")
num = int(num)
def isEven(x):
    if(x%2 == 0):
        print("This number is even")
    else:
        print("This number is odd")

isEven(num)
#                                           <!====== ===========>
 
# 2. Take name as input and print a greeting message for that particular name.
name = input("Enter your name: ")
print("Good Morning, "+name)
#                                           <!====== ===========>

# 3. Write a program to input principal, time, and rate (P, T, R) from the user and find Simple Interest.
principal_amount = int(input("Enter your principal amount: "))
time = int(input("Enter time: "))
interest_rate = int(input("Enter your interest rate: "))
interest = (principal_amount * time * interest_rate) 
interest = interest/100
print("Your interest rate is " + str(interest))
#                                           <!====== ===========>

# 4. Take in two numbers and an operator (+, -, *, /) and calculate the value. (Use if conditions)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
opr = input("Enter any operator any of these (+, -, *, /): ")

global result 
# Calculator Function
def calculator(a, b):
    if (opr == "+"):
        result = a + b
    elif (opr == "-"):
        result = a - b
    elif (opr == "*"):
        result = a * b
    elif (opr == "/"):
        result = a / b
    return result

result = calculator(a=num1, b=num2)
print ("Result is: " + str(result))
#                                           <!====== ===========>

# 5. Take 2 numbers as input and print the largest number.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

def largestNum(a , b):
    if (a > b):
        print("Largest Number is: " + str(a))
    elif (a < b):
        print("Largest Number is: " + str(b))
    else:
        print("Both numbers are equal")

largestNum(num1, num2)
#                                           <!====== ===========>

# 6. Input currency in rupees and output in USD.
from math import ceil

num1 = int(input("Enter your amount in rupees: "))
global result
def pkrToUsd(x):
    result = x / 280
    return result
result = round(pkrToUsd(num1),2)
print("Your amount in USD is: " + str(result))
#                                           <!====== ===========>

# 7. To calculate Fibonacci Series up to n numbers.
num1 = int(input("Enter number: "))
count = 0
a, b = 0, 1
while count < num1:
    print(a)
    c = a + b
    a = b
    b = c
    count += 1
#                                           <!====== ===========>

# 8. To find Armstrong Number between two given number.
number = int(input("Enter number: "))
sum = 0
num1 = number

while (num1 > 0):
    x = num1 % 10
    sum += x ** 3
    num1 = num1 // 10

if (number == sum):
    print('This number is a armstrong number.')
else:
    print('This number is not a armstrong number.')
#                                           <!====== ===========>
