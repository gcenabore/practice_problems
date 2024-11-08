#15. Create a program that ask user to input 10 numbers. Print how many are even numbers.

even_count = 0

for x in range(10):
    num = int(input(f"Please enter number {x + 1}: "))

    if num % 2 != 1:
        even_count += 1

print(f"The counts of even numbers are: {even_count}")


