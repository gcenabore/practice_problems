#Create a program that ask user to input 2 numbers. Print the bigger number.

input1 = int(input("Please enter the first number: "))

input2 = int(input("Please enter the second number: "))

if input1 > input2:
    print(f"The highest number is {input1}.")

elif input2 > input1:
    print(f"The highest number is {input2}.")

else:
    print(f"{input1} and {input2} is equal.")



