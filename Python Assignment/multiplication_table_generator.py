#Name:Rupali Akter
#Student ID:23
#Problem:05
#multiplication table generator


def multiplication_table(number):
    for i in range(1, 21):
        print(f"{number} x {i} = {number * i}")

while True:
    try:
        number = int(input("Enter a number: "))
        if number < 1:
            print("Please enter a positive integer.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

multiplication_table(number)

choice = input(f"Do you want to see tables from 1 to {number}? (y/n): ").strip().lower()

if choice == "y":
    for table_number in range(1, number + 1):
        print(f"\nMultiplication Table of {table_number}:")
        multiplication_table(table_number)