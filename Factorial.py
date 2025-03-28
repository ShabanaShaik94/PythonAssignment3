# Program to perform Factorial

# Taking an integer as input from the user
num = int(input("Enter a number: "))

def factorial(n):
    if n < 2:
        return 1
    else :
        return n * (factorial(n-1))

# Displaying the Factorial results
print(f"Factorial of {num} is : {factorial(num)}")