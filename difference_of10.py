#13 .Create a program that ask user to input 10 numbers. Print the difference of all the numbers.

first_num = int(input("Enter the first number to be subtracted with: "))
difference = first_num

for x in range(2, 11):
    num = int(input(f"Please enter number{x}: "))

    difference -= num

print(f"the difference of all the numbers is {difference}")