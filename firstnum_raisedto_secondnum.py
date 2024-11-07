#11. Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.

num1 = float(input("Please enter a number (Base): "))

num2 = float(input("Please enter a number (Exponent): "))

result = num1 ** num2

print(f"when {num1} is raised to the power of {num2} the answer would be: {result}")
