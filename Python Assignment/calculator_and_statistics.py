#Name:Rupali Akter
#ID:23
#Problem:12
#Function-Based Calculator and Statistics

import math


def add(first_number, second_number):
    return first_number + second_number


def subtract(first_number, second_number):
    return first_number - second_number


def multiply(first_number, second_number):
    return first_number * second_number


def divide(first_number, second_number):
    if second_number == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return first_number / second_number


def find_max(numbers):
    if not numbers:
        raise ValueError("At least one number is required.")
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest


def find_min(numbers):
    if not numbers:
        raise ValueError("At least one number is required.")
    smallest = numbers[0]
    for number in numbers[1:]:
        if number < smallest:
            smallest = number
    return smallest


def calculate_average(numbers):
    if not numbers:
        raise ValueError("At least one number is required.")
    return sum(numbers) / len(numbers)


def is_prime(number):
    if number < 2:
        return False
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


def read_float(prompt):
    while True:
        try:
            number = float(input(prompt))
            if math.isfinite(number):
                return number
            print("Error: Enter a finite number.")
        except ValueError:
            print("Error: Enter a valid number.")


def read_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Enter a valid integer.")


def read_number_list():
    while True:
        count = read_integer("How many numbers? ")
        if count > 0:
            break
        print("Error: Enter a count greater than zero.")

    numbers = []
    for index in range(count):
        numbers.append(read_float(f"Enter number {index + 1}: "))
    return numbers


def main():
    while True:
        print("\nCalculator and Statistics")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Find maximum")
        print("6. Find minimum")
        print("7. Calculate average")
        print("8. Check whether an integer is prime")
        print("9. Exit")
        choice = input("Select an option: ").strip()

        if choice in ("1", "2", "3", "4"):
            first_number = read_float("Enter first number: ")
            second_number = read_float("Enter second number: ")
            try:
                if choice == "1":
                    result = add(first_number, second_number)
                elif choice == "2":
                    result = subtract(first_number, second_number)
                elif choice == "3":
                    result = multiply(first_number, second_number)
                else:
                    result = divide(first_number, second_number)
                print(f"Result: {result}")
            except ZeroDivisionError as error:
                print(f"Error: {error}")
        elif choice in ("5", "6", "7"):
            numbers = read_number_list()
            if choice == "5":
                print(f"Maximum: {find_max(numbers)}")
            elif choice == "6":
                print(f"Minimum: {find_min(numbers)}")
            else:
                print(f"Average: {calculate_average(numbers)}")
        elif choice == "8":
            number = read_integer("Enter an integer: ")
            print(f"Prime: {'Yes' if is_prime(number) else 'No'}")
        elif choice == "9":
            print("Exiting Calculator and Statistics.")
            break
        else:
            print("Error: Select a number from 1 to 9.")


if __name__ == "__main__":
    main()