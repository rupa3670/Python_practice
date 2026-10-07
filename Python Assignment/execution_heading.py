#Name:Rupali Akter
#ID:23
#Problem:14
#Exception Handling and Input Validation

import math


def read_nonempty(prompt, field_name):
	while True:
		value = input(prompt).strip()
		if value:
			return value
		print(f"Invalid {field_name}!\n{field_name} cannot be empty.\n")


def read_age():
	while True:
		try:
			age = int(input("Enter Age: "))
			if age >= 0:
				return age
			print("Invalid Age!\nAge cannot be negative.\n")
		except ValueError:
			print("Invalid Age!\nPlease enter an integer.\n")


def read_marks():
	while True:
		try:
			marks = float(input("Enter Marks: "))
			if math.isfinite(marks) and 0 <= marks <= 100:
				return marks
			print("Invalid Marks!\nMarks must be between 0 and 100.\n")
		except ValueError:
			print("Invalid Marks!\nPlease enter a number.\n")


def read_cgpa():
	while True:
		try:
			cgpa = float(input("Enter CGPA: "))
			if math.isfinite(cgpa) and 0 <= cgpa <= 4:
				return cgpa
			print("Invalid CGPA!\nCGPA must be between 0 and 4.\n")
		except ValueError:
			print("Invalid CGPA!\nPlease enter a number.\n")


def read_finite_number(prompt):
	while True:
		try:
			number = float(input(prompt))
			if math.isfinite(number):
				return number
			print("Invalid number! Please enter a finite number.\n")
		except ValueError:
			print("Invalid number! Please enter a number.\n")


def perform_optional_division():
	while True:
		answer = input("Would you like to perform a division? (yes/no): ").strip().lower()
		if answer in ("yes", "y"):
			numerator = read_finite_number("Enter the numerator: ")
			while True:
				denominator = read_finite_number("Enter the divisor: ")
				if denominator != 0:
					print(f"Division result: {numerator / denominator}")
					return
				print("Invalid divisor! Division by zero is not allowed. Please enter it again.\n")
		elif answer in ("no", "n"):
			return
		else:
			print("Please answer yes or no.\n")


def main():
	name = read_nonempty("Enter Name: ", "Name")
	age = read_age()
	marks = read_marks()
	cgpa = read_cgpa()

	print("\nStudent Information")
	print(f"Name: {name}")
	print(f"Age: {age}")
	print(f"Marks: {marks:g}")
	print(f"CGPA: {cgpa:g}")

	perform_optional_division()


if __name__ == "__main__":
	main()
