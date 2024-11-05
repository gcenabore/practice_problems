#2. Create a program that ask user to input 2 numbers. Print the lower number.

input1 = int(input("Please enter first number: "))

input2 = int(input("Please enter second number: "))

if input1 < input2:
    print(f"{input1} is the lowest number.")

elif input2 < input1:
    print(f"{input2} is the lowest number.")

else:
    print(f"{input1} and {input2} is equal.")