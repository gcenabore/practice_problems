#12. Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

sum = 0

for x in range(10):
    number = int(input("Pleease enter a number: "))

    sum += number

print(f"The sum of all number is {sum}")

