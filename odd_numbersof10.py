#14. Create a program that ask user to input 10 numbers. Print how many are odd numbers.

odd_count = 0

for x in range(10):
    num = int(input(f"Please enter number {x + 1}: "))
    if num % 2 != 0:
        odd_count += 1

print(f"the number of odd number is {odd_count}")